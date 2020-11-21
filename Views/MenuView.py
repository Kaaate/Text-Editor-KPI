from tkinter import Menu

class Menubar:
    def __init__(self, root):

        # delegate (UIController)
        self.delegate = None

        # main menu
        menubar = Menu(root)

        # TODO Create menus
        # File menu
        filemenu = Menu(menubar, tearoff=0)

        filemenu.add_command(label = "Open", command = self.buttonPressed)
        filemenu.add_command(label = "Save", command = self.buttonPressed)
        filemenu.add_command(label = "Close", command = self.buttonPressed)

        menubar.add_cascade(label = "File", menu = filemenu)

        root.config(menu = menubar)

    def setDelegate(self, delegate):
        self.delegate = delegate

    # TODO Create *name*ButtonPressedFunctions
    def buttonPressed(self):
        if self.delegate is not None:
            self.delegate.buttonPressed()

