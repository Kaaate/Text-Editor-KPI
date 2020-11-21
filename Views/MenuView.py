from tkinter import Menu

class Menubar:
    def __init__(self, root, delegate):

        # delegate (UIController)
        self.delegate = delegate

        # main menu
        menubar = Menu(root)

        # file menu
        menu = Menu(menubar, tearoff=0)

        menu.add_command(label = "Open", command = self.delegate.openButtonPressed)
        menu.add_command(label = "Save", command = self.delegate.saveButtonPressed)
        menu.add_separator()
        menu.add_command(label = "Close", command = root.quit)

        menubar.add_cascade(label = "File", menu = menu)

        # task 13 menu
        menu = Menu(menubar, tearoff=0)
        menu.add_command(label="task13", command=self.delegate.task13ButtonPressed)
        menubar.add_cascade(label="task13", menu=menu)

        # task 15 menu
        menu = Menu(menubar, tearoff=0)

        menu.add_command(label="Begin with the letter a", command=self.delegate.task15aButtonPressed)
        menu.add_command(label="End with the letter w", command=self.delegate.task15bButtonPressed)
        menu.add_command(label="Begin and end with the same letter", command=self.delegate.task15cButtonPressed)
        menu.add_command(label="Contain at least one letter d", command=self.delegate.task15dButtonPressed)
        menu.add_command(label="Contain exactly three letters e", command=self.delegate.task15eButtonPressed)

        menubar.add_cascade(label="task15", menu=menu)

        # TODO task 30 menu

        # TODO task 31 menu

        # TODO task 51 menu

        # TODO task 55 menu

        # TODO task 56 menu

        # TODO task 61 menu

        # TODO task 64 menu (replace)

        # TODO task 64 menu (search)

        root.config(menu = menubar)
