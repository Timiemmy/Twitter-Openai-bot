import tweepy
import openai
import random
import time
import os
from dotenv import load_dotenv

load_dotenv('.env')


class My_twitter_bot(tweepy.StreamingClient):
    api_key = os.getenv('api_key')
    api_secret_key = os.getenv('api_secret_key')
    bearer_token = os.getenv('bearer_token')
    access_token = os.getenv('access_token')
    access_token_secret = os.getenv('access_token_secret')

    openai.api_key = os.getenv('OPENAI_API_KEY')

    client = tweepy.Client(bearer_token, api_key,
                           api_secret_key, access_token, access_token_secret)

    auth = tweepy.OAuth1UserHandler(
        api_key, api_secret_key, access_token, access_token_secret)
    api = tweepy.API(auth)

    prompts = [
        {
            "hashtag": "#python #backenddeveloper",
            "text": "post something about backend developer"
        },
        {
            "hashtag": "#djangorestframework #apidevelopemt #techtwitter",
            "text": "post something about django rest framework"
        },
        {
            "hashtag": "#python #backenddeveloper",
            "text": "post about python backend developer"
        },
        {
            "hashtag": "#python #apidevelopment",
            "text": "post about api"
        },
        {
            "hashtag": "#mysql #python",
            "text": "post something about mysql"
        },
        {
            "hashtag": "#mysql #database",
            "text": "answer question about mysql"
        },
        {
            "hashtag": "#mongodb #database",
            "text": "post something about mongodb"
        },
        {
            "hashtag": "#mongodb #database",
            "text": "answer question about mongodb"
        },
        {
            "hashtag": "#webdeveloper #webdevelopment #python",
            "text": "tweet a quote on web development"
        },
        {
            "hashtag": "#webdeveloper #webdevelopment #python #techtwitter",
            "text": "tweet a quote on programming"
        },
        {
            "hashtag": "#backenddeveloper #python #techtwitter",
            "text": "post about how to start backend development"
        },
        {
            "hashtag": "#apideveloper #python",
            "text": "post about consistency"
        },
    ]

    def __init__(self):
        error = 1
        while error == 1:
            tweet = self.create_tweet()
            try:
                print('connected')
                error = 0
                self.api.update_status(tweet)
            except:
                error = 1

    def create_tweet(self):
        chosen_prompt = random.choice(self.prompts)
        text = chosen_prompt["text"]
        hashtags = chosen_prompt["hashtag"]

        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=text,
            temperature=0.7,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        tweet = response.choices[0].text
        tweet = tweet + " " + hashtags
        return tweet


while True:
    twitter = My_twitter_bot()
    twitter.create_tweet()

    time.sleep(10)
