from packages.twi_automation.Domain.twi_error_handle_judgement import (
    TwiErrorHandleJudgement,
)
from tweepy import errors
from requests import Response


def test_ツイート_認証エラー() -> None:
    response = Response()
    response.status_code = [401]

    e = errors.Unauthorized(response)
    e.api_codes.append(32)

    judgement = TwiErrorHandleJudgement(e)
    log_msg = judgement.judge()

    assert (
        log_msg
        == "Twitter API authentication failed (https://developer.twitter.com/en/portal/dashboard)"
    )
