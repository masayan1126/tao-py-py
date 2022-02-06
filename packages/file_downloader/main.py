from shared.Application.download_file_service import DownloadFileService
from shared.Domain.xfile import XFile
from shared.Domain.xurl import XUrl

x_url = XUrl(href="https://www.home-movie.biz/mov/hts-samp001.mp4")
x_file = XFile(x_url)

download_path_to = "C:\\Users\\nishigaki\\Desktop\\"
file_name = x_file.get_file_name()

DownloadFileService().execute(
    x_file=x_file, download_path_to=download_path_to, extension=".mp4"
)
