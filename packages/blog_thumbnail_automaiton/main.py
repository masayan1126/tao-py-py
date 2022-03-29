from shared.Application.get_post_thumbnail_url_service import GetPostThumbnailService
from shared.Domain.xurl import XUrl
from shared.Enums.post_category import PostCategory
# from injector import Injector

# injector = Injector()
# get_post_thumbnail_url_service = injector.get(GetPostThumbnailService)

xurl = GetPostThumbnailService().execute(PostCategory.PYTHON)
print(xurl.get_href())

# 画像をダウンロードしてアップロードする

