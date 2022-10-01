from shared.Domain.File.file_download_service import FileDownloadService
from shared.Domain.FileSystem.x_file_system_path import XFileSystemPath
from shared.Domain.File.x_file import XFile
from shared.Domain.Url.x_url import XUrl

x_file = XFile(XUrl(encoded_href="https://www.home-movie.biz/mov/hts-samp001.mp4"))
download_path_to = XFileSystemPath.home_dir().join("desktop")

FileDownloadService().download(x_file=x_file, download_path_to=download_path_to)
