from shared.Domain.FileSystem.x_file_system_path import XFileSystemPath
from shared.Domain.FileSystem.x_file import XFile
import urllib.request
import urllib.parse

from shared.Domain.xstr import XStr


class FileDownloader:
    def download(self, x_file: XFile, download_path_to: XFileSystemPath, extension):
        # 対象の拡張子が含まれていれば
        if XStr(x_file.filename()).has_end(extension):

            download_path_to = download_path_to.join(x_file.filename()).of_text()

            try:
                urllib.request.urlretrieve(
                    x_file.x_url().href(),
                    download_path_to,
                )
            except ValueError:
                raise ValueError
