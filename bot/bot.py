import tweepy
import json
import os
import logging
from stream.autoretweetstreamlistener import AutoRetweetStreamListener
from http.client import IncompleteRead
from urllib3.exceptions import ProtocolError


def run_auth():
    # Go to auth dir to get credentials
    script_dir = os.path.dirname(__file__)
    auth_path = os.path.join(script_dir, "../auth/credentials.json")

    # Load JSON
    try:
        with open(auth_path) as f:
            data = json.load(f)
    except FileNotFoundError:
        logging.error('File ' + auth_path + ' does not exist')
        os.sys.exit()

    # Set keys
    consumer_key = data['consumer_key']
    consumer_secret = data['consumer_secret']
    access_token = data['access_token']
    access_token_secret = data['access_token_secret']

    # Authorize
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    try:
        api = tweepy.API(auth)
        return api
    except:
        logging.error('unable to authorize API')
        os.sys.exit()


def listen_to_streams(api):
    # Go to data dir to get filters.
    script_dir = os.path.dirname(__file__)
    filter_path = os.path.join(script_dir, "../data/filters.json")

    # Load JSON
    try:
        with open(filter_path) as f:
            data = json.load(f)
    except FileNotFoundError:
        logging.error('File ' + filter_path + ' does not exist')
        os.sys.exit()

    # Set keys
    user_ids = data["users"]

    # Listen
    stream_listener = AutoRetweetStreamListener(api, user_ids)

    while True:
        try:
            my_stream = tweepy.Stream(auth=api.auth, listener=stream_listener)
            logging.warning('stream started/restarted')
            my_stream.filter(follow=user_ids)
        except ProtocolError:
            logging.error('Protocol error. Restarting stream...')
            continue
        except IncompleteRead:
            logging.error('Incomplete Read error. Restarting stream...')
            continue
        except KeyboardInterrupt:
            my_stream.disconnect()
            break
    os.sys.exit()


def main():
    # Go to data dir to get settings.
    script_dir = os.path.dirname(__file__)
    settings_path = os.path.join(script_dir, "../data/settings.json")

    # Load JSON
    try:
        with open(settings_path) as f:
            data = json.load(f)
    except FileNotFoundError:
        logging.error('File ' + settings_path + ' does not exist')
        os.sys.exit()

    log_level_json = data["log_level"]
    if log_level_json is not None:
        log_level_string = log_level_json.lower().strip()
    
    log_level = logging.ERROR
    if log_level_string == 'warning':
        log_level = logging.WARNING
    elif log_level_string == 'info':
        log_level = logging.INFO        

    log_path = os.path.join(os.path.dirname(__file__), '../log.txt')
    logging.basicConfig(filename=log_path, format='%(asctime)s %(levelname)s: %(message)s',
                        datefmt='%d-%m-%Y %I:%M:%S %p', level=log_level)
    api = run_auth()
    logging.warning('api authenticated')
    listen_to_streams(api)


if __name__ == "__main__":
    main()
