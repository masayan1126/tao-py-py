from unittest.mock import MagicMock
from shared.Domain.Twi.twi_error_judgement import (
    TwiErrorJudgement,
)


def test_ツイート_認証エラー() -> None:
    response_mock = MagicMock()
    response_mock.status = 401
    http_exception_mock = MagicMock(response_mock)
    http_exception_mock.api_codes = [32]
    sut = TwiErrorJudgement(http_exception_mock)
    error_msg = sut.judge()

    assert (
        error_msg
        == "Twitter API authentication failed (https://developer.twitter.com/en/portal/dashboard)"
    )


def test_ツイート_リクエスト上限エラー() -> None:
    response_mock = MagicMock()
    response_mock.status = 429
    http_exception_mock = MagicMock(response_mock)
    http_exception_mock.api_codes = [88]
    sut = TwiErrorJudgement(http_exception_mock)
    error_msg = sut.judge()

    assert error_msg == "Twitter API Rate Limmit Error"
