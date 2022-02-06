# 対象のhtml要素のfieldに値をセットします
class SetWebElementService:
    def execute(self, web_element_list):

        list(
            map(
                lambda web_element: web_element.get_element().send_keys(
                    web_element.get_value()
                ),
                web_element_list,
            )
        )
