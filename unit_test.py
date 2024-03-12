import unittest
from unittest.mock import patch
from twitter_bot import TwitterBot

class TestTwitterBot(unittest.TestCase):
    @patch('tweepy.API.update_status')
    def test_post_tweet(self, mock_update_status):
        # Initialize the bot with test credentials
        bot = TwitterBot("API key", "API secret key", "Access token", "Access token secret")
        
        # Attempt to post a tweet (the API call is mocked)
        bot.post_tweet("This is a test tweet from TweetGenAI's unittest.")
        
        # Assert that the update_status method was called once
        mock_update_status.assert_called_once_with("This is a test tweet from TweetGenAI's unittest.")
        print("Test passed. update_status method was called successfully.")

if __name__ == '__main__':
    unittest.main()