from tkinter import LEFT
from source.game import *
from source.gui import *


top = tk.Tk()
# lägg till frames här
pongArea = PongArea(top, width=300, height=100, bg='white')
menu = Menu(top)
pongArea.pack(side=LEFT)
menu.pack()

top.mainloop()
