import re
import tweepy
from tweepy import OAuthHandler
import time
from time import sleep
import textblob
from textblob import TextBlob


consumer_key='0q2L2AcmJTTwheRp2UdIWVR8E'
consumer_secret='8K3zBCDnVh3OUz3FmpV2w4NWmEcwMcKIgl1gS3t8Be1Jzg7pBX'
access_token='715235391847026689-lhtJfxhTrNPV2OxxCiON7P3nLeN3tIp'
access_token_secret='zYalAAytrQJBA5IbOmjcu8erWckPxa84BiZKaiikiRSbN'

auth= tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)
api=tweepy.API(auth)


def retrieve_tweets():
    tweets=api.search("#Dhoni")
    print(tweets)


def f_count():
    follower_count = api.get_user('@balwantrawat333').followers_count
    print(follower_count)


def update_status():
    update_status=api.update_status(status ="Hello Everyone !")
    print(update_status)


def display_menu():
    print('''what do you want:
    1.) Retrieve Tweets
    2.) f count
    3.) update status
    ''')
    option=int(input("enter the option you want to retrieve: "))
    if (option==1):
        retrieve_tweets()
        display_menu()
    elif (option == 2):
        f_count()
        display_menu()
    elif (option == 3):
        update_status()
        display_menu()




display_menu()

