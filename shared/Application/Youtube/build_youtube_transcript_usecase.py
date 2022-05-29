from dataclasses import dataclass
from shared.Domain.Excel.xcsv import XCsv
from shared.Domain.FileSystem.x_file_system_path import XFileSystemPath
from shared.Domain.Url.x_url import XUrl
from shared.Youtube.yt_transcript_list import YtTranscriptList


@dataclass
class BuildYoutubeTranscriptUsecase:

    yt_transcript_list: YtTranscriptList

    def to_csv(self, save_path_to: XFileSystemPath):

        for d in self.yt_transcript_list.all():
            print(d)

        XCsv().output(
            save_path_to,
            self.yt_transcript_list.all(),
            index="vide_id",
            encoding="utf-8-sig",
        )
