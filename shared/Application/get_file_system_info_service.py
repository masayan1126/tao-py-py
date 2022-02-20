import os
from shared.Domain.xpath import XPath


# 対象のディレクトに存在するディレクトリ名とファイル名を取得します
class GetFileSystemInfoService:
    def execute(self, xpath: XPath):
        return os.walk(xpath.get_path())
