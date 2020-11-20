from tkinter.scrolledtext import ScrolledText
from Views.ViewConfiguration import Congifuration

class TextField:
   def __init__(self,master):
      self.master = master
      self.textField = ScrolledText(
         self.master,
         width = Congifuration.windowWidth,
         height = Congifuration.windowHeight,
         font = Congifuration.textSize
      )
      self.textField.pack()

   def printText(self):
      print(self.textField.get('1.0', 'end-1c'))