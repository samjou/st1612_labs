import json
import boto3
import kafka
import time
import os

# AWS CREDENTIALS
AWS_ACCESS_KEY_ID = os.environ['EDUCATE_AWS_ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY= os.environ['EDUCATE_AWS_SECRET_ACCESS_KEY']
AWS_SESSION_TOKEN= os.environ['EDUCATE_AWS_SESSION_TOKEN']

# KAFKA DATA
BUCKET_NAME = 'raw.finalproject'
TOPIC_NAME = 'sample-topic'
KAFKA_SERVER = 'ec2-54-175-184-211.compute-1.amazonaws.com:9092'
PREFIX = 'tweets'

consumer = kafka.KafkaConsumer( 
        TOPIC_NAME,
        bootstrap_servers=KAFKA_SERVER, 
        enable_auto_commit=True, 
        auto_commit_interval_ms=30 * 1000, 
        auto_offset_reset='smallest')

s3 = boto3.client(
        's3',
        aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
        aws_session_token=AWS_SESSION_TOKEN)

def save_to_s3(data, bucket_name, key_prefix):
    timestamp = str(time.time()) #.split('.')[0]
    s3.put_object(
        Body=json.dumps(data),
        Bucket=bucket_name,
        Key=f"{key_prefix}/{timestamp}.json",
        ContentType='application/json'
    )

for message in consumer:
    data = json.loads(message.value)
    print(f"Debug: Saving tweet {data}")
    save_to_s3(data, BUCKET_NAME, PREFIX)
