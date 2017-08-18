from tkinter import LEFT
from source.game import *
from source.gui import *


top = tk.Tk()
controller = Controller(top)
# lägg till frames här
pongArea = PongArea(top, width=300, height=100, bg='white')
menu = Menu(top, controller.stop, controller.start, controller.printPlay)
pongArea.pack(side=LEFT)
menu.pack()

top.mainloop()
