from shared.Application.Youtube.download_youtube_video_usecase import (
    DownloadYoutubeVideoUsecase,
)
from shared.Domain.FileSystem.x_file_system_path import XFileSystemPath
from shared.Domain.String.xstr import XStr

download_path_to = XFileSystemPath(XStr("packages/clipping_yt/videos"))
options = {"outtmpl": download_path_to.of_text()}

video_id = "0vC3Tc7VDrE"

DownloadYoutubeVideoUsecase().download(video_id=video_id, options=options)
