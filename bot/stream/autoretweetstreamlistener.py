import tweepy
import logging


class AutoRetweetStreamListener(tweepy.StreamListener):
    def __init__(self, api, user_ids):
        super().__init__()
        self.api = api
        self.user_ids = user_ids

    def on_status(self, status):
        if hasattr(status, "retweeted_status"):
            # Do not retweet retweets.
            logging.info('Ignored retweet from ' + status.user.screen_name)
            return

        if status.in_reply_to_status_id is not None:
            # Do not retweet replies
            logging.info('Ignored reply from ' + status.user.screen_name)
            return

        if status.user.id_str not in self.user_ids:
            # The user is not in the list of users to retweet.
            logging.info('Ignored tweet from ' + status.user.screen_name)
            return

        try:
            self.api.retweet(status.id)
            logging.info('Retweeted: ' + status.text + ' from user ' + status.user.screen_name)
        except tweepy.error.TweepError:
            logging.error('Failed to retweet: ' + status.text + ' from user ' + status.user.screen_name)

    def on_error(self, status_code):
        if status_code == 420:
            # returning False in on_error disconnects the stream
            logging.error('Status 420 received.')
            return False

        # returning non-False reconnects the stream, with backoff.
        return True
