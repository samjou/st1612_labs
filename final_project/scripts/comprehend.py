from kafka import KafkaClient
from kafka import KafkaConsumer
from kafka import KafkaProducer
import json
import boto3
import os

# AWS CREDENTIALS
AWS_ACCESS_KEY_ID = os.environ['NON_EDUCATE_AWS_ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY = os.environ['NON_EDUCATE_AWS_SECRET_ACCESS_KEY']

# KAFKA CONFIG
KAFKA_SERVER = 'ec2-54-175-184-211.compute-1.amazonaws.com:9092'
CONSUMER_KAFKA_TOPIC = 'raw-topic'
PRODUCER_KAFKA_TOPIC = 'sentiment-topic'

producer = KafkaProducer(bootstrap_servers=KAFKA_SERVER)
consumer = KafkaConsumer(
        CONSUMER_KAFKA_TOPIC, 
        bootstrap_servers=KAFKA_SERVER, 
        enable_auto_commit=True, 
        auto_commit_interval_ms=30 * 1000, 
        auto_offset_reset='smallest')

comprehend = boto3.client(
    service_name='comprehend', 
    region_name='eu-west-1',
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY)

for message in consumer:
    tweets = json.loads(message.value)[u'text'].strip()
    sentiment_all = comprehend.detect_sentiment(Text=tweets, LanguageCode='es')
    sentiment = sentiment_all['Sentiment']
    positive = sentiment_all['SentimentScore']['Positive']
    negative = sentiment_all['SentimentScore']['Negative']
    total = positive - negative
    data_record = {
        'message': tweets,
        'sentiment': sentiment,
        'total': total
    }
    producer.send(PRODUCER_KAFKA_TOPIC, json.dumps(data_record).encode('utf-8'))
