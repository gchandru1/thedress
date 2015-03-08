from twython import Twython
import config
import json 
import csv

def get_access_token():
    f = open('access_token.txt', 'r')
    return f.read()

ACCESS_TOKEN = get_access_token()
twitter = Twython(config.CONSUMER_KEY, access_token = ACCESS_TOKEN)

def pretty_print(d):
    print json.dumps(d, indent = 4)
    

#get tweets for given query
def search_tweets(search_term, rtype):
    query = search_term + ' since:2015-02-26'
    results = twitter.search(q = query, result_type = rtype, lang = 'en', count = 100)
#   pretty_print(results)    
    return results.get('statuses')


def save_tweets():
    search_term = 'thedress OR blueandblack OR whiteandgold OR dressgate OR dressgate2015'
    tweets = search_tweets(search_term, 'mixed')
    # pretty_print(tweets[0])
    # text, id, favorite_count, retweeted, retweet_count, entities['hastags'][i]['text'], 
    # user['verified'], user['followers_count'], created_at , possibly_sensitive 
    with open('tweet_data.csv', 'w+') as csvfile:
        writer = csv.writer(csvfile)
        for t in tweets:
            hashtags = [tag['text'] for tag in t['entities']['hashtags']]
            text = t['text'].encode('ascii', 'ignore')
            csvdata = [text, t['id'], t['favorite_count'], t['retweeted'],
                       t['retweet_count'], t['user']['verified'], t['user']['followers_count'], 
                       t['created_at'] , t.get('possibly_sensitive'), '|'.join(hashtags)]
            writer.writerow(csvdata)
        
save_tweets()
