import tweepy
from openai import OpenAI

class TwitterBot:
    def __init__(self, api_key, api_secret_key, access_token, access_token_secret, openai_api_key):
        self.client = tweepy.Client(
            consumer_key=api_key,
            consumer_secret=api_secret_key,
            access_token=access_token,
            access_token_secret=access_token_secret,
            wait_on_rate_limit=True
        )

        self.openai_client = OpenAI(api_key=openai_api_key)

    def post_tweet(self, content):
        response = self.client.create_tweet(text=content)
        print(f"https://twitter.com/user/status/{response.data['id']}")
        print(f"{response}")

    def generate_content(self, prompt):
        try:
            # Adding an instruction for the model to keep the output within 280 characters
            modified_prompt = f"{prompt} Write a tweet that is no more than 280 characters. Your response should only contains the tweet content and no other words."

            # example with a system message
            response = self.openai_client.chat.completions.create(
                model="gpt-3.5-turbo-0125",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": modified_prompt},
                ],
                temperature=0,
            )

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