from unittest.mock import MagicMock, patch
import pytest
from shared.Core.operator_type import OperatorType
from shared.Domain.String.xstr import XStr
from shared.Domain.Twi.tweet import Tweet
from shared.Domain.Twi.twitter_operator import TwitterOperator
from tweepy.errors import HTTPException, TweepyException


# モジュールをモックへ差し替えるように追加(Gitリポジトリに存在しないconfigなど)
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

# memo: テスト対象のクラスでconfigを使用しているので、mockした後にimportする必要あり
from shared.Domain.Twi.twitter_operator_impl import TwitterOperatorImpl
from shared.Core.operator_factory import OperatorFactory


@pytest.fixture
def sut() -> TwitterOperator:
    return OperatorFactory().create(OperatorType.TWI)


@patch.object(TwitterOperatorImpl, "twi")
def test_do_tweet(tweepy_api_mock, sut: TwitterOperator) -> None:

    tweet_content = XStr("dummy tweet content")
    status_mock = MagicMock(text=tweet_content.value())  # models.Status
    api_instance = tweepy_api_mock.return_value  # twiメソッドの返り値

    api_instance.update_status.return_value = (
        status_mock  # tweepy.api.APIのインスタンスはupdate_statusメソッドを持つ
    )

    expected = tweet_content.value()
    actual = sut.do_tweet(tweet_content).text()

    assert expected == actual


@patch.object(TwitterOperatorImpl, "twi")
def test_do_tweet_例外(tweepy_api_mock, sut: TwitterOperator) -> None:
    with pytest.raises(TweepyException):
        tweet_content = XStr("dummy tweet content")
        api_instance = tweepy_api_mock.return_value  # twiメソッドの返り値
        api_instance.update_status.side_effect = TweepyException("TweepyException !!")

        sut.do_tweet(tweet_content).text()


@patch.object(TwitterOperatorImpl, "twi")
def test_favorite(tweepy_api_mock, sut: TwitterOperator) -> None:
    api_instance = tweepy_api_mock.return_value  # twiメソッドの返り値

    tweets_mock = [
        MagicMock(user=MagicMock(screen_name="name1")),
        MagicMock(user=MagicMock(screen_name="name2")),
    ]

    api_instance.search_tweets.return_value = tweets_mock
    api_instance.create_favorite.return_value = MagicMock()

    expected = ["name1\n", "name2\n"]
    actual = sut.favorite(XStr("hashtag1"))

    assert expected == actual


@patch.object(TwitterOperatorImpl, "twi")
def test_favorite_例外(tweepy_api_mock, sut: TwitterOperator) -> None:
    with pytest.raises(TweepyException):
        api_instance = tweepy_api_mock.return_value  # twiメソッドの返り値
        # tweepy_instance_mock = MagicMock()
        api_instance.search_tweets.side_effect = TweepyException("TweepyException !!")

        sut.favorite(XStr("hashtag2"))


@patch.object(TwitterOperatorImpl, "twi")
def test_follow(tweepy_api_mock, sut: TwitterOperator) -> None:

    api_instance = tweepy_api_mock.return_value  # twiメソッドの返り値

    tweets_mock = [
        MagicMock(user=MagicMock(screen_name="name1")),
        MagicMock(user=MagicMock(screen_name="name2")),
    ]

    api_instance.search_tweets.return_value = tweets_mock

    expected = (2, ["name1\n", "name2\n"])
    actual = sut.follow(XStr("hashtag3"))

    assert expected == actual


@patch.object(TwitterOperatorImpl, "twi")
def test_follow_例外(tweepy_api_mock, sut: TwitterOperator) -> None:
    with pytest.raises(HTTPException):
        api_instance = tweepy_api_mock.return_value  # twiメソッドの返り値

        http_exception_mock = HTTPException(MagicMock(status_code=500))
        http_exception_mock.api_codes = [162, 283]
        api_instance.search_tweets.side_effect = http_exception_mock

        sut.follow(XStr("hashtag2"))


@patch.object(TwitterOperatorImpl, "twi")
def test_follow_例外_フォローいいね済み例外はスルー(tweepy_api_mock, sut: TwitterOperator) -> None:
    api_instance = tweepy_api_mock.return_value  # twiメソッドの返り値

    tweets_mock = [
        MagicMock(user=MagicMock(screen_name="name1")),
        MagicMock(user=MagicMock(screen_name="name2")),  # 2件目がフォローいいね済み例外
        MagicMock(user=MagicMock(screen_name="name3")),
    ]

    http_exception_mock = HTTPException(MagicMock(status_code=500))
    http_exception_mock.api_codes = [139]  # フォローいいね済み例外
    api_instance.search_tweets.return_value = tweets_mock
    api_instance.create_friendship.side_effect = [None, http_exception_mock, None]

    expected = (2, ["name1\n", "name2\n", "name3\n"])
    actual = sut.follow(XStr("hashtag3"))

    assert expected == actual
    assert (
        api_instance.create_friendship.call_count == 3
    )  # ループ途中でフォローいいね済み例外ででても。3回呼ばれる


@patch.object(TwitterOperatorImpl, "twi")
def test_unfollow(tweepy_api_mock, sut: TwitterOperator) -> None:

    follower_ids_mock = [
        1,
        3,
        4,
    ]
    friend_ids_mock = [
        2,
        7,
        6,
    ]
    api_instance = tweepy_api_mock.return_value
    api_instance.get_follower_ids.return_value = follower_ids_mock
    api_instance.get_friend_ids.return_value = friend_ids_mock

    api_instance.get_user.side_effect = [
        MagicMock(screen_name="name1"),
        MagicMock(screen_name="name2"),
        MagicMock(screen_name="name3"),
    ]

    expected = (3, ["name1", "name2", "name3"])
    actual = sut.unfollow(3)

    assert expected == actual


@patch.object(TwitterOperatorImpl, "twi")
def test_unfollow_例外(tweepy_api_mock, sut: TwitterOperator) -> None:
    with pytest.raises(TweepyException):

        follower_ids_mock = [
            1,
            3,
            4,
        ]
        friend_ids_mock = [
            2,
            7,
            6,
        ]
        api_instance = tweepy_api_mock.return_value
        api_instance.get_follower_ids.return_value = follower_ids_mock
        api_instance.get_friend_ids.return_value = friend_ids_mock

        http_exception_mock = HTTPException(MagicMock(status_code=500))
        api_instance.destroy_friendship.side_effect = [None, http_exception_mock, None]

        sut.unfollow(3)


@patch.object(TwitterOperatorImpl, "twi")
def test_fetch_timeline(tweepy_api_mock, sut: TwitterOperator) -> None:

    statuses_mock = [
        MagicMock(id=1, text="a"),
        MagicMock(id=2, text="b"),
        MagicMock(id=3, text="c"),
        MagicMock(id=4, text="d"),
        MagicMock(id=5, text="e"),
    ]
    api_instance = tweepy_api_mock.return_value
    api_instance.user_timeline.return_value = statuses_mock

    expected = [
        Tweet(1, "a"),
        Tweet(2, "b"),
        Tweet(3, "c"),
        Tweet(4, "d"),
        Tweet(5, "e"),
    ]
    actual = sut.fetch_timeline(XStr("screen name2"), 5)

    assert expected == actual


@patch.object(TwitterOperatorImpl, "twi")
def test_follower_ids_全フォロワーのIDをリストで取得できる(
    tweepy_api_mock, sut: TwitterOperator
) -> None:
    api_instance = tweepy_api_mock.return_value
    api_instance.get_follower_ids.return_value = [1, 2, 3, 4, 5]

    expected = [1, 2, 3, 4, 5]
    actual = sut.follower_ids("screen name1")

    assert expected == actual


@patch.object(TwitterOperatorImpl, "twi")
def test_follow_ids_フォローしている全ユーザーのIDをリストで取得できる(
    tweepy_api_mock, sut: TwitterOperator
) -> None:
    api_instance = tweepy_api_mock.return_value
    api_instance.get_friend_ids.return_value = [1, 2, 3, 4, 5]

    expected = [1, 2, 3, 4, 5]
    actual = sut.follow_ids("screen name1")

    assert expected == actual
