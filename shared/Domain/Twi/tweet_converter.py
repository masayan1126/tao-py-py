from typing import Dict

from shared.Domain.Twi.tweet import Tweet
from shared.Util.dict_util import DictUtil
from tweepy import models


class TweetConverter:
    def convert(self, status: models.Status) -> Dict:
        is_contain_media = False
        media_list = []

        # 画像・動画が含まれている
        is_contain_media = hasattr(status, "extended_entities")

        if is_contain_media:
            for media in status.extended_entities["media"]:

                if media["type"] == "photo":
                    media_list.append(
                        {
                            "id": media["id"],
                            "url": media["media_url_https"],
                            "type": media["type"],
                        }
                    )
                elif media["type"] == "video":
                    # 最もビットレーどが高い動画urlを使用する
                    # FIXME:videoは1ツイートに1つの前提
                    highest = DictUtil.highest(
                        status.extended_entities["media"][0]["video_info"]["variants"],
                        "bitrate",
                        0,
                    )

                    media_list.append(
                        {
                            "id": media["id"],
                            "url": highest["url"],
                            "type": media["type"],
                        }
                    )

        return Tweet(
            status.id,
            status.text,
            is_contain_media,
            media_list,
        )
