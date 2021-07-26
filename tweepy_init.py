import tweepy
import time
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


consumer_key = '#'
consumer_secret = '#'
access_token = '#'
access_token_secret = '#'


auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True,
    wait_on_rate_limit_notify=True)

api = tweepy.API(auth)

print("Py Script made by @snowy")

time.sleep(5)

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")

time.sleep(5)


recipient_id = '766461993901551616'

text = "hi im a bot"

direct_message = api.send_direct_message(recipient_id, text)
print(direct_message.message_create['message_data']['text'])


user = api.get_user("Johnas_07")

print("User details:")
print(user.name)
print(user.description)  
print(user.location)

print("Last 20 Followers:")
for follower in user.followers():
    print(follower.name)
    time.sleep(1)


hashtag = "#"
tweetNumber = "#"


tweets = tweepy.Cursor(api.search, hashtag).items(tweetNumber)

def searchBot():
    for tweet in tweets:
        try:
            tweet.retweet()
            print("retweet done!")
            time.sleep(10)
            tweet.like()
        except tweepy.TweepError as e:
            print(e.reason)
            time.sleep(10)


screen_name = "#"

count = 3
statuses = api.user_timeline(screen_name, count = count) 
for status in statuses:
    print(status.text, end = "\n\n")


time.sleep(1)


screen_name ="#"
perform_block = False
    
api.report_spam(screen_name = screen_name, perform_block = perform_block)

time.sleep(5)


print("script has run succsessfully")
print("if you want to run this Script again restart your terminal to reRun it")
print("Credits to @x8 snowy --YT")