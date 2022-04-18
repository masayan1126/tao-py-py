from shared.Domain.x_file_system_path import XFileSystemPath
from shared.Domain.xfile import XFile
import urllib.request
import urllib.parse

from shared.Domain.xstr import XStr


class DownloadFileService:
    def download(self, x_file: XFile, download_path_to: XFileSystemPath, extension):
        # 対象の拡張子が含まれていれば
        if XStr(x_file.get_file_name()).has_end(extension):

            download_path_to = download_path_to.join(x_file.get_file_name()).of_text()

            try:
                urllib.request.urlretrieve(
                    x_file.get_url().get_href(),
                    download_path_to,
                )
            except ValueError:
                raise ValueError
