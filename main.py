from dotenv import load_dotenv
import os
from twitter_bot import TwitterBot

def main():
    load_dotenv()
    
    api_key = os.getenv('API_KEY')
    api_secret_key = os.getenv('API_SECRET_KEY')
    access_token = os.getenv('ACCESS_TOKEN')
    access_token_secret = os.getenv('ACCESS_TOKEN_SECRET')

    openai_api_key = os.getenv('OPENAI_API_KEY')

    bot = TwitterBot(api_key, api_secret_key, access_token, access_token_secret, openai_api_key)

    # Generate tweet content
    prompt = "Imagine you're a wise sage with knowledge spanning the universe. Share a profound or quirky fact about anything."
    tweet_content = bot.generate_content(prompt)
    
    # Post the generated content
    if tweet_content:
        bot.post_tweet(tweet_content)
        print("Tweet posted successfully.")
    else:
        print("Failed to generate content.")

if __name__ == "__main__":
    main()