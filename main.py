from tkinter import Tk
from Controller import UIController

# create window
root = Tk()
root.title("Lab6")
root.resizable(0,0)

# create view
uiViewController = UIController(root)
uiViewController.setDelegateFoMenuView()

root.mainloop()
