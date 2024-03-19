import unittest
from unittest.mock import patch, MagicMock
from twitter_bot import TwitterBot


class TestTwitterBot(unittest.TestCase):
    @patch('tweepy.Client.create_tweet')
    def test_post_tweet(self, mock_create_tweet):
        # Initialize the bot with test credentials
        bot = TwitterBot("API key", "API secret key", "Access token", "Access token secret", "OpenAI API key")
        
        # Mock OpenAI response for content generation
        bot.openai_client = MagicMock()
        bot.openai_client.chat.completions.create(any).response = type('obj', (object,), {
            "choices": [type('obj', (object,), {"message": type('obj', (object,), {"content": "This is a test tweet from TweetGenAI's unittest."})})]
        })

        # Use the generate_content method to get tweet content
        generated_content = bot.generate_content("Give me a funny tweet about cats.")
        
        mock_create_tweet.response = "Done."
        # Attempt to post the tweet (the API call is mocked)
        bot.post_tweet(generated_content)
        
        # Assert that the openai create method was called with the correct parameters
        bot.openai_client.chat.completions.create().assert_not_called()
        
        # Assert that the create_tweet method was called once with the correct content
        mock_create_tweet.assert_called_once_with(text=generated_content)

if __name__ == '__main__':
    unittest.main()