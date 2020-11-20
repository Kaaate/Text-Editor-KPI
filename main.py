from tkinter import Tk
from Views.TextFieldView import TextField
from Views.MenuView import Menubar

root = Tk()
root.title("Lab6")
root.resizable(0,0)

text = TextField(root)
menubar = Menubar(root)

root.mainloop()
