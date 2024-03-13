import unittest
from unittest.mock import patch
from twitter_bot import TwitterBot

class TestTwitterBot(unittest.TestCase):
    @patch('tweepy.Client.create_tweet')
    def test_post_tweet(self, mock_create_tweet):
        # Initialize the bot with test credentials
        bot = TwitterBot("API key", "API secret key", "Access token", "Access token secret")
        
        # Attempt to post a tweet (the API call is mocked)
        tweet_content = "This is a test tweet from TweetGenAI's unittest."
        bot.post_tweet(tweet_content)
        
        # Assert that the create_tweet method was called once with the correct content
        mock_create_tweet.assert_called_once_with(text=tweet_content)
        print("Test passed. create_tweet method was called successfully.")

if __name__ == '__main__':
    unittest.main()