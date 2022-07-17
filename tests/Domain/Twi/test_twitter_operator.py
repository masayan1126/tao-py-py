import unittest.mock
from requests import Response
import pytest
from requests import Response
from shared.Domain.Twi.tweet import Tweet
import tweepy
from tweepy import errors

# return_valueとside_effectが両方指定されていると、後者が優先


def test_tweet() -> None:

    tweepy_models_status = {
        "id": 1111111111111111111,
        "followers_count": 6172196,
        "friends_count": 12,
    }
    m = unittest.mock.MagicMock()
    m.tweet.return_value = tweepy_models_status

    acutual = m.tweet()
    expected = {
        "id": 1111111111111111111,
        "followers_count": 6172196,
        "friends_count": 12,
    }

    assert acutual == expected


def test_tweet_http例外() -> None:
    with pytest.raises(errors.TweepyException):
        m = unittest.mock.MagicMock()
        m.tweet.side_effect = errors.TweepyException(Response())

        m.tweet()


def test_fav() -> None:

    screen_name = "ふぁぼしたユーザーのスクリーンネーム"
    m = unittest.mock.MagicMock()
    m.favorite.return_value = screen_name

    acutual = m.favorite()
    expected = "ふぁぼしたユーザーのスクリーンネーム"

    assert acutual == expected


def test_fav_http例外() -> None:
    with pytest.raises(errors.TweepyException):
        m = unittest.mock.MagicMock()
        m.favorite.side_effect = errors.TweepyException(Response())

        m.favorite()


def test_follow() -> None:

    success_count = 10
    m = unittest.mock.MagicMock()
    m.follow.return_value = success_count

    acutual = m.follow()
    expected = 10

    assert acutual == expected


def test_follow_http例外() -> None:
    with pytest.raises(errors.TweepyException):
        m = unittest.mock.MagicMock()
        m.follow.side_effect = errors.TweepyException(Response())

        m.follow()


def test_unfollow() -> None:

    unfollowed_user_screen_names = [
        "unfollowed_user_screen_name1",
        "unfollowed_user_screen_name2",
    ]
    m = unittest.mock.MagicMock()
    m.unfollow.return_value = unfollowed_user_screen_names

    acutual = m.unfollow()
    expected = [
        "unfollowed_user_screen_name1",
        "unfollowed_user_screen_name2",
    ]

    assert acutual == expected


def test_unfollow_http例外() -> None:
    with pytest.raises(errors.TweepyException):
        m = unittest.mock.MagicMock()
        m.unfollow.side_effect = errors.TweepyException(Response())
        m.unfollow()


def test_fetch_timeline() -> None:
    tweet = Tweet(
        1,
        "ツイート内容",
        False,
        [],
    )

    m = unittest.mock.MagicMock()
    m.fetch_timeline.return_value = tweet

    acutual = m.fetch_timeline()
    expected = tweet

    assert acutual == expected


def test_analyze() -> None:

    word_count = 10
    m = unittest.mock.MagicMock()
    m.analyze.return_value = word_count

    acutual = m.analyze()
    expected = 10

    assert acutual == expected


def test_analyze_例外() -> None:
    with pytest.raises(FileNotFoundError):
        m = unittest.mock.MagicMock()
        m.analyze.side_effect = FileNotFoundError

        m.analyze()
