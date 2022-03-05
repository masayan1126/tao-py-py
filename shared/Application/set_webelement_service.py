from typing import List
from shared.Domain.xweb_element_list import XWebElementList

# 対象のhtml要素のfieldに値をセットします
class SetWebElementService:
    def execute(self, web_element_list: XWebElementList):

        list(
            map(
                lambda xweb_element: xweb_element.get_element().send_keys(
                    xweb_element.get_value()
                ),
                web_element_list.get_web_element_list(),
            )
        )
