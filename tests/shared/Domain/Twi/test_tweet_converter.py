from unittest.mock import MagicMock, patch
import pytest
from shared.Domain.Twi.tweet import Tweet
from shared.Domain.Twi.tweet_converter import TweetConverter


@pytest.fixture
def sut() -> TweetConverter:
    return TweetConverter()


@patch("shared.Domain.Twi.tweet_converter.Status")
def test_convert(tweepy_status_mock, sut: TweetConverter) -> None:
    tweepy_status_mock.id = 1
    tweepy_status_mock.text = "text1"
    tweepy_status_mock._json = {
        "extended_entities": {"media": [{"id": 1575753595152367616}]}
    }

    expected = Tweet(1, "text1", True, [])  # TODO: 画像・動画
    actual = sut.convert(tweepy_status_mock)

    assert expected == actual


@patch("shared.Domain.Twi.tweet_converter.Status")
def test_convert_メディアなし(tweepy_status_mock, sut: TweetConverter) -> None:
    tweepy_status_mock.id = 2
    tweepy_status_mock.text = "text2"
    tweepy_status_mock._json = MagicMock()

    expected = Tweet(2, "text2", False, [])
    actual = sut.convert(tweepy_status_mock)

    assert expected == actual
