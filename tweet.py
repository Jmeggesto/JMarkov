from twython import Twython 

APP_KEY = 'a'
APP_SECRET = 'a'

twitter = Twython(APP_KEY, APP_SECRET)

auth = twitter.get_authentication_tokens()

ACCESS_TOKEN = "a"
ACCESS_TOKEN_SECRET = "a"

twitter = Twython(APP_KEY, APP_SECRET,
                  ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

twitter.update_status(status='See how easy using Twython is!')