from __future__ import annotations
from dataclasses import dataclass
from typing import Any
import ffmpeg

from shared.Domain.FileSystem.x_file_system_path import XFileSystemPath


@dataclass
class YtVideoStreamer:
    _video_stream: Any
    _audio_stream: Any

    def __init__(
        self, video_path: XFileSystemPath, begin: float = None, duration: float = None
    ):
        self._video_stream = ffmpeg.input(
            video_path.to_text(),
            ss=begin,
            t=duration,
        )

        self._audio_stream = self._video_stream.audio

    def video_stream(self) -> Any:
        return self._video_stream

    def audio_stream(self) -> Any:
        return self._audio_stream

    def output(self, filepath: XFileSystemPath) -> None:
        self.video_stream().filter("fps", fps=15, round="up").output(
            self.video_stream(), self.audio_stream(), filepath.to_text(), crf=30
        ).run(overwrite_output=True)
