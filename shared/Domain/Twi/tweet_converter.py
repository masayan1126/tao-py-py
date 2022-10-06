from shared.Domain.Twi.tweet import Tweet
from shared.Util.dict_util import DictUtil
from tweepy.models import Status


class TweetConverter:
    def convert(self, status: Status) -> Tweet:
        media_list = []
        is_contain_media = False

        if "extended_entities" not in status._json:

            tweet = Tweet(
                status.id,
                status.text,
                is_contain_media,
                media_list,
            )

            return tweet

        # TODO: 画像・動画

        if hasattr(status.extended_entities, "media"):

            is_contain_media = True

        # for media in status.extended_entities["media"]:

        #     if media["type"] == "photo":
        #         media_list.append(
        #             {
        #                 "id": media["id"],
        #                 "url": media["media_url_https"],
        #                 "type": media["type"],
        #             }
        #         )
        #     elif media["type"] == "video":
        #         # 最もビットレーどが高い動画urlを使用する
        #         # FIXME:videoは1ツイートに1つの前提
        #         highest = DictUtil.highest(
        #             status.extended_entities["media"][0]["video_info"]["variants"],
        #             "bitrate",
        #             0,
        #         )

        #         media_list.append(
        #             {
        #                 "id": media["id"],
        #                 "url": highest["url"],
        #                 "type": media["type"],
        #             }
        #         )

        tweet = Tweet(
            status.id,
            status.text,
            is_contain_media,
            media_list,
        )

        return tweet
