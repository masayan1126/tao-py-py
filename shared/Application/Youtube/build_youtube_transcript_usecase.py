from dataclasses import dataclass
from shared.Domain.Excel.xcsv import XCsv
from shared.Domain.FileSystem.x_file_system_path import XFileSystemPath
from shared.Youtube.yt_transcript_list import YtTranscriptList


@dataclass
class BuildYoutubeTranscriptUsecase:

    _yt_transcript_list: YtTranscriptList

    def to_csv(self, save_path_to: XFileSystemPath):

        for d in self._yt_transcript_list.all():
            print(d)

        XCsv().output(
            save_path_to,
            self._yt_transcript_list.all(),
            index="vide_id",
            encoding="utf-8-sig",
        )

    def yt_transcript_list(self):
        return self._yt_transcript_list
