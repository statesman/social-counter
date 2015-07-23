import requests
import twitter as TwitterApi
from instagram.client import InstagramAPI
from ConfigParser import ConfigParser


# Get config from file
cfg = ConfigParser()
cfg.readfp(open('config.cfg'))


def log(account, prefix=""):
    """
    @account: str
    @prefix: str
    """
    print "Checking " + prefix + account


def facebook(account):
    """
    @account: str
    """
    log(account, "facebook.com/")
    r = requests.get('https://graph.facebook.com/' + account +
                     '?access_token=' + cfg.get('facebook', 'access_token'))
    if r.status_code == 200:
        return r.json()['likes']


def twitter(account):
    """
    @account: str
    """
    log(account, "@")
    api = TwitterApi.Api(
        consumer_key=cfg.get('twitter', 'consumer_key'),
        consumer_secret=cfg.get('twitter', 'consumer_secret'),
        access_token_key=cfg.get('twitter', 'access_token_key'),
        access_token_secret=cfg.get('twitter', 'access_token_secret')
    )
    twitter_account = api.GetUser(screen_name=account)
    return twitter_account.followers_count


def insta(account):
    """
    @account: str
    """
    log(account, "@")
    api = InstagramAPI(
        client_id=cfg.get('instagram', 'client_id'),
        client_secret=cfg.get('instagram', 'client_secret')
    )
    user = api.user_search(account)[0]
    found_user = api.user(user.id)
    return found_user.counts['followed_by']


def youtube(account):
    """
    @account: str
    """
    log(account, "youtube.com/")
    r = requests.get('http://gdata.youtube.com/feeds/api/users/' +
                     account + '?alt=json')
    return r.json()['entry']['yt$statistics']['subscriberCount']


def googleplus(account):
    """
    @account: str
    """
    log(account, "+")
    r = requests.get('https://www.googleapis.com/plus/v1/people/+' +
                     account + '?key=' + cfg.get('google_plus', 'api_key'))
    return r.json()['circledByCount']


def tumblr(blog_prefix):
    """
    @blog_prefix: str
    """
    log(blog_prefix)
    r = requests.get('http://api.tumblr.com/v2/blog/' + blog_prefix +
                     '.tumblr.com/info?api_key=' +
                     cfg.get('tumblr', 'oauth_consumer_key'))
    return r.json()['response']['blog']['likes']
