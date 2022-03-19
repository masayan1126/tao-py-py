import tkinter
from packages.jobcan import login


class Widget(tkinter.Frame):
    def __init__(self, root) -> None:
        super().__init__(root, width=790, height=490, borderwidth=4, relief="groove")
        self.root = root
        self.pack()
        self.pack_propagate(0)
        self.build()

    def build(self):
        self.close_btn()
        self.input_field()
        self.exec_btn()
        self.message = tkinter.Message(self)
        self.message.pack()

    def input_field(self):
        self.text_box = tkinter.Entry(self)
        self.text_box["width"] = 50
        self.text_box.pack()

    def input_handler(self):
        text = self.text_box.get()
        self.message["text"] = text
        print(text)

    def close_btn(self):
        btn = tkinter.Button(self)
        btn["text"] = "閉じる"
        btn["command"] = self.root.destroy
        # ボタンの配置
        btn.pack(side="bottom")

    def exec_btn(self):
        btn = tkinter.Button(self)
        btn["text"] = "実行する"
        btn["command"] = self.input_handler  # ()は不要
        btn.pack(side="bottom")

    def exec_btn(self):
        btn = tkinter.Button(self)
        btn["text"] = "ジョブカン"
        btn["command"] = login.authenticate  # ()は不要
        btn.pack(side="left")
