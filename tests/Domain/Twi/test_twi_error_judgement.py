from shared.Domain.Twi.twi_error_judgement import (
    TwiErrorJudgement,
)
from tweepy import errors
from requests import Response


def test_ツイート_認証エラー() -> None:
    response = Response()
    response.status_code = [401]

    e = errors.Unauthorized(response)
    e.api_codes.append(32)

    judgement = TwiErrorJudgement(e)
    log_msg = judgement.judge()

    assert (
        log_msg
        == "Twitter API authentication failed (https://developer.twitter.com/en/portal/dashboard)"
    )
