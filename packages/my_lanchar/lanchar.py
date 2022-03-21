import datetime
import tkinter
from typing import Callable, Optional
from packages.jobcan import login
from shared.Domain.i_widget import IWidget


class Lanchar(IWidget):
    def __init__(self, root) -> None:
        self.root = root
        frame = tkinter.Frame(root)

        # # 各列の引き伸ばし設定
        root.grid_columnconfigure(0, weight=1)
        root.grid_columnconfigure(1, weight=1)
        root.grid_columnconfigure(2, weight=1)
        root.grid_rowconfigure(0, weight=0)
        root.grid_rowconfigure(1, weight=1)
        root.grid_rowconfigure(2, weight=1)

    def build(self):
        label = self.label(datetime.date.today())
        label.grid(column=0, row=0, sticky=tkinter.E, columnspan=3)

        # ボタン
        btn1 = self.btn("勤怠", login.authenticate)
        btn1.grid(column=0, row=1, sticky="NSEW")

        btn2 = self.btn("②")
        btn2.grid(column=1, row=1, sticky="NSEW")

        btn3 = self.btn("③")
        btn3.grid(column=2, row=1, sticky="NSEW")

        btn4 = self.btn("④")
        btn4.grid(column=0, row=2, sticky="NSEW")

        btn5 = self.btn("⑤")
        btn5.grid(column=1, row=2, sticky="NSEW")

        btn6 = self.btn("⑥")
        btn6.grid(column=2, row=2, sticky="NSEW")

        return self

    def label(self, text: str):
        return tkinter.Label(text=text)

    def btn(self, text: str, command: Optional[Callable] = None):
        btn = tkinter.Button()
        btn["text"] = text
        btn["command"] = command

        return btn

    # def input_field(self):
    #     self.text_box = tkinter.Entry(self)
    #     self.text_box["width"] = 50
    #     self.text_box.pack()

    # def input_handler(self):
    #     text = self.text_box.get()
    #     self.message["text"] = text
    #     print(text)

    # def input_handler(self):
    # self.message = tkinter.Message(self)
    # self.message.pack()
