from dataclasses import dataclass
from shared.Core.Log.log_handler import LogHandler
from shared.Core.Log.log_type import LogType
from shared.Domain.Twi.twi_error_judgement import (
    TwiErrorJudgement,
)
from packages.twi_automation.env import ENV
from packages.twi_automation.Domain.regular_tweet_media_type import RegularTweetMediaType
from shared.Domain.Time.x_date_time import XDateTime
from shared.Domain.String.xstr import XStr
from shared.Domain.Twi.twitter_operator_factory import TwitterOperatorFactory
from shared.Domain.Twi.twitter_operator_factory_option import (
    TwitterOperatorFactoryOption,
)
from tweepy import errors
from shared.Domain.common.randomizer import Randomizer


@dataclass
class RegularTweetUseCase:

     def do_regular_tweet(
        self, mediaType: RegularTweetMediaType
    ) -> None:

        now = XDateTime.now()

        tweet_content = self._build_tweet_content(mediaType, now)

        factory_option = TwitterOperatorFactoryOption(
            ENV["MY_SCREEN_NAME"], ENV["BLACK_LIST"]
        )

        try:
            operator = TwitterOperatorFactory().create(factory_option)
            operator.do_tweet(tweet_content)

            LogHandler(
                LogType.NOTIFICATION,
                "Tweet was successful" "\n\n" f"content: {tweet_content.value()} mediaType: {mediaType}",
                ENV["PACKAGE_NAME"],
            ).to_slack(ENV["SLACK_WEBHOOK_URL_TWITTER_AUTOMATION"])

        except (errors.TweepyException) as e:

            judgement = TwiErrorJudgement(e)
            log_msg = judgement.judge()

            LogHandler(
                LogType.EXCEPTION,
                log_msg,
                ENV["PACKAGE_NAME"],
            ).to_slack(ENV["SLACK_WEBHOOK_URL_TWITTER_AUTOMATION"])

     def _build_tweet_content(self, mediaType: RegularTweetMediaType, now: XDateTime):
         if mediaType is RegularTweetMediaType.NOTE:
             tweet = ENV["REGULAR_TWEET"]["NOTE"] #現状、1つ
         elif mediaType is RegularTweetMediaType.YOUTUBE:
             index = Randomizer().gen_random_int(0, len(ENV["REGULAR_TWEET"]["YOUTUBE"]) - 1) #0～1
             tweet = ENV["REGULAR_TWEET"]["YOUTUBE"][index]
         else:
             tweet = ENV["REGULAR_TWEET"]["TECH_BLOG"]

         return XStr(f"{tweet}{now.format('%Y/%m/%d %H:%M:%S')}")