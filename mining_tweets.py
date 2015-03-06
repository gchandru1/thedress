from twython import Twython
import config

def get_access_token():
    f = open('access_token.txt', 'r')
    return f.read()

ACCESS_TOKEN = get_access_token()
twitter = Twython(config.CONSUMER_KEY, access_token = ACCESS_TOKEN)


#get tweets for given query
def search_tweets():
    return twitter.search(q='thedress', result_type = 'popular')

print search_tweets()