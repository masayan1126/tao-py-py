from unittest.mock import MagicMock, patch

# モジュールをモックへ差し替えるように追加
import sys

config_mock = MagicMock()
config_mock.CONFIG = {
    "CONSUMER_KEY": "CONSUMER_KEY1",
    "CONSUMER_SECRET": "CONSUMER_SECRET1",
    "ACCESS_TOKEN": "ACCESS_TOKEN1",
    "ACCESS_SECRET": "ACCESS_SECRET1",
}
sys.modules["packages.twi_automation.config"] = config_mock

env_mock = MagicMock()
env_mock.CONFIG = {
    "MY_SCREEN_NAME": "MY_SCREEN_NAME1",
    "REGULAR_TWEET": "REGULAR_TWEET1",
    "HASH_TAG": "HASH_TAG1",
    "SLACK_WEBHOOK_URL_TWITTER_AUTOMATION": "SLACK_WEBHOOK_URL_TWITTER_AUTOMATION1",
    "BLACK_LIST": [
        "BLACK_LIST1",
    ],
}
sys.modules["packages.twi_automation.env"] = env_mock

import pytest
from shared.Core.operator_factory import OperatorFactory
from shared.Core.operator_type import OperatorType
from shared.Domain.String.xstr import XStr
from shared.Domain.Twi.tweet import Tweet
from shared.Domain.Twi.twitter_operator import TwitterOperator
from shared.Domain.Twi.twitter_operator_impl import TwitterOperatorImpl
from tweepy.errors import HTTPException, TweepyException


@pytest.fixture
def sut() -> TwitterOperator:
    return OperatorFactory().create(OperatorType.TWI)


@patch.object(TwitterOperatorImpl, "twi")
def test_do_tweet(tweepy_api_mock, sut: TwitterOperator) -> None:

    tweet_content = XStr("dummy tweet content")
    status_response_mock = MagicMock(text=tweet_content.value())
    tweepy_instance_mock = MagicMock()
    tweepy_instance_mock.update_status.return_value = (
        status_response_mock  # tweepy.api.APIのインスタンスはupdate_statusメソッドを持つ
    )
    tweepy_api_mock.return_value = tweepy_instance_mock

    expected = tweet_content.value()
    actual = sut.do_tweet(tweet_content).text()

    assert expected == actual


# @patch.object(TwitterOperatorImpl, "twi")
# def test_do_tweet_例外(tweepy_api_mock, sut: TwitterOperator) -> None:
#     with pytest.raises(TweepyException):
#         tweet_content = XStr("dummy tweet content")

#         status_response_mock = MagicMock(
#             side_effect=TweepyException("TweepyException !!")
#         )
#         tweepy_instance_mock = MagicMock()
#         tweepy_instance_mock.update_status.side_effect = (
#             status_response_mock  # tweepy.api.APIのインスタンスはupdate_statusメソッドを持つ
#         )
#         tweepy_api_mock.return_value = tweepy_instance_mock

#         expected = tweet_content.value()
#         actual = sut.do_tweet(tweet_content).text()

#         assert expected == actual


# @patch.object(TwitterOperatorImpl, "twi")
# def test_favorite(tweepy_api_mock, sut: TwitterOperator) -> None:

#     search_results_mock = [
#         MagicMock(user=MagicMock(screen_name="name1")),
#         MagicMock(user=MagicMock(screen_name="name2")),
#     ]
#     tweepy_instance_mock = MagicMock()
#     tweepy_instance_mock.search_tweets.return_value = (
#         search_results_mock  # tweepy.api.APIのインスタンスはupdate_statusメソッドを持つ
#     )
#     tweepy_instance_mock.create_favorite.return_value = MagicMock()
#     tweepy_api_mock.return_value = tweepy_instance_mock

#     expected = ["name1\n", "name2\n"]
#     actual = sut.favorite(XStr("hashtag1"))

#     assert expected == actual


# @patch.object(TwitterOperatorImpl, "twi")
# def test_favorite_例外(tweepy_api_mock, sut: TwitterOperator) -> None:
#     with pytest.raises(TweepyException):
#         search_results_mock = MagicMock(
#             side_effect=TweepyException("TweepyException !!")
#         )
#         tweepy_instance_mock = MagicMock()
#         tweepy_instance_mock.search_tweets.side_effect = search_results_mock
#         tweepy_api_mock.return_value = tweepy_instance_mock

#         sut.favorite(XStr("hashtag2"))


# @patch.object(TwitterOperatorImpl, "twi")
# def test_follow(tweepy_api_mock, sut: TwitterOperator) -> None:

#     search_results_mock = [
#         MagicMock(user=MagicMock(screen_name="name1")),
#         MagicMock(user=MagicMock(screen_name="name2")),
#     ]
#     tweepy_instance_mock = MagicMock()
#     tweepy_instance_mock.search_tweets.return_value = (
#         search_results_mock  # tweepy.api.APIのインスタンスはupdate_statusメソッドを持つ
#     )
#     tweepy_instance_mock.create_follow.return_value = MagicMock()
#     tweepy_api_mock.return_value = tweepy_instance_mock

#     expected = (2, ["name1\n", "name2\n"])
#     actual = sut.follow(XStr("hashtag3"))

#     assert expected == actual


# @patch.object(TwitterOperatorImpl, "twi")
# def test_follow_例外(tweepy_api_mock, sut: TwitterOperator) -> None:
#     with pytest.raises(HTTPException):
#         tweepy_instance_mock = MagicMock()
#         http_exception_mock = HTTPException(MagicMock(status_code=500))
#         http_exception_mock.api_codes = [162, 283]
#         tweepy_instance_mock.search_tweets.side_effect = http_exception_mock

#         tweepy_api_mock.return_value = tweepy_instance_mock

#         sut.follow(XStr("hashtag2"))


# @patch.object(TwitterOperatorImpl, "twi")
# def test_follow_例外_フォローいいね済み例外はスルー(tweepy_api_mock, sut: TwitterOperator) -> None:
#     tweepy_instance_mock = MagicMock()
#     http_exception_mock = HTTPException(MagicMock(status_code=500))
#     http_exception_mock.api_codes = [139]  # フォローいいね済み例外
#     tweepy_instance_mock.search_tweets.side_effect = http_exception_mock
#     tweepy_api_mock.return_value = tweepy_instance_mock

#     sut.follow(XStr("hashtag2"))


# @patch.object(TwitterOperatorImpl, "twi")
# def test_unfollow(tweepy_api_mock, sut: TwitterOperator) -> None:

#     follower_ids_mock = [
#         1,
#         3,
#         4,
#     ]
#     friend_ids_mock = [
#         5,
#         6,
#         7,
#     ]
#     tweepy_instance_mock = MagicMock()
#     tweepy_instance_mock.get_follower_ids.return_value = follower_ids_mock
#     tweepy_instance_mock.get_friend_ids.return_value = friend_ids_mock
#     tweepy_instance_mock.destroy_friendship.return_value = MagicMock()
#     tweepy_instance_mock.get_user.side_effect = [
#         MagicMock(screen_name="name1"),
#         MagicMock(screen_name="name2"),
#         MagicMock(screen_name="name3"),
#     ]
#     tweepy_api_mock.return_value = tweepy_instance_mock

#     expected = (3, ["name1", "name2", "name3"])
#     actual = sut.unfollow(3)

#     assert expected == actual


# @patch.object(TwitterOperatorImpl, "twi")
# def test_unfollow_例外(tweepy_api_mock, sut: TwitterOperator) -> None:
#     with pytest.raises(TweepyException):

#         friend_ids_mock = [
#             5,
#             6,
#             7,
#         ]
#         tweepy_instance_mock = MagicMock()
#         tweepy_instance_mock.get_follower_ids.side_effect = TweepyException(
#             "TweepyException !!"
#         )
#         tweepy_instance_mock.get_friend_ids.return_value = friend_ids_mock
#         tweepy_instance_mock.destroy_friendship.return_value = MagicMock()
#         tweepy_instance_mock.get_user.side_effect = [
#             MagicMock(screen_name="name1"),
#             MagicMock(screen_name="name2"),
#             MagicMock(screen_name="name3"),
#         ]
#         tweepy_api_mock.return_value = tweepy_instance_mock

#         sut.unfollow(3)


# @patch.object(TwitterOperatorImpl, "twi")
# def test_fetch_timeline(tweepy_api_mock, sut: TwitterOperator) -> None:

#     statuses_mock = [
#         MagicMock(id=1, text="a"),
#         MagicMock(id=2, text="b"),
#         MagicMock(id=3, text="c"),
#         MagicMock(id=4, text="d"),
#         MagicMock(id=5, text="e"),
#     ]
#     tweepy_instance_mock = MagicMock()
#     tweepy_instance_mock.user_timeline.return_value = statuses_mock
#     tweepy_api_mock.return_value = tweepy_instance_mock

#     expected = [
#         Tweet(1, "a"),
#         Tweet(2, "b"),
#         Tweet(3, "c"),
#         Tweet(4, "d"),
#         Tweet(5, "e"),
#     ]
#     actual = sut.fetch_timeline(XStr("screen name2"), 1)

#     assert expected == actual


# @patch.object(TwitterOperatorImpl, "twi")
# def test_follower_ids_全フォロワーのIDをリストで取得できる(
#     tweepy_api_mock, sut: TwitterOperator
# ) -> None:
#     tweepy_instance_mock = MagicMock()
#     tweepy_instance_mock.get_follower_ids.return_value = [1, 2, 3, 4, 5]
#     tweepy_api_mock.return_value = tweepy_instance_mock

#     expected = [1, 2, 3, 4, 5]
#     actual = sut.follower_ids("screen name1")

#     assert expected == actual


# @patch.object(TwitterOperatorImpl, "twi")
# def test_follow_ids_フォローしている全ユーザーのIDをリストで取得できる(
#     tweepy_api_mock, sut: TwitterOperator
# ) -> None:
#     tweepy_instance_mock = MagicMock()
#     tweepy_instance_mock.get_friend_ids.return_value = [1, 2, 3, 4, 5]
#     tweepy_api_mock.return_value = tweepy_instance_mock

#     expected = [1, 2, 3, 4, 5]
#     actual = sut.follow_ids("screen name1")

#     assert expected == actual
