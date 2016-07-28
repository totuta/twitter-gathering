#! /usr/bin/python 
# -*- coding: utf-8 -*-

# filename: twitter-tracking.py 
# description: storing tweets about any keywords
# author: Wonchang Chung

import tweepy   # pip install tweepy : you might need virtualenv to use this package
import json


#################
# SEARCH OPTIONS
#################

# maximum number of tweets per searching
#   maximum rate for the Search API is 2,000tweets/15minutes
MAX_TWEETS = 2000

# set output file name
OUT_FILE = 'DIRECTORY/FILENAME'
# OUT_FILE = 'output/tweets.json'							# example

# set search query
#   refer to https://dev.twitter.com/rest/public/search 
QUERY = 'YOUR_QUERY_HERE'
# QUERY = '"Columbia University" OR "columbia university"'  # example 1
# QUERY = '"#DeepLearning" OR "#MachineLearning"'           # example 2


#################
# AUTHENTICATION
#################

# your authentication information
#   to obtain authentication info, go to https://apps.twitter.com/app/new
CONSUMER_KEY = 'YOUR_COSUMER_KEY_HERE'
CONSUMER_SECRET = 'YOUR_CONSUMER_SECRET_HERE'
ACCESS_KEY = 'YOUR_ACCESS_KEY_HERE'
ACCESS_SECRET = 'YOUR_ACCESS_SECRET_HERE'

# authentication process
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)


def main():

	# show running message
	print "-" * 20
	print "Searching tweets.."
	print "-" * 20

	# search them!
	searched_tweets = [status for status in tweepy.Cursor(api.search, q=QUERY).items(MAX_TWEETS)]
	# searched_tweets = [status for status in tweepy.Cursor(api.statuses_lookup, id="679827823700254721").items(MAX_TWEETS)]

	# storing in json format
	outFile = open(OUT_FILE,'a')

	# for a full map of tweet data, refer to http://mike.teczno.com/img/raffi-krikorian-map-of-a-tweet.png
	for i in range(0,len(searched_tweets)):

		json_temp = {}

		json_temp['id'] = searched_tweets[i].id
		json_temp['text'] = searched_tweets[i].text.encode("utf-8")
		json_temp['created_at'] = str(searched_tweets[i].created_at)
		json_temp['in_reply_to_user_id'] = searched_tweets[i].in_reply_to_user_id
		json_temp['geo'] = searched_tweets[i].geo
		json_temp['source'] = searched_tweets[i].source.encode("utf-8")

		json_temp['user'] = {}
		json_temp['user']['id'] = searched_tweets[i].user.id
		json_temp['user']['description'] = searched_tweets[i].user.description.encode("utf-8")
		json_temp['user']['location'] = searched_tweets[i].user.location.encode("utf-8")
		json_temp['user']['created_at'] = str(searched_tweets[i].user.created_at)
		json_temp['user']['favourites_count'] = searched_tweets[i].user.favourites_count
		json_temp['user']['friends_count'] = searched_tweets[i].user.friends_count
		json_temp['user']['time_zone'] = searched_tweets[i].user.time_zone
		json_temp['user']['utc_offset'] = searched_tweets[i].user.utc_offset
		json_temp['user']['followers_count'] = searched_tweets[i].user.followers_count
		json_temp['user']['geo_enabled'] = searched_tweets[i].user.geo_enabled

		outFile.write(json.dumps(json_temp, indent = 4))
		outFile.write(',\n')

	outFile.close()

	# how many tweets we've got?
	print "-" * 20
	print "Total %d tweets are tracked." % len(searched_tweets)
	print "-" * 20

if __name__ == "__main__": main()