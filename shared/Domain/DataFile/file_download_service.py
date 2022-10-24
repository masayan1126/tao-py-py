from shared.Domain.FileSystem.x_file_system_path import XFileSystemPath
from shared.Domain.DataFile.x_file import XFile
import urllib.request


class FileDownloadService:
    def download(self, x_file: XFile, download_path_to: XFileSystemPath) -> str:

        downloaded_file_path, message = urllib.request.urlretrieve(
            x_file.filepath().href(),
            download_path_to.join(x_file.filename()).to_text(),
        )

        return downloaded_file_path
