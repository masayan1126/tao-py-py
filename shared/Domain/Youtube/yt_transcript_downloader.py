from dataclasses import dataclass
from shared.Youtube.yt_transcript import YtTranscript
from shared.Youtube.yt_transcript_list import YtTranscriptList
from youtube_transcript_api import YouTubeTranscriptApi
from shared.Youtube.i_yt_transcript_downloader import IYtTranscriptDownloader


@dataclass
class YtTranscriptDownloader(IYtTranscriptDownloader):
    def download(self, video_id: str) -> YtTranscriptList:
        yt_transcript_list = []

        for transcript in YouTubeTranscriptApi.list_transcripts(video_id):
            for script in transcript.fetch():
                yt_transcript_list.append(
                    YtTranscript(
                        video_id,
                        script["text"],
                        script["start"],
                        script["duration"],
                    )
                )

        return YtTranscriptList(yt_transcript_list)
