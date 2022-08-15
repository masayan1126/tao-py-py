from pandas import DataFrame
from packages.my_rss.Application.rss_notification_usecase import RssNotificationUsecase
from shared.Domain.Converter.data_frame_converter import DataFrameConverter
from shared.Domain.Excel.xcsv import XCsv
from shared.Domain.FileSystem.x_file_system_path import XFileSystemPath
from shared.Domain.String.xstr import XStr

site_list_df: DataFrame = XCsv().read(
    XFileSystemPath(XStr("packages/my_rss/site_list.csv")),
    encoding="UTF-8",
    header=0,
)

site_list = DataFrameConverter.to_list(site_list_df)
RssNotificationUsecase(site_list).notify_to_line()
