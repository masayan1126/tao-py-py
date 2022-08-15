from shared.Domain.FileSystem.x_file_system_path import XFileSystemPath
from shared.Domain.String.xstr import XStr
from shared.Youtube.yt_video_streamer import YtVideoStreamer


class ClipYoutubeVideoUsecase:
    def clip(self):

        yt_video_streamer = YtVideoStreamer(
            XFileSystemPath(
                XStr(
                    "【プロ野球 開幕戦】3_25 阪神タイガース VS 東京ヤクルトスワローズを一緒に観戦するライブ。【開幕戦2022】-V2SSVEmWGs8.mp4"
                )
            ),
            begin=9227.07,
            duration=50.64,
        )

        x_str = XStr("output.mp4")
        yt_video_streamer.output(XFileSystemPath(x_str))
