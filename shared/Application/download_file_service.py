from shared.Domain.xfile import XFile
import urllib.request
import urllib.parse

from shared.Domain.xstr import XStr
from shared.x_logger import XLogger


class DownloadFileService:
    def download(self, x_file: XFile, download_path_to, extension):
        # 対象の拡張子が含まれていれば
        if XStr(x_file.get_file_name()).has_end(extension):
            try:
                urllib.request.urlretrieve(
                    x_file.get_url().get_href(),
                    download_path_to + x_file.get_file_name(),
                )
            except ValueError:
                raise ValueError
