import tweepy
from facebook import GraphAPI

# Twitter API credentials
twitter_api_key = "your_twitter_api_key"
twitter_api_secret_key = "your_twitter_api_secret_key"
twitter_access_token = "your_twitter_access_token"
twitter_access_token_secret = "your_twitter_access_token_secret"

# Facebook API credentials
facebook_access_token = "your_facebook_access_token"

def post_to_twitter(message):
    auth = tweepy.OAuth1UserHandler(twitter_api_key, twitter_api_secret_key, twitter_access_token, twitter_access_token_secret)
    api = tweepy.API(auth)
    api.update_status(message)

def post_to_facebook(message):
    graph = GraphAPI(access_token=facebook_access_token)
    graph.put_object(parent_object='me', connection_name='feed', message=message)

if __name__ == "__main__":
    campaign_message = "Join us in supporting the president's re-election campaign! #Vote2027"
    post_to_twitter(campaign_message)
    post_to_facebook(campaign_message)