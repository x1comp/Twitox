import tweepy
import time

consumer_key = '#'
consumer_secret = '#'


key = '#'
secret = '#'


auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 
auth.set_access_token(key, secret)

api = tweepy.API(auth, wait_on_rate_limit=True,
    wait_on_rate_limit_notify=True)

api = tweepy.API(auth)
try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")



def read_last_seen(FILE_NAME):
    file_read = open(FILE_NAME, 'r')
    last_seen_id = int(file_read.read().strip())
    file_read.close()
    return last_seen_id

def store_last_seen(FILE_NAME, last_seen_id):
    file_write = open(FILE_NAME, 'w')
    file_write.write(str(last_seen_id))
    file_write.close()
    return

tweets = api.mentions_timeline()
print (tweets[0])

for tweet in tweets:
    print(str(tweet.id) + '-' +tweet.text) 

time.sleep(5)

hashtag = "#ripfortnite"
tweetNumber = 10

tweets = tweepy.Cursor(api.search, hashtag).items(tweetNumber)

def searchBot():
    for tweet in tweets:
        try:
            tweet.retweet()
            print("retweet done!")
            time.sleep(10)
        except tweepy.TweepError as e:
            print(e.reason)
            time.sleep(10)
        

searchBot()
time.sleep(30)

user = api.get_user("#")

print("User details:")
print(user.name)
print(user.description)
print(user.location)

print("Last 20 Followers:")
for follower in user.followers():
    print(follower.name)
    time.sleep(20)
    

