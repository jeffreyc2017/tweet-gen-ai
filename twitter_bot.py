import tweepy

class TwitterBot:
    def __init__(self, api_key, api_secret_key, access_token, access_token_secret):
        self.client = tweepy.Client(
            consumer_key=api_key,
            consumer_secret=api_secret_key, 
            access_token=access_token,
            access_token_secret=access_token_secret,
            wait_on_rate_limit=True
        )

    def post_tweet(self, content):
        response = self.client.create_tweet(
            text=content
        )
        print(f"https://twitter.com/user/status/{response.data['id']}")

    def delete_tweet(self, id):
        response = self.client.delete_tweet(id=id)
        print(f"{response}")
