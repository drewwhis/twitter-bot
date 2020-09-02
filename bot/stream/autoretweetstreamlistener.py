import tweepy


class AutoRetweetStreamListener(tweepy.StreamListener):
    def __init__(self, api, user_ids):
        super().__init__()
        self.api = api
        self.user_ids = user_ids

    def on_status(self, status):
        if hasattr(status, "retweeted_status"):
            # Do not retweet retweets.
            return

        if status.in_reply_to_status_id is not None:
            # Do not retweet replies
            return

        if status.user.id not in self.user_ids:
            # The user is not in the list of users to retweet.
            return

        try:
            self.api.retweet(status.id)
        except tweepy.error.TweepError:
            print(status.text, status.id)

    def on_error(self, status_code):
        if status_code == 420:
            # returning False in on_error disconnects the stream
            return False

        # returning non-False reconnects the stream, with backoff.
        return True
