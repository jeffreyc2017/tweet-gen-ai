import tweepy
from openai import OpenAI

class TwitterBot:
    def __init__(self, api_key, api_secret_key, access_token, access_token_secret, openai_api_key, bearer_token=None):
        self.client = tweepy.Client(
            consumer_key=api_key,
            consumer_secret=api_secret_key,
            access_token=access_token,
            access_token_secret=access_token_secret,
            bearer_token=bearer_token,
            wait_on_rate_limit=True
        )

        self.openai_client = OpenAI(api_key=openai_api_key)

    def post_tweet(self, content):
        response = self.client.create_tweet(text=content)
        print(f"https://twitter.com/user/status/{response.data['id']}")
        print(f"Response: {response}")

    def generate_content(self, prompt):
        try:
            # Adding an instruction for the model to keep the output within 280 characters
            modified_prompt = f"{prompt} Write a tweet that is no more than 280 characters. Your response should only contains the tweet content and no other words."

            response = self.openai_client.chat.completions.create(
                model="gpt-3.5-turbo-0125",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": modified_prompt},
                ],
                temperature=0.7,  # Adjusting temperature for more varied outputs
            )

            print(response)

            content = response.choices[0].message.content
            print(content)

            # Additional check to ensure the content is within the limit
            return content if len(content) <= 280 else content[:277] + '...'
        except Exception as e:
            print(f"Error generating content: {e}")
            return ""

    def delete_tweet(self, id):
        response = self.client.delete_tweet(id=id)
        print(f"{response}")

    # According to this web page:
    # https://developer.twitter.com/en/docs/twitter-api/getting-started/about-twitter-api#v2-access-level
    # the free tier doesn't have access to search functions.
    def search_tweets(self, query, max_results=10):
        tweets = self.client.search_recent_tweets(query=query, max_results=max_results, user_auth=True)
        return tweets.data if tweets.data else []

    def reply_to_tweet(self, tweet_id, conversation_id, reply_text):
        response = self.client.create_tweet(text=reply_text, in_reply_to_tweet_id=tweet_id)
        if response.data:
            print(f"Replied to tweet: https://twitter.com/user/status/{response.data['id']}")
        else:
            print("Failed to post reply.")

    def read_and_reply(self, search_query):
        # Fetch a list of tweets based on the search query
        tweets = self.search_tweets(search_query, max_results=1)
        if tweets:
            selected_tweet = tweets[0]
            print(f"Selected Tweet: {selected_tweet.text}")
            
            # Generate a prompt for a reply
            prompt = f"How would you reply to this tweet? '{selected_tweet.text}'"
            reply_content = self.generate_content(prompt)
            
            # Post the reply
            if reply_content:
                self.reply_to_tweet(selected_tweet.id, selected_tweet.conversation_id, reply_content)
            else:
                print("No reply was generated.")
        else:
            print("No tweets found for the given query.")