from __future__ import annotations
from dataclasses import dataclass
from typing import Callable, List
from shared.Youtube.yt_transcript import YtTranscript
from youtube_transcript_api import YouTubeTranscriptApi


@dataclass
class YtTranscriptList:
    yt_transcript_list: list[YtTranscript]

    def __init__(self, video_id: str):
        self.yt_transcript_list = []
        transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)

        for transcript in transcript_list:
            for script in transcript.fetch():
                self.add(
                    YtTranscript(
                        video_id, script["text"], script["start"], script["duration"]
                    )
                )

    def all(self) -> list[YtTranscript]:
        return self.yt_transcript_list

    def add(self, yt_transcript: YtTranscript) -> YtTranscriptList:
        self.yt_transcript_list.append(yt_transcript)
        return self

    def count(self) -> int:
        return len(self.yt_transcript_list)

    def map(self, callable: Callable) -> YtTranscriptList:
        list(map(lambda yt_transcript: callable(yt_transcript), self.all()))
        return self

    def is_empty(self) -> bool:
        return self.count() == 0

    def first(self) -> YtTranscript:
        try:
            return self.all()[0]
        except IndexError:

            raise IndexError
