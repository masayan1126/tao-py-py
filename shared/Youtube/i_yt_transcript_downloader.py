from __future__ import annotations
import abc

from shared.Youtube.yt_transcript_list import YtTranscriptList


class IYtTranscriptDownloader:
    @abc.abstractmethod
    def download(self, video_id: str) -> YtTranscriptList:
        pass
