from shared.Domain.FileSystem.x_file_system_path import XFileSystemPath
from shared.Domain.File.x_file import XFile
import urllib.request
import urllib.parse

from shared.Domain.String.xstr import XStr


class FileDownloadeService:
    def download(self, x_file: XFile, download_path_to: XFileSystemPath, extension):
        # 対象の拡張子が含まれていれば
        if XStr(x_file.filename()).has_end(extension):

            path_str = download_path_to.join(x_file.filename()).of_text()

            try:
                urllib.request.urlretrieve(
                    x_file.x_url().href(),
                    path_str,
                )
            except ValueError:
                raise ValueError
