from shared.Application.Youtube.youtube_video_download_usecase import (
    YoutubeVideoDownloadUsecase,
)
from shared.Domain.FileSystem.x_file_system_path import XFileSystemPath
from shared.Domain.String.xstr import XStr

download_path_to = XFileSystemPath(XStr("packages/clipping_yt/videos"))
options = {"outtmpl": download_path_to.of_text()}

video_id = "vudjymfhl3A"  # TODO: CSVから読み込む

YoutubeVideoDownloadUsecase().download(video_id=video_id, options=options)
