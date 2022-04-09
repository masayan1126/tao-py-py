import urllib.request, urllib.error
from shared.Domain.xurl import XUrl


class CheckIsValidUrlService:
    def handle(self, xurl: XUrl) -> bool:
        try:
            response = urllib.request.urlopen(xurl.get_href())
            return True
        except ValueError:
            return False
        finally:
            if "response" in locals():
                response.close()
