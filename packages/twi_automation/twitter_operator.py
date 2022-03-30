import datetime
from i_twitter_operator import ITwitterOperator
import tweepy

from config import CONFIG

from logging import DEBUG,  getLogger
import os
from slack_log_handler import SlackLogHandler


class TwitterOperator(ITwitterOperator):
    def __init__(self):
        CONSUMER_KEY = CONFIG["CONSUMER_KEY"]
        CONSUMER_SECRET = CONFIG["CONSUMER_SECRET"]
        ACCESS_TOKEN = CONFIG["ACCESS_TOKEN"]
        ACCESS_SECRET = CONFIG["ACCESS_SECRET"]

        auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
        self._twi = tweepy.API(auth)

    # FIXME: Xstrに変更する
    def tweet(self, tweet_content: str):
        try:
            # FIXME: XLoggerを使用する
            SLACK_WEBHOOK_URL = os.environ.get("SLACK_WEBHOOK_URL_TWITTER_AUTOMATION")
            handler = SlackLogHandler(SLACK_WEBHOOK_URL)
            handler.setLevel(DEBUG)
            logger = getLogger(__name__)
            logger.setLevel(DEBUG)
            logger.addHandler(handler)

            return self._twi.update_status(tweet_content)
        except tweepy.errors.TweepyException as e:

            if 32 in e.api_codes:
                logger.exception("認証に失敗しました。\n認証情報はこちらから確認できます(https://developer.twitter.com/en/portal/dashboard)")
            elif 187 in e.api_codes:
                logger.exception("重複するツイートが投稿されました。")
            else:
                logger.exception(e)

    def favorite(self, hashtag="#駆け出しエンジニアと繋がりたい -filter:retweets"):
        tweets = self._twi.search_tweets(q=hashtag, count=50)

        # FIXME: XLoggerを使用する
        SLACK_WEBHOOK_URL = os.environ.get("SLACK_WEBHOOK_URL_TWITTER_AUTOMATION")
        handler = SlackLogHandler(SLACK_WEBHOOK_URL)
        handler.setLevel(DEBUG)
        logger = getLogger(__name__)
        logger.setLevel(DEBUG)
        logger.addHandler(handler)

        for tweet in tweets:
            #スクリーンネーム(名前の下にある@以降の「英数字の組み合わせの箇所)
            screen_name = tweet.user.screen_name
            tweet_id = tweet.id

            # TODO: いい感じにする
            black_list = ["ahobot_unchi"]

            if screen_name not in black_list:
                try:
                    self._twi.create_favorite(tweet_id)
                    print('@' + screen_name + 'のいいねに成功しました')
                # 以下で、RateLimitError ⇨ TooManyRequestsになった模様
                # https://github.com/tweepy/tweepy/commit/cd5f696d09530f86ac0edf1ec0fe0a02578a3920
                except tweepy.errors.TooManyRequests as e:
                    logger.exception("【Twitter API Rate Limmit Error】@"f"{screen_name}のいいねに失敗しました")
                except tweepy.errors.TweepyException as e:
                    if 139 in e.api_codes:
                        logger.exception("すでにフォローまたはいいねがされているため、処理をキャンセルしました")
                    # elif 187 in e.api_codes:
                    #     logger.exception("重複するツイートが投稿されました。")
                    else:
                        logger.exception("【Tweepy Error】@"f"{screen_name}のいいねに失敗しました")

    def follow(self, hashtag: str = "#駆け出しエンジニアと繋がりたい -filter:retweets"):
        # FIXME: XStrを使う
        # 検索結果
        tweets = self._twi.search_tweets(q=hashtag, count=25)

        # FIXME: XLoggerを使用する
        SLACK_WEBHOOK_URL = os.environ.get("SLACK_WEBHOOK_URL_TWITTER_AUTOMATION")
        handler = SlackLogHandler(SLACK_WEBHOOK_URL)
        handler.setLevel(DEBUG)
        logger = getLogger(__name__)
        logger.setLevel(DEBUG)
        logger.addHandler(handler)

        for tweet in tweets:
            #スクリーンネーム(名前の下にある@以降の「英数字の組み合わせの箇所)
            screen_name = tweet.user.screen_name
            tweet_id = tweet.id

            black_list = ["ahobot_unchi"]

            if screen_name not in black_list:
                try:
                    # フォローしていいね
                    self._twi.create_friendship(screen_name=screen_name)
                    self._twi.create_favorite(tweet_id)
                    print('@' + screen_name + 'のフォローに成功しました')
                    # 以下で、RateLimitError ⇨ TooManyRequestsになった模様
                    # https://github.com/tweepy/tweepy/commit/cd5f696d09530f86ac0edf1ec0fe0a02578a3920
                except tweepy.errors.TooManyRequests as e:
                    logger.exception("【Twitter API Rate Limmit Error】@"f"{screen_name}のフォローに失敗しました")
                    logger.exception(e)
                except tweepy.errors.TweepyException as e:

                    if 139 in e.api_codes:
                        logger.exception("すでにフォローまたはいいねがされているため、処理をキャンセルしました")
                    # elif 187 in e.api_codes:
                    #     logger.exception("重複するツイートが投稿されました。")
                    else:
                        logger.exception("【Tweepy Error】@"f"{screen_name}のフォローに失敗しました")
            
            

        # フォロー制限
        # ・1日1,000人以上フォローした場合
        # ・1日250通以上のダイレクトメッセージを送信した場合
        # ・1時間あたり150 API リクエストを送信した場合
        # ・フォローの上限に達した場合（フォローする人が 2,001人になった場合）

        # 参考
        # https://myafu-python.com/twitter-follow/

    def unfollow(self, my_screen_name:str):

        # フォロワー
        follower_ids = self._twi.get_follower_ids(screen_name=my_screen_name)
        # フォロー
        follow_ids = self._twi.get_friend_ids(screen_name=my_screen_name)

        total_unfollow_count = 0
        for friend_id in follow_ids:
            # 相互フォローでなければ
            if friend_id not in follower_ids:
                if total_unfollow_count <= 100:
                    self._twi.destroy_friendship(user_id=friend_id)
                    print("{0}のフォローを解除しました。".format(self._twi.get_user(user_id=friend_id).screen_name))
                    total_unfollow_count += 1
                else:
                    print('一度にフォロー解除可能な人数(100人)に達したため処理を中断します。')
                    break

        # 参考
        # https://kia-tips.com/it/python/write-twitter-bot-python-tweepy-unfollow-non-followers#i-3
    
    def analyze(self, my_screen_name:str):

        # FIXME: XLoggerを使用する
        SLACK_WEBHOOK_URL = os.environ.get("SLACK_WEBHOOK_URL_TWITTER_AUTOMATION")
        handler = SlackLogHandler(SLACK_WEBHOOK_URL)
        handler.setLevel(DEBUG)
        logger = getLogger(__name__)
        logger.setLevel(DEBUG)
        logger.addHandler(handler)

        # フォロワー
        follower_ids = self._twi.get_follower_ids(screen_name=my_screen_name)
        # フォロー
        follow_ids = self._twi.get_friend_ids(screen_name=my_screen_name)


        try:
            f = open(file="/Users/nishigakimasaya/Desktop/twi/analytics.txt", mode='a', encoding="UTF-8")

            # if f.read() == "":
            #     XLogger.exceptionToSlack("対象のファイルがの中身が空です")
            #     XLogger.exception(f"対象のファイルがの中身が空です(ファイル名:{x_text.get_path()})")
            #     sys.exit()

            # print(f.read())
            # return f.read()

            t_delta = datetime.timedelta(hours=9)
            JST = datetime.timezone(t_delta, 'JST')
            now = datetime.datetime.now(JST)

            f.write(f"{now}/ フォロー数: {len(follow_ids)}/フォロワー数: {len(follower_ids)}""\n")

        except FileNotFoundError:
            logger.exception("対象のファイルが存在しないか、破損しています")
        finally:
            # 必ず閉じる。閉じていないファイルに再びアクセスしたら、ファイルが開きっぱなしなので開けない等になる
            # with文を使用すれば、自動で閉じてくれる
            if "f" in locals():
                f.close()


