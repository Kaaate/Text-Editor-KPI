from tkinter.scrolledtext import ScrolledText

class TextField:
   def __init__(self,master):
      self.master = master
      self.textField = ScrolledText(
         self.master,
         width = 50,
         height = 30,
         font = 20
      )
      self.textField.pack()

   def printText(self):
      print(self.textField.get('1.0', 'end-1c'))