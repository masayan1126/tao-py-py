from re import X
from shared.Enums.post_category import PostCategory
from shared.Domain.xurl import XUrl
# from injector import inject

class GetPostThumbnailService:
    # @inject
    # def __init__(self, xurl:XUrl):
    #     self.xurl = XUrl("")

    def execute(self, post_category:PostCategory):

        if post_category == PostCategory.PYTHON:
            return XUrl("https://drive.google.com/file/d/1r65VN9nFEnuo6rog4l7pOGa4hEJQnSW0/view?usp=sharing")

        # match os:
        #     case OsType.WINDOWS:
        #         subprocess.Popen(["start",app_path])
        #     case OsType.DARWIN:
        #         subprocess.Popen(["open", app_path])
        #     case OsType.LINUX:
        #         subprocess.Popen(["see", app_path])
        #     case _:
        #         pass
