from twitter import *

DEFAULT_NO_HASH_TEXT = "NO_HASH_TAG"

class TwitterUtils:

    def __init__(self):

        self.api_key = ""
        self.api_sec = ""
        self.owner_id = ""

        self.access_token = ""
        self.secret_token = ""

        self.api = Twitter(auth=OAuth(self.access_token, self.secret_token,
                       self.api_key, self.api_sec))

    def get_tweets_by_user(self, user):
        """
        returns the tweets of a user
        """
        tweets = self.api.statuses.user_timeline(screen_name=user, count=150)
        return tweets

    def get_all_hash_tags_by_user(self, user):
        """
        @returns list of sets, each set contains the hashtags of a tweet.
        Tweets with no hashtags contains the item DEFAULT_NO_HASH_TEXT
        """
        tweets = self.get_tweets_by_user(user)
        whole_list_of_hash_tags = list()
        for tweet in tweets:
            hash_tags_for_tweet = list()
            hash_tags = tweet['entities']['hashtags']

            if len(hash_tags)==0:
                hash_tags_for_tweet.append(DEFAULT_NO_HASH_TEXT)

            for hash_tag in hash_tags:
                hash_tags_for_tweet.append(hash_tag['text'])

            whole_list_of_hash_tags.append(frozenset(hash_tags_for_tweet))

        return whole_list_of_hash_tags
