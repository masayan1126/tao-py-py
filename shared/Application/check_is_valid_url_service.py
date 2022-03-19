import urllib.request, urllib.error
from shared.Domain.xurl import XUrl


class CheckIsValidUrlService:
    def execute(self, xurl: XUrl) -> bool:
        try:
            f = urllib.request.urlopen(xurl.get_href())
            return True
        except:
            print(f"{xurl.get_href()}は無効なurlです")
            return False
        finally:
            if "f" in locals():
                f.close()
