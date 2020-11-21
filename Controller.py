# Controller for UI
from Views.TextFieldView import TextField
from Views.MenuView import Menubar

class UIController:
    def __init__(self, root):
        self.menuView = Menubar(root, self)
        self.textFieldView = TextField(root)

    def openButtonPressed(self):
        self.textFieldView.setString("openButtonPressed")

    def saveButtonPressed(self):
        self.textFieldView.setString("saveButtonPressed")

    def task13ButtonPressed(self):
        self.textFieldView.setString("task13ButtonPressed")

    def task15aButtonPressed(self):
        self.textFieldView.setString("task15aButtonPressed")

    def task15bButtonPressed(self):
        self.textFieldView.setString("task15bButtonPressed")

    def task15cButtonPressed(self):
        self.textFieldView.setString("task15cButtonPressed")

    def task15dButtonPressed(self):
        self.textFieldView.setString("task15dButtonPressed")

    def task15eButtonPressed(self):
        self.textFieldView.setString("task15eButtonPressed")

