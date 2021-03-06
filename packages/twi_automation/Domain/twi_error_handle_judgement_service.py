from shared.i_judgement import IJudgement
from tweepy import errors


class TwiErrorHandleJudgementService(IJudgement):
    def __init__(self, e: errors.TweepyException) -> None:
        self.e = e

    def judge(self) -> str:

        if 32 in self.e.api_codes:
            return "Twitter API authentication failed (https://developer.twitter.com/en/portal/dashboard)"
        # tweepy.errors.TooManyRequests: 429 Too Many Requests
        elif 88 in self.e.api_codes:
            return "Twitter API Rate Limmit Error"

        elif 161 in self.e.api_codes:
            return "Reached the maximum number of followers"

        elif 162 in self.e.api_codes:
            return "Canceled follow because of blocked user"

        elif 187 in self.e.api_codes:
            return "Duplicate tweets have been posted"

        elif 283 in self.e.api_codes:
            return "Received spam treatment"

        else:
            return "Failed"
