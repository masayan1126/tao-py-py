# from pandas import DataFrame
# from shared.Core.Log.log_handler import LogHandler
# from shared.Core.Log.log_type import LogType
# from shared.Domain.Twi.twi_error_judgement import (
#     TwiErrorJudgement,
# )
# from packages.twi_automation.env import ENV
# from shared.Domain.Converter.data_frame_converter import DataFrameConverter

# from shared.Domain.Excel.xcsv import XCsv
# from shared.Domain.FileSystem.x_file_system_path import XFileSystemPath
# from shared.Domain.String.xstr import XStr
# from shared.Domain.Twi.twitter_operator_factory import TwitterOperatorFactory
# from shared.Domain.Twi.twitter_operator_factory_option import (
#     TwitterOperatorFactoryOption,
# )
# from tweepy import errors

# # 毎日30分おきにランダムで1記事をツイート(csvのリストから取得)

# posts_df: DataFrame = XCsv().read(
#     XFileSystemPath(XStr("packages/twi_automation/posts.csv")),
#     encoding="UTF-8",
#     header=0,
# )

# posts = DataFrameConverter.to_list(posts_df)

# randomizer = NumberRandomizer()
# random_numbers = randomizer.generate(0, len(posts), 1)

# factory_option = TwitterOperatorFactoryOption(ENV["MY_SCREEN_NAME"], ENV["BLACK_LIST"])
# operator = TwitterOperatorFactory().create(factory_option)

# for random_number in random_numbers:
#     selected_post = posts[random_number]
#     title = selected_post["title"]
#     link = selected_post["link"]
#     tweet_content = XStr(f"{title}" "\n\n" f"{link}")
#     try:
#         operator.do_tweet(tweet_content)

#         LogHandler(
#             LogType.NOTIFICATION,
#             "Tweet was successful" "\n\n" f"{tweet_content.value()}",
#             ENV["PACKAGE_NAME"],
#         ).to_slack(ENV["SLACK_WEBHOOK_URL_TWITTER_AUTOMATION"])

#     except (errors.TweepyException) as e:
#         judgement = TwiErrorJudgement(e)
#         log_msg = judgement.judge()

#         LogHandler(
#             LogType.EXCEPTION,
#             log_msg,
#             ENV["PACKAGE_NAME"],
#         ).to_slack(ENV["SLACK_WEBHOOK_URL_TWITTER_AUTOMATION"])
