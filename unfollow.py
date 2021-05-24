#! /usr/bin/env python

# how to unfollow everyone who isn't following you
# By Jamieson Becker (Public Domain/no copyright, do what you will)


# Easy instructions even if you don't know Python
#
# 1.  remember to pip or easy_install tweepy
#
# 2.  edit the script below and plug in your keys. Don't leave
#     whitespace (i.e., spaces) at beginning or end of any keys
#
# 3.  you need to create a new app in your account at dev.twitter.com
#     and then plug in the new consumer and app keys below.
#
# 4.  the app needs to be set to read-write, but apps are read-only
#     by default. that's all there is to it.
# 
# 5.  Execute this script by either python unfollow.py OR
#     chmod +x unfollow.py and then execute it: ./unfollow.py

import time
import tweepy
import sys

CONSUMER_KEY = 'XUAGz64NEy6deSYf4eOrTEXs0' #environ['CONSUMER_KEY']
CONSUMER_SECRET = 'ujFaK0wnEQ8WWq7d4BH6A9WWYB4ORPynWDGHAnvYFCI5boxN9J' # environ['CONSUMER_SECRET']
ACCESS_KEY = '1356366441612599297-JTOlqpQIGIKJkI3UpP5jGEGiR9YNFc' # environ['ACCESS_KEY']
ACCESS_SECRET = '5ql6FmYG6YIq9qe94PvRUO66sbKrD93jaKZcJWkxXJPrb' # environ['ACCESS_SECRET']


auth = tweepy.auth.OAuthHandler(
        consumer_key=CONSUMER_KEY,
        consumer_secret=CONSUMER_SECRET)
auth.set_access_token(
        ACCESS_KEY,
        ACCESS_SECRET)

# the following dictionaries etc aren't strictly needed for this
# but useful for your own more in-depth apps.

api=tweepy.API(auth_handler=auth)

print("Loading followers..")
followers = []
for follower in tweepy.Cursor(api.followers).items():
    followers.append(follower)

print("Found %s followers, finding friends.." %len(followers))
friends = []
for friend in tweepy.Cursor(api.friends).items():
    friends.append(friend)

# creating dictionaries based on id's is handy too

friend_dict = {}
for friend in friends:
    friend_dict[friend.id] = friend

follower_dict = {}
for follower in followers:
    follower_dict[follower.id] = follower

# now we find all your "non_friends" - people who don't follow you
# even though you follow them.

non_friends = [friend for friend in friends if friend.id not in follower_dict]

# double check, since this could be a rather traumatic operation.

print("Unfollowing %s non-following users.." % len(non_friends))
print("This will take approximately %s minutes." % (len(non_friends)/60.0))
answer = raw_input("Are you sure? [Y/n]").lower()
if answer and answer[0] != "y":
    sys.exit(1)

for nf in non_friends:
    print("Unfollowing " + str(nf.id).rjust(10))
    try:
        nf.unfollow()
    except:
        print("  .. failed, sleeping for 5 seconds and then trying again.")
        time.sleep(5)
        nf.unfollow()
    print(" .. completed, sleeping for 1 second.")
    time.sleep(1)