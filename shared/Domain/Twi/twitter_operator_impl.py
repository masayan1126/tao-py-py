from dataclasses import dataclass
from packages.twi_automation.env import ENV
from packages.twi_automation.config import CONFIG
from shared.Domain.Twi.twitter_operator import TwitterOperator
from shared.Domain.String.xstr import XStr
from shared.Domain.Twi.tweet import Tweet
from shared.Domain.Twi.tweet_converter import TweetConverter
import tweepy
from tweepy.api import API
from tweepy import errors
from tweepy.errors import HTTPException
from tweepy import models


@dataclass
class TwitterOperatorImpl(TwitterOperator):
    def __init__(self):

        CONSUMER_KEY = CONFIG["CONSUMER_KEY"]
        CONSUMER_SECRET = CONFIG["CONSUMER_SECRET"]
        ACCESS_TOKEN = CONFIG["ACCESS_TOKEN"]
        ACCESS_SECRET = CONFIG["ACCESS_SECRET"]

        auth = tweepy.OAuth1UserHandler(CONSUMER_KEY, CONSUMER_SECRET)
        auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
        _twi = API(auth)
        self._twi = _twi
        self._my_screen_name = ENV["MY_SCREEN_NAME"]
        self.black_list = ENV["BLACK_LIST"]

    def twi(self) -> API:
        return self._twi

    def do_tweet(self, tweet_content: XStr) -> Tweet:
        try:
            status: models.Status = self.twi().update_status(tweet_content.value())

            return TweetConverter().convert(status)
        except (errors.TweepyException) as e:
            raise e

    def favorite(self, hashtag: XStr) -> list[str]:
        favorited_user_screen_names: list[str] = []

        try:
            tweets = self.twi().search_tweets(q=hashtag.value(), count=50)

            for tweet in tweets:
                screen_name = f"{tweet.user.screen_name}" "\n"

                if screen_name not in self.black_list:
                    # スクリーンネーム(名前の下にある@以降の「英数字の組み合わせの箇所)
                    self.twi().create_favorite(tweet.id)
                    favorited_user_screen_names.append(screen_name)
            return favorited_user_screen_names
        except (errors.TweepyException) as e:
            raise e

    def follow(self, hashtag: XStr) -> tuple[int, list[str]]:
        tweets = self.twi().search_tweets(q=hashtag.value(), count=25)
        follow_count = 0
        followed_users = []
        for tweet in tweets:
            try:

                screen_name = tweet.user.screen_name
                followed_users.append(f"{screen_name}" "\n")

                # ブラックリストでもなく、自分自身でもない場合のみフォローしていいね
                if (
                    screen_name not in self.black_list
                    and screen_name != self.my_screen_name()
                ):
                    self.twi().create_friendship(screen_name=screen_name)
                    self.twi().create_favorite(tweet.id)
                    follow_count += 1
                    # 以下で、RateLimitError ⇨ TooManyRequestsになった模様
                    # https://github.com/tweepy/tweepy/commit/cd5f696d09530f86ac0edf1ec0fe0a02578a3920

            except (HTTPException) as e:

                # フォロー・イイね済み例外(139)は例外を投げて落とさなくてよい。そのユーザーへの処理をスキップするだけ

                if 139 not in e.api_codes:
                    raise e
                else:
                    continue
        return follow_count, followed_users

    # 参考
    # https://kia-tips.com/it/python/write-twitter-bot-python-tweepy-unfollow-non-followers#i-3
    def unfollow(self, max_unfollow_count: int = 100) -> tuple[int, list[str]]:
        total_unfollow_count = 0
        unfollowed_user_screen_names: list[str] = []

        try:
            follower_ids = self.follower_ids(self.my_screen_name())  # フォロワーリスト

            for friend_id in self.follow_ids(self.my_screen_name()):  # フォローリスト
                if total_unfollow_count > max_unfollow_count:
                    break

                # 相互フォローだったら
                if friend_id in follower_ids:
                    continue

                self.twi().destroy_friendship(user_id=friend_id)
                total_unfollow_count += 1
                unfollowed_user_screen_names.append(
                    self.twi().get_user(user_id=friend_id).screen_name
                )

            return total_unfollow_count, unfollowed_user_screen_names

        except (errors.TweepyException) as e:
            raise e

    def fetch_timeline(
        self, screen_name: XStr, count: int, since_id: int = None
    ) -> list[Tweet]:
        statuses: list[models.Status] = self.twi().user_timeline(
            screen_name=screen_name.value(),
            count=count,
            include_rts=False,
            exclude_replies=True,
            since_id=since_id,
        )

        tweets = []

        for status in statuses:
            tweets.append(TweetConverter().convert(status))

        return tweets

    def follower_ids(self, screen_name: str):
        return self.twi().get_follower_ids(screen_name=screen_name)

    def follow_ids(self, screen_name: str):
        return self.twi().get_friend_ids(screen_name=screen_name)

    def my_screen_name(self) -> str:
        return self._my_screen_name
