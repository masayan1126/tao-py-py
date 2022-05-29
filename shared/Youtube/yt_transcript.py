from __future__ import annotations
from dataclasses import dataclass


@dataclass
class YtTranscript:
    _video_id: str
    _text: str
    _start: float
    _duration: float

    def video_id(self) -> str:
        return self._video_id

    def text(self) -> str:
        return self._text

    def start(self) -> float:
        return self._start

    def duration(self) -> float:
        return self._duration
