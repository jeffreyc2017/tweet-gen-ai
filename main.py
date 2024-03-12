from dotenv import load_dotenv
import os
from twitter_bot import TwitterBot

def main():
    load_dotenv()
    
    api_key = os.getenv('API_KEY')
    api_secret_key = os.getenv('API_SECRET_KEY')
    access_token = os.getenv('ACCESS_TOKEN')
    access_token_secret = os.getenv('ACCESS_TOKEN_SECRET')

    bot = TwitterBot(api_key, api_secret_key, access_token, access_token_secret)
    
    content = "Hello world, this is a test tweet from TweetGenAI!"
    bot.post_tweet(content)
    print("Tweet posted successfully.")

if __name__ == "__main__":
    main()