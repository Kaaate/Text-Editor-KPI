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
        #task 64
        menu.add_command(label="Search", command=self.delegate.searchButtonPressed)
        menu.add_command(label="Replace", command=self.delegate.replaceButtonPressed)
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

        # task 30 menu
        menu = Menu(menubar, tearoff=0)

        menu.add_command(label="Delete the first character", command=self.delegate.task30aButtonPressed)
        menu.add_command(label="Delete the first and last character", command=self.delegate.task30bButtonPressed)
        menu.add_command(label="Delete the second character", command=self.delegate.task30cButtonPressed)
        menu.add_command(label="Replacement of the second character with the character ‘a’",
                         command=self.delegate.task30dButtonPressed
        )
        menu.add_command(label="Deleting the character with the number k", command=self.delegate.task30eButtonPressed)
        menu.add_command(label="Dividing a line into two equal parts and rearranging them in places (if line length - even)",
                         command=self.delegate.task30fButtonPressed
        )
        menu.add_command(label="Dividing the line into two equal parts and the middle character, permutation parts in places, with the middle character remaining in place (if line length - odd number).",
                         command=self.delegate.task30gButtonPressed
        )

        menubar.add_cascade(label="task30", menu=menu)

        # task 31 menu

        menu = Menu(menubar, tearoff=0)

        menu.add_command(label="Replace all 'a' to 'A'", command=self.delegate.task31ButtonPressed)

        menubar.add_cascade(label="task31", menu=menu)

        # TODO task 51 menu

        # TODO task 55 menu

        # TODO task 56 menu

        # TODO task 61 menu

        root.config(menu = menubar)
