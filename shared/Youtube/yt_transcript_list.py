from __future__ import annotations
from dataclasses import dataclass
from typing import Callable
from shared.Domain.List.array_impl import ArrayImpl
from shared.Youtube.yt_transcript import YtTranscript


@dataclass
class YtTranscriptList(ArrayImpl):
    def __init__(self, yt_transcript_list: list[YtTranscript]):
        super().__init__(yt_transcript_list)

    def add(self, yt_transcript: YtTranscript) -> YtTranscriptList:
        super().add(yt_transcript)
        return self

    def map(self, callable: Callable) -> YtTranscriptList:

        super().map(callable)
        return self

    def first(self) -> YtTranscript:
        try:
            return super().first()
        except IndexError:

            raise IndexError
