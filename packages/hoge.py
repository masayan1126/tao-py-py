from multiprocessing.connection import wait
from pyexpat import XMLParserType
import sys
from time import sleep
import pyautogui as pgui
import pyperclip
from shared.Domain.Automatic.automatic_operator import AutomaticOperator
from shared.Domain.Automatic.automatic_operator_impl import AutomaticOperatorImpl
from shared.Domain.FileSystem.software_process_operator import SoftWareProcessOperator

from shared.Domain.FileSystem.x_file_system_path import XFileSystemPath
from shared.Domain.Scraping.web_browser_operator import WebBrowserOperator
from shared.Domain.String.xstr import XStr
from shared.Domain.Text.x_text import XText


# int_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# # 何個ずつに分割するかpa
# n = 4a

# # リスト内包表記
# # rangeの第3引数(step)に数値を指定すると、stepずつ増加する等差数列が生成される([0, 4, 8]の1つずつがiに入る)
# splited = [int_array[i : i + n] for i in range(0, len(int_array), n)]
# automatic_operator: AutomaticOperator = AutomaticOperatorImpl()
# print(automatic_operator.get_position())


# 文字列の近似値

string1 = "lemon"
string2 = "almne"

result = 0

for st in string1:
    if st in string1 and string1.find(st) == string2.find(st):
        result += 1
        print(st)

length = len(string1)

print(result)
