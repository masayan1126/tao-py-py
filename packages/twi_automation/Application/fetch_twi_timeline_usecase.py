from shared.Domain.Log.x_logger import XLogger
from shared.Domain.String.xstr import XStr
from packages.twi_automation.env import ENV
from shared.Domain.Twi.tweet import Tweet
from shared.Domain.Twi.twitter_operator import TwitterOperator


class FetchTwiTimelineUsecase:
    def fetch(
        self, screen_name: XStr, fetch_count: int, since_tweet_id: int = None
    ) -> list[Tweet]:

        try:
            twitter_operator = TwitterOperator()
            return twitter_operator.fetch_timeline(
                screen_name=screen_name, count=fetch_count, since_id=since_tweet_id
            )
        except Exception as e:
            XLogger.exception_to_slack(
                ENV["SLACK_WEBHOOK_URL_TWITTER_AUTOMATION"],
                e,
            )
            raise e
