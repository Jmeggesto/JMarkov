from twython import Twython 
import json

APP_KEY = ""
APP_SECRET = ""
ACCESS_TOKEN = ""
ACCESS_TOKEN_SECRET = ""

with open("config.txt") as c:
        filecontents = c.read()

options = filecontents.split("\n")

APP_KEY = options[0]
APP_SECRET = options[1]
ACCESS_TOKEN = options[2]
ACCESS_TOKEN_SECRET = options[3]

twitter = Twython(APP_KEY, APP_SECRET)

twitter = Twython(APP_KEY, APP_SECRET,
                  ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

twitter.update_status(status='hello, world!')



