from dataclasses import dataclass
from shared.judgement import Judgement
from tweepy import errors


@dataclass
class TwiErrorJudgement(Judgement):
    e: errors.TweepyException

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
