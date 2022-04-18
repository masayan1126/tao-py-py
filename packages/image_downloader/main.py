# import re

# import pandas as pd
# from shared.Domain.Scraping.i_html_analyzer import IHtmlAnalyzer
# from shared.Domain.Scraping.soup_factory import SoupFactory
# from shared.Domain.xregex import XRegex
# from shared.Domain.xstr import XStr
# from shared.Domain.xcsv import XCsv
# from shared.Domain.xurl import XUrl
# from shared.di_container import DiContainer

# soup = SoupFactory().create(XUrl(""))
# i_html_analyzer: IHtmlAnalyzer = DiContainer().resolve(IHtmlAnalyzer)
# i_html_analyzer.bind(soup)

# url_result_set = i_html_analyzer.find_by_selector(selector="main")
# name_result_set = i_html_analyzer.find_by_selector(
#     selector="main"
# )  # asideは除く

# atags = url_result_set[0].find_all("a")

# urls = list(
#     map(
#         lambda atag: atag.get("href"),
#         atags,
#     )
# )

# names = list(
#     map(
#         lambda tag: tag.text.strip(),
#         name_result_set,
#     )
# )


# results = []

# for i, url in enumerate(urls):
#     slug = XRegex("(?<=brand\/).+?(?=\/)").partial_match(target=XStr(url))
#     d = {"name": names[i], "slag": slug}
#     results.append(d)

# XCsv().output(XFileSystemPath.home_dir().join("Desktop/brands.csv")
#     results,
# )

# download_path_to = (XFileSystemPath.home_dir().join("Desktop/downloads")
# )

# # 画像URLからダウンロード
# for i, image_url in enumerate(image_list):
#     x_url = XUrl(href=image_url)
#     if CheckIsValidUrlService().execute(x_url):
#         x_image = XImage(x_url=x_url, alt="")
#         DownloadImageService().execute(
#             x_image=x_image, download_path_to=download_path_to, prefix=i + 1
#         )
