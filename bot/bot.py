import tweepy
import json
import os
from stream.autoretweetstreamlistener import AutoRetweetStreamListener


def run_auth():
    # Go to auth dir to get credentials
    script_dir = os.path.dirname(__file__)
    auth_path = os.path.join(script_dir, "../auth/credentials.json")

    # Load JSON
    try:
        with open(auth_path) as f:
            data = json.load(f)
    except FileNotFoundError:
        print('File', auth_path, 'does not exist')
        os.sys.exit()

    # Set keys
    consumer_key = data['consumer_key']
    consumer_secret = data['consumer_secret']
    access_token = data['access_token']
    access_token_secret = data['access_token_secret']

    # Authorize
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    return api


def listen_to_streams(api):
    # Go to data dir to get filters.
    script_dir = os.path.dirname(__file__)
    filter_path = os.path.join(script_dir, "../data/filters.json")

    # Load JSON
    try:
        with open(filter_path) as f:
            data = json.load(f)
    except FileNotFoundError:
        print('File', filter_path, 'does not exist')
        os.sys.exit()

    # Set keys
    user_ids = data["users"]

    # Listen
    stream_listener = AutoRetweetStreamListener(api)
    my_stream = tweepy.Stream(auth=api.auth, listener=stream_listener)
    my_stream.filter(follow=user_ids, is_async=True)


def main():
    api = run_auth()
    listen_to_streams(api)


if __name__ == "__main__":
    main()
