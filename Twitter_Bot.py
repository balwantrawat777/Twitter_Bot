import re
import tweepy
from tweepy import OAuthHandler
import time
from time import sleep
import textblob
from textblob import TextBlob
import paralleldots
from collections import Counter
import nltk
from nltk.corpus import *
nltk.download('stopwords')



consumer_key='0q2L2AcmJTTwheRp2UdIWVR8E'
consumer_secret='8K3zBCDnVh3OUz3FmpV2w4NWmEcwMcKIgl1gS3t8Be1Jzg7pBX'
access_token='715235391847026689-lhtJfxhTrNPV2OxxCiON7P3nLeN3tIp'
access_token_secret='zYalAAytrQJBA5IbOmjcu8erWckPxa84BiZKaiikiRSbN'
paralleldots.set_api_key("j6QuF8ZrmEDmRLqNCEZIpA3r7OF0GrPE3c5iDZEyas4")

auth= tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)
api=tweepy.API(auth)

paralleldots.get_api_key()


def retrieve_tweets():
    global tweets
    tweet_input = input("enter the hashtag you want to search")
    tweets = api.search(q=tweet_input)
    print(tweets)


def f_count():
    tweet_input = input("enter the hashtag you want to search")
    tweets = api.search(q=tweet_input)
    print("UserName      Follower Count")

    for tweet in tweets:
        print(tweet.user.name + "     " + str(tweet.user.followers_count))



def update_status():
    update_status=api.update_status(status ="Hello Everyone !")
    print(update_status)

def tweet_location():
    tweets=input("enter the hashtag to search")
    tweet1=api.search(tweets)
    for search_results in tweet1:
        print('location',search_results.user.location)
        print('time_zone',search_results.user.time_zone)
        print('language',search_results.user.lang)

def sentiments():
    tweet_input = input("enter the hashtag you want to search")
    tweets = api.search(q=tweet_input)
    print(tweets)

    for tweet in tweets:
        text = tweet.text

    print("\nSentiments")
    print(paralleldots.sentiment("i am very lucky")["sentiment"])


def stwords():
    global count
    stop_words = set(stopwords.words('english'))
    x = [x.upper() for x in stop_words]
    tweets = api.user_timeline(screen_name="dhoni", count=20, tweet_mode="extended")
    for tweet_compare in tweets:
        fulltext = tweet_compare.full_text
        tmp = []
        tmp.append(fulltext)
        temp = tmp
        import re
        cur_tweet = re.sub(r"http\S+", "", str(temp))
        cur_tweet1 = re.split(r"\s", cur_tweet)
        cur_tweet = [w for w in cur_tweet1 if not w in stop_words]
        cur_tweet=[]
        for w in cur_tweet1:
            if w not in stop_words:
                cur_tweet.append(w)
                count = Counter(cur_tweet).most_common(5)
        print(count)


def compare():
    flagword = 0
    flagword1 = 0
    # for narendra modi
    tweets = api.user_timeline(screen_name="narendramodi", count=200, tweet_mode="extended")
    for tweet_compare in tweets:
        fulltext = tweet_compare.full_text
        tmp = []
        tmp.append(fulltext)
        temp = tmp
        import re
        cur_tweet = re.sub(r"http\S+", "", str(temp))
        cur_tweet = re.split(r"\s", cur_tweet)
        for word in cur_tweet:
            word=word.upper()
            if word == "AMERICA" or word == "US" or word=="USA" or word=="UNITED STATES OF AMERICA":
                flagword = flagword + 1
    print("USA BY NARENDRA MODI: "+ str(flagword))

    # for donald trump
    tweets = api.user_timeline(screen_name="realDonaldTrump", count=200, tweet_mode="extended")
    for tweet_compare in tweets:
        fulltext = tweet_compare.full_text
        tmp = []
        tmp.append(fulltext)
        temp = tmp
        import re
        cur_tweet = re.sub(r"http\S+", "", str(temp))
        cur_tweet = re.split(r"\s", cur_tweet)
        for word in cur_tweet:
            word = word.upper()
            if word == "INDIA":
                flagword1 = flagword1 + 1
    print("INDIA BY DONALD TRUMP: " + str(flagword1))


def display_menu():
    print('''select the option you want to perform :
    1.)To retrieve Tweets
    2.)To count the followers
    3.)To update status
    4.)To determine sentiments
    5.)To find location,time zone and language  of tweet
    6.)To determine top usage 
    7.) To compare two tweets
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

    elif (option==4):
        sentiments()
        display_menu()

    elif (option==5):
        tweet_location()
        display_menu()

    elif (option==6):
        stwords()
        display_menu()

    elif (option== 7):
        compare()
        display_menu()

    else:
        print("please enter a valid option ")

display_menu()

