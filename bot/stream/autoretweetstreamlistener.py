import tweepy


class AutoRetweetStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        if hasattr(status, "retweeted_status"):
            print('it was a retweet')
            return

        # TODO: Retweet instead of print
        text = status.text
        print(text)

    def on_error(self, status_code):
        if status_code == 420:
            # returning False in on_error disconnects the stream
            return False

        # returning non-False reconnects the stream, with backoff.
        return True
