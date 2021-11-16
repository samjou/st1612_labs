from __future__ import print_function
import tweepy
import json
import os
from kafka import KafkaProducer

# Twitter Secrets
CONSUMER_KEY = os.environ['TWITTER_CONSUMER_KEY']
CONSUMER_SECRET = os.environ['TWITTER_CONSUMER_SECRET']
ACCESS_TOKEN = os.environ['TWITTER_ACCESS_TOKEN']
ACCESS_TOKEN_SECRET = os.environ['TWITTER_ACCESS_TOKEN_SECRET']
WORDS = ['EnriquePenalosa', 'RoyBarreras', 'agaviriau', 'juanmanuelgalan', 'petrogustavo', 'sergio_fajardo']

# Kafka Config
KAFKA_TOPIC = "raw-topic"
KAFKA_SERVER = 'ec2-54-175-184-211.compute-1.amazonaws.com:9092'

producer = KafkaProducer(
    value_serializer=lambda v: json.dumps(v).encode('utf-8'), 
    bootstrap_servers=KAFKA_SERVER)

class StreamListener(tweepy.StreamListener):
    #This is a class provided by tweepy to access the Twitter Streaming API.

    def on_connect(self):
        # Called initially to connect to the Streaming API
        print("You are now connected to the streaming API.")

    def on_error(self, status_code):
        # On error - if an error occurs, display the error / status code
        print('An Error has occured: ' + repr(status_code))
        return False

    def on_data(self, data):
        #This is the meat of the script...it connects to your mongoDB and stores the tweet
        try:
            # Decode the JSON from Twitter
            datajson = json.loads(data)

            #grab the 'created_at' data from the Tweet to use for display
            created_at = datajson['created_at']

            #print out a message to the screen that we have collected a tweet
            print("Tweet collected at " + str(created_at))

            #insert the data into the mongoDB into a collection called twitter_search
            #if twitter_search doesn't exist, it will be created.

            producer.send(KAFKA_TOPIC, datajson)
            #producer.send('sampletopic', key=b'message-two', value=b'This is Kafka-Python')
            producer.flush()

        except Exception as e:
           print(e)

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
#Set up the listener. The 'wait_on_rate_limit=True' is needed to help with Twitter API rate limiting.
listener = StreamListener(api=tweepy.API(wait_on_rate_limit=True))
streamer = tweepy.Stream(auth=auth, listener=listener)
print("Tracking: " + str(WORDS))
streamer.filter(track=WORDS)
