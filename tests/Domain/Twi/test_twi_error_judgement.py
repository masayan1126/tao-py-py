import unittest.mock
from urllib import response
import pytest
from packages.twi_automation.Domain.twi_error_handle_judgement import (
    TwiErrorHandleJudgement,
)
from packages.twi_automation.env import ENV
from shared.Domain.Time.x_date_time import XDateTime

from shared.Domain.Twi.twitter_operator import TwitterOperator
from shared.Domain.xstr import XStr
import tweepy
from tweepy import errors
from requests import Response


def test_ツイート_認証エラー() -> None:
    response = Response()
    response.status_code = [401]
    e = errors.Unauthorized(response)

    # e: errors.TweepyException = errors.TweepyException()
    e.api_codes.append(32)

    judgement = TwiErrorHandleJudgement(e)
    log_msg = judgement.judge()

    assert (
        log_msg
        == "Twitter API authentication failed (https://developer.twitter.com/en/portal/dashboard)"
    )
