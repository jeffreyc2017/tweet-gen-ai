import tweepy

class TwitterBot:
    def __init__(self, api_key, api_secret_key, access_token, access_token_secret):
        auth = tweepy.OAuth1UserHandler(api_key, api_secret_key, access_token, access_token_secret)
        self.api = tweepy.API(auth)

    def post_tweet(self, content):
        self.api.update_status(content)
