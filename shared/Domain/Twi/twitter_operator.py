from typing import List
from packages.twi_automation.config import CONFIG
from packages.twi_automation.env import ENV
from shared.Domain.Time.x_date_time import XDateTime
from shared.Domain.Twi.i_twitter_operator import ITwitterOperator
from shared.Domain.xstr import XStr
import tweepy
from tweepy import errors


class TwitterOperator(ITwitterOperator):
    def __init__(self):
        CONSUMER_KEY = CONFIG["CONSUMER_KEY"]
        CONSUMER_SECRET = CONFIG["CONSUMER_SECRET"]
        ACCESS_TOKEN = CONFIG["ACCESS_TOKEN"]
        ACCESS_SECRET = CONFIG["ACCESS_SECRET"]

        auth = tweepy.OAuth1UserHandler(CONSUMER_KEY, CONSUMER_SECRET)
        auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
        self._twi = tweepy.API(auth)
        self._my_screen_name = ENV["MY_SCREEN_NAME"]

    def tweet(self, tweet_content: XStr):
        try:
            return self._twi.update_status(tweet_content.get_string())
        except (errors.TweepyException) as e:
            raise e

    def favorite(self, hashtag: XStr):

        favorited_user_screen_names: List[str] = []

        try:
            tweets = self._twi.search_tweets(q=hashtag.get_string(), count=50)
            black_list = ENV["BLACK_LIST"]

            for tweet in tweets:

                screen_name = f"{tweet.user.screen_name}" "\n"

                if screen_name not in black_list:
                    # スクリーンネーム(名前の下にある@以降の「英数字の組み合わせの箇所)
                    self._twi.create_favorite(tweet.id)
                    favorited_user_screen_names.append(screen_name)

        except (errors.TweepyException) as e:
            raise e

        return favorited_user_screen_names

    def follow(self, hashtag: XStr):
        # 検索結果
        try:
            tweets = self._twi.search_tweets(q=hashtag.get_string(), count=25)
            success_count = 0
            black_list = ENV["BLACK_LIST"]

            for tweet in tweets:
                screen_name = tweet.user.screen_name

                # ブラックリストでもなく、自分自身でもない場合のみフォローしていいね
                if (
                    screen_name not in black_list
                    and screen_name != self.my_screen_name()
                ):
                    self._twi.create_friendship(screen_name=screen_name)
                    self._twi.create_favorite(tweet.id)
                    success_count += 1
                    # 以下で、RateLimitError ⇨ TooManyRequestsになった模様
                    # https://github.com/tweepy/tweepy/commit/cd5f696d09530f86ac0edf1ec0fe0a02578a3920
        except (errors.TweepyException) as e:
            raise e

        return success_count

    def unfollow(self):

        total_unfollow_count = 0
        unfollowed_user_screen_names: List[str] = []

        try:
            for friend_id in self.follow_ids():
                # 相互フォローでなければ
                if friend_id not in self.follower_ids():
                    if total_unfollow_count <= 100:
                        self._twi.destroy_friendship(user_id=friend_id)
                        total_unfollow_count += 1
                        unfollowed_user_screen_names.append(
                            self._twi.get_user(user_id=friend_id).screen_name
                        )
                    else:
                        break
        except (errors.TweepyException) as e:
            raise e

        return unfollowed_user_screen_names

        # 参考
        # https://kia-tips.com/it/python/write-twitter-bot-python-tweepy-unfollow-non-followers#i-3

    def analyze(self) -> str:
        # TODO: 前日比など

        now = XDateTime.now()
        return (
            f"{now.format('%Y/%m/%d %H:%M:%S')}/ フォロー数: {len(self.follow_ids())}/フォロワー数: {len(self.follower_ids())}"
            "\n"
        )

    def follower_ids(self):
        return self._twi.get_follower_ids(screen_name=self.my_screen_name())

    def follow_ids(self):
        return self._twi.get_friend_ids(screen_name=self.my_screen_name())

    def my_screen_name(self):
        return self._my_screen_name
