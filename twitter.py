from datetime import datetime
import json
from numpy import loads
import tweepy
import time
from os import environ
from moon.terminal_ui import TerminalUi
from moon.dialamoon import Moon


moon = Moon()
moon.set_moon_phase()
moon.save_to_disk('moon')


# KEYS

"""
CONSUMER_KEY = 'XUAGz64NEy6deSYf4eOrTEXs0' #environ['CONSUMER_KEY']
CONSUMER_SECRET = 'ujFaK0wnEQ8WWq7d4BH6A9WWYB4ORPynWDGHAnvYFCI5boxN9J' # environ['CONSUMER_SECRET']
ACCESS_KEY = '1356366441612599297-JTOlqpQIGIKJkI3UpP5jGEGiR9YNFc' # environ['ACCESS_KEY']
ACCESS_SECRET = '5ql6FmYG6YIq9qe94PvRUO66sbKrD93jaKZcJWkxXJPrb' # environ['ACCESS_SECRET']
"""

CONSUMER_KEY = environ['CONSUMER_KEY']
CONSUMER_SECRET = environ['CONSUMER_SECRET']
ACCESS_KEY = environ['ACCESS_KEY']
ACCESS_SECRET = environ['ACCESS_SECRET']

# AUTH

auth = tweepy.OAuthHandler(CONSUMER_KEY , CONSUMER_SECRET)

auth.set_access_token(ACCESS_KEY , ACCESS_SECRET)

# auth and set bot to sleep when reach the max twitter actions permitted

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

user = api.me()

# url image
img_url = "./moon.jpg"
phase = moon.moon_datetime_info['phase']
age = moon.moon_datetime_info['age']
diameter = moon.moon_datetime_info['diameter']
distance = moon.moon_datetime_info['distance']
earth_distance = round(distance/12742, 1)
message = 'Phase: '+ str(phase)+ '%' + '\nAge: '+ str(age) + ' days\nDiameter: '+ str(diameter) + ' arcseconds\nDistance: '+ str(distance) + ' km (' + str(earth_distance) + ' Earth diameters)'



# Main Loop
while True:
        api.update_with_media(img_url, status=message)
        time.sleep(60*60*24)
        