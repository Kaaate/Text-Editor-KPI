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

    # task 13
    def task13ButtonPressed(self):
        self.textFieldView.setString("task13ButtonPressed")

    # task 15
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

    # task 30
    def task30aButtonPressed(self):
        self.textFieldView.setString("task30aButtonPressed")

    def task30bButtonPressed(self):
        self.textFieldView.setString("task30bButtonPressed")

    def task30cButtonPressed(self):
        self.textFieldView.setString("task30cButtonPressed")

    def task30dButtonPressed(self):
        self.textFieldView.setString("task30dButtonPressed")

    def task30eButtonPressed(self):
        self.textFieldView.setString("task30eButtonPressed")

    def task30fButtonPressed(self):
        self.textFieldView.setString("task30fButtonPressed")

    def task30gButtonPressed(self):
        self.textFieldView.setString("task30gButtonPressed")

    #task31
    def task31ButtonPressed(self):
        self.textFieldView.setString("task31ButtonPressed")

    # TODO task 51 menu

    # TODO task 55 menu

    # TODO task 56 menu

    # TODO task 61 menu

    # task 64 menu (replace)
    def replaceButtonPressed(self):
        self.textFieldView.setString("replaceButtonPressed")

    # task 64 menu (search)
    def searchButtonPressed(self):
        self.textFieldView.setString("searchButtonPressed")
