from shared.Application.Youtube.build_youtube_transcript_usecase import (
    BuildYoutubeTranscriptUsecase,
)
from shared.Domain.FileSystem.x_file_system_path import XFileSystemPath
from shared.Domain.String.xstr import XStr
from shared.Youtube.yt_transcript_list import YtTranscriptList


usecase = BuildYoutubeTranscriptUsecase(YtTranscriptList(video_id="0vC3Tc7VDrE"))
usecase.to_csv(
    XFileSystemPath(XStr("packages/clipping_yt/csv/transcripts.csv")).to_absolute()
)

print("debug")
