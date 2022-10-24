from dataclasses import dataclass
from shared.Domain.DataFile.Csv.csv_file_operator_impl import CsvFileOperatorImpl
from shared.Domain.FileSystem.x_file_system_path import XFileSystemPath
from shared.Domain.Youtube.yt_transcript_list import YtTranscriptList


@dataclass
class YoutubeTranscriptBuildUsecase:
    _yt_transcript_list: YtTranscriptList

    def to_csv(self, save_path_to: XFileSystemPath):

        for d in self._yt_transcript_list.all():
            print(d)

        CsvFileOperatorImpl().output(
            save_path_to,
            self._yt_transcript_list.all(),
            index="vide_id",
            encoding="utf-8-sig",
        )

    def yt_transcript_list(self):
        return self._yt_transcript_list
