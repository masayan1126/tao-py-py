from unittest.mock import MagicMock, patch
import pytest
from shared.Domain.String.xstr import XStr
from shared.Domain.Twi.tweet import Tweet
from shared.Domain.Twi.twitter_operator import TwitterOperator
from shared.Domain.Twi.twitter_operator_factory_option import (
    TwitterOperatorFactoryOption,
)

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


# memo: テスト対象のクラスでconfigを使用しているので、mockした後にimportする必要あり
from shared.Domain.Twi.twitter_operator_factory import TwitterOperatorFactory


@pytest.fixture
def factory_option() -> TwitterOperatorFactoryOption:
    return TwitterOperatorFactoryOption(
        "screen_name1", ["black_list_user1", "black_list_user2"]
    )


def test_do_tweet(factory_option: TwitterOperatorFactoryOption) -> None:
    with patch("shared.Domain.Twi.twitter_operator_impl.API") as tweepy_api_mock:
        tweet_content = XStr("dummy tweet content")
        status_mock = MagicMock(text=tweet_content.value())  # models.Status
        api_instance = MagicMock()
        api_instance.update_status.return_value = (
            status_mock  # tweepy.api.APIのインスタンスはupdate_statusメソッドを持つ
        )

        tweepy_api_mock.return_value = api_instance  # APIメソッドの返り値

        sut = TwitterOperatorFactory().create(factory_option)

        expected = XStr("dummy tweet content").value()
        actual = sut.do_tweet(XStr("dummy tweet content")).text()

        assert expected == actual


@patch("shared.Domain.Twi.twitter_operator_impl.API")
def test_do_tweet_例外(
    tweepy_api_mock, factory_option: TwitterOperatorFactoryOption
) -> None:
    with pytest.raises(TweepyException):
        tweet_content = XStr("dummy tweet content")
        api_instance = tweepy_api_mock.return_value
        api_instance.update_status.side_effect = TweepyException("TweepyException !!")
        tweepy_api_mock.return_value = api_instance  # APIメソッドの返り値

        sut = TwitterOperatorFactory().create(factory_option)
        sut.do_tweet(tweet_content).text()


@patch("shared.Domain.Twi.twitter_operator_impl.API")
def test_favorite(
    tweepy_api_mock, factory_option: TwitterOperatorFactoryOption
) -> None:
    api_instance = tweepy_api_mock.return_value

    tweets_mock = [
        MagicMock(user=MagicMock(screen_name="name1")),
        MagicMock(user=MagicMock(screen_name="name2")),
    ]

    api_instance.search_tweets.return_value = tweets_mock
    api_instance.create_favorite.return_value = MagicMock()

    sut = TwitterOperatorFactory().create(factory_option)

    expected = ["name1\n", "name2\n"]
    actual = sut.favorite(XStr("hashtag1"))

    assert expected == actual


@patch("shared.Domain.Twi.twitter_operator_impl.API")
def test_favorite_例外(
    tweepy_api_mock, factory_option: TwitterOperatorFactoryOption
) -> None:
    with pytest.raises(TweepyException):
        api_instance = tweepy_api_mock.return_value
        # tweepy_instance_mock = MagicMock()
        api_instance.search_tweets.side_effect = TweepyException("TweepyException !!")

        sut = TwitterOperatorFactory().create(factory_option)

        sut.favorite(XStr("hashtag2"))


@patch("shared.Domain.Twi.twitter_operator_impl.API")
def test_follow(tweepy_api_mock, factory_option: TwitterOperatorFactoryOption) -> None:

    api_instance = tweepy_api_mock.return_value

    tweets_mock = [
        MagicMock(user=MagicMock(screen_name="name1")),
        MagicMock(user=MagicMock(screen_name="name2")),
    ]

    api_instance.search_tweets.return_value = tweets_mock

    sut = TwitterOperatorFactory().create(factory_option)

    expected = (2, ["name1\n", "name2\n"])
    actual = sut.follow(XStr("hashtag3"))

    assert expected == actual


@patch("shared.Domain.Twi.twitter_operator_impl.API")
def test_follow_例外(
    tweepy_api_mock, factory_option: TwitterOperatorFactoryOption
) -> None:
    with pytest.raises(HTTPException):
        api_instance = tweepy_api_mock.return_value

        http_exception_mock = HTTPException(MagicMock(status_code=500))
        http_exception_mock.api_codes = [162, 283]
        api_instance.search_tweets.side_effect = http_exception_mock

        sut = TwitterOperatorFactory().create(factory_option)
        sut.follow(XStr("hashtag2"))


@patch("shared.Domain.Twi.twitter_operator_impl.API")
def test_follow_例外_フォローいいね済み例外はスルー(
    tweepy_api_mock, factory_option: TwitterOperatorFactoryOption
) -> None:
    api_instance = tweepy_api_mock.return_value

    tweets_mock = [
        MagicMock(user=MagicMock(screen_name="name1")),
        MagicMock(user=MagicMock(screen_name="name2")),  # 2件目がフォローいいね済み例外
        MagicMock(user=MagicMock(screen_name="name3")),
    ]

    http_exception_mock = HTTPException(MagicMock(status_code=500))
    http_exception_mock.api_codes = [139]  # フォローいいね済み例外
    api_instance.search_tweets.return_value = tweets_mock
    api_instance.create_friendship.side_effect = [None, http_exception_mock, None]

    sut = TwitterOperatorFactory().create(factory_option)

    expected = (2, ["name1\n", "name2\n", "name3\n"])
    actual = sut.follow(XStr("hashtag3"))

    assert expected == actual
    assert (
        api_instance.create_friendship.call_count == 3
    )  # ループ途中でフォローいいね済み例外ででても。3回呼ばれる


@patch("shared.Domain.Twi.twitter_operator_impl.API")
def test_unfollow(
    tweepy_api_mock, factory_option: TwitterOperatorFactoryOption
) -> None:

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

    sut = TwitterOperatorFactory().create(factory_option)

    expected = (3, ["name1", "name2", "name3"])
    actual = sut.unfollow(3)

    assert expected == actual


@patch("shared.Domain.Twi.twitter_operator_impl.API")
def test_unfollow_例外(
    tweepy_api_mock, factory_option: TwitterOperatorFactoryOption
) -> None:
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

        sut = TwitterOperatorFactory().create(factory_option)
        sut.unfollow(3)


@patch("shared.Domain.Twi.twitter_operator_impl.API")
def test_fetch_timeline(
    tweepy_api_mock, factory_option: TwitterOperatorFactoryOption
) -> None:

    statuses_mock = [
        MagicMock(id=1, text="a"),
        MagicMock(id=2, text="b"),
        MagicMock(id=3, text="c"),
        MagicMock(id=4, text="d"),
        MagicMock(id=5, text="e"),
    ]
    api_instance = tweepy_api_mock.return_value
    api_instance.user_timeline.return_value = statuses_mock

    sut = TwitterOperatorFactory().create(factory_option)

    expected = [
        Tweet(1, "a"),
        Tweet(2, "b"),
        Tweet(3, "c"),
        Tweet(4, "d"),
        Tweet(5, "e"),
    ]
    actual = sut.fetch_timeline(XStr("screen name2"), 5)

    assert expected == actual


@patch("shared.Domain.Twi.twitter_operator_impl.API")
def test_follower_ids_全フォロワーのIDをリストで取得できる(
    tweepy_api_mock, factory_option: TwitterOperatorFactoryOption
) -> None:
    api_instance = tweepy_api_mock.return_value
    api_instance.get_follower_ids.return_value = [1, 2, 3, 4, 5]

    sut = TwitterOperatorFactory().create(factory_option)

    expected = [1, 2, 3, 4, 5]
    actual = sut.follower_ids("screen name1")

    assert expected == actual


@patch("shared.Domain.Twi.twitter_operator_impl.API")
def test_follow_ids_フォローしている全ユーザーのIDをリストで取得できる(
    tweepy_api_mock, factory_option: TwitterOperatorFactoryOption
) -> None:
    api_instance = tweepy_api_mock.return_value
    api_instance.get_friend_ids.return_value = [1, 2, 3, 4, 5]

    sut = TwitterOperatorFactory().create(factory_option)

    expected = [1, 2, 3, 4, 5]
    actual = sut.follow_ids("screen name1")

    assert expected == actual
