from pandas import DataFrame
from packages.twi_automation.Domain.twi_error_handle_judgement_service import (
    TwiErrorHandleJudgementService,
)
from packages.twi_automation.env import ENV
from shared.Domain.Converter.data_frame_converter import DataFrameConverter

from shared.Domain.Excel.xcsv import XCsv
from shared.Domain.Twi.twitter_operator import TwitterOperator
from shared.Domain.Number.number_randomizer import NumberRandomizer
from shared.Domain.FileSystem.x_file_system_path import XFileSystemPath
from shared.Domain.String.xstr import XStr
from shared.Domain.Log.x_logger import XLogger
import tweepy
from tweepy import errors

# 毎日30分おきにランダムで1記事をツイート(csvのリストから取得)

posts_df: DataFrame = XCsv().read(
    XFileSystemPath(XStr("packages/twi_automation/posts.csv")),
    encoding="UTF-8",
    header=0,
)

posts = DataFrameConverter.to_list(posts_df)

randomizer = NumberRandomizer()
random_numbers = randomizer.generate(0, len(posts), 1)

twitter_operator = TwitterOperator()

for random_number in random_numbers:
    selected_post = posts[random_number]
    title = selected_post["title"]
    link = selected_post["link"]
    tweet_content = XStr(f"{title}" "\n\n" f"{link}")
    try:
        twitter_operator.tweet(tweet_content)

        XLogger.notification_to_slack(
            ENV["SLACK_WEBHOOK_URL_TWITTER_AUTOMATION"],
            "Tweet was successful" "\n\n" f"{tweet_content.value()}",
        )
    except (errors.TweepyException) as e:
        judgement = TwiErrorHandleJudgementService(e)
        log_msg = judgement.judge()

        XLogger.exception_to_slack(
            ENV["SLACK_WEBHOOK_URL_TWITTER_AUTOMATION"],
            log_msg,
        )

print("debug")
