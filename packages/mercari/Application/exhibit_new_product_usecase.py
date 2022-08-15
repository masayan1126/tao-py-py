from shared.Domain.Automatic.automatic_operator import AutomaticOperator
from shared.Domain.Automatic.automatic_operator_impl import AutomaticOperatorImpl

from shared.Domain.FileSystem.software_process_operator import SoftWareProcessOperator
from shared.Domain.FileSystem.x_file_system_path import XFileSystemPath
from shared.Domain.String.xstr import XStr
from shared.Domain.Text.text_file_service import TextFileService
from shared.Domain.Text.x_text import XText


class ExhibitNewProductUsecase:
    def exhibit(self, detail_filepath: XFileSystemPath):

        detail = TextFileService(x_text=XText(detail_filepath)).read(encoding="UTF-8")

        automatic_operator: AutomaticOperator = AutomaticOperatorImpl()

        # 商品画像
        # automatic_operator.click(x=934, y=340, duration=2, wait_time=2.0)
        # # エクスプローラーのパス入力欄
        # pgui.click(x=841, y=56, duration=1)
        # # # # 画像のファイルパスを入力
        # pyperclip.copy(XFileSystemPath.home_dir().join("Desktop/images"))
        # pgui.hotkey("ctrl", "v")
        # pgui.click(x=843, y=455, duration=1)
        # pgui.hotkey("ctrl", "a")
        # pgui.hotkey("alt", "o")

        # # カテゴリ概要
        # pgui.click(x=1206, y=697, duration=1)
        # pgui.press("down")
        # pgui.press("down")
        # pgui.press("down")
        # pgui.press("down")
        # pgui.press("down")
        # pgui.press("down")
        # pgui.press("down")
        # pgui.press("down")
        # pgui.press("enter")

        # # カテゴリ詳細
        # pgui.click(x=1213, y=764, duration=1)
        # pgui.press("down")
        # pgui.press("down")
        # pgui.press("down")
        # pgui.press("enter")
        # pgui.click(x=1215, y=834, duration=1)
        # pgui.press("down")
        # pgui.press("down")
        # pgui.press("enter")
        # # pgui.click(x=1227, y=540, duration=1)
        # # pgui.press("down")
        # # pgui.press("down")

        # # # 商品の状態
        # pgui.click(x=1209, y=1016, duration=1)
        # pgui.press("down")
        # pgui.press("down")
        # pgui.press("enter")

        # pgui.scroll(-1000)

        # # # 商品名
        # pgui.click(x=1199, y=339, duration=1)
        # pyperclip.copy("ほぼ新品）16インチMacBook Pro シルバー(2019)")
        # pgui.hotkey("ctrl", "v")

        # # 商品の説明
        # pgui.click(x=1199, y=460, duration=1)
        # pyperclip.copy(detail)
        # pgui.hotkey("ctrl", "v")

        # pgui.scroll(-1500)

        # # 価格
        # pgui.click(x=1207, y=539, duration=1)
        # pyperclip.copy("180000")
        # pgui.hotkey("ctrl", "v")

        # # print(pgui.position())
