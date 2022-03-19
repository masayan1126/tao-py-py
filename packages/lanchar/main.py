#!/usr/bin/env python
# -*- coding: utf8 -*-

import sys
import tkinter as tk

from packages.lanchar.widget import Widget


# ウィジェット用のオブジェクト生成
root = tk.Tk()

# アプリバーに表示するタイトル
root.title(u"Software Title")

# ウインドウサイズ
root.geometry("800x500")

# パーツの設定
widget = Widget(root=root)

# 起動
widget.mainloop()
