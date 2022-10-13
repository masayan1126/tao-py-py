from shared.Application.Youtube.youtube_transcript_build_usecase import (
    YoutubeTranscriptBuildUsecase,
)
from shared.Domain.FileSystem.x_file_system_path import XFileSystemPath
from shared.Domain.String.xstr import XStr
from shared.Youtube.i_yt_transcript_downloader import IYtTranscriptDownloader
from shared.Youtube.yt_transcript_downloader import YtTranscriptDownloader

downloader: IYtTranscriptDownloader = YtTranscriptDownloader()
yt_transcript_list = downloader.download(video_id="0vC3Tc7VDrE")

usecase = YoutubeTranscriptBuildUsecase(yt_transcript_list)
usecase.to_csv(
    XFileSystemPath(XStr("packages/clipping_yt/csv/transcripts.csv")).to_absolute()
)
