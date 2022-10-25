import tkinter
from packages.my_lanchar.lanchar import Lanchar
from shared.Domain.i_widget import IWidget


root = tkinter.Tk()
root.title("Launcher")
root.geometry("400x200")

# パーツの設定
lanchar: IWidget = Lanchar(root=root).build()

root.mainloop()
