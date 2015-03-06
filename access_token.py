from twython import Twython
import config

def get_access_token():
    tw = Twython(config.CONSUMER_KEY, config.CONSUMER_SECRET, oauth_version = 2)
    access_token = tw.obtain_access_token()
    f = open('access_token.txt', 'w')
    f.write(access_token)
    f.close()
    print 'Access token successfully written to access_token.txt'

get_access_token()