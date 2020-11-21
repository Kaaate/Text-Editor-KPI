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

   def getString(self):
      return self.textField.get('1.0', 'end-1c')

   def setString(self, value):
      self.textField.delete('1.0', 'end-1c')
      self.textField.insert('1.0', value)

