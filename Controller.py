# Controller for UI
from Views.TextFieldView import TextField
from Views.MenuView import Menubar

class UIController:
    def __init__(self, root):
        self.menuView = Menubar(root)
        self.textFieldView = TextField(root)

    def setDelegateFoMenuView(self):s
        self.menuView.setDelegate(self)

    def buttonPressed(self):
        print("OK")
