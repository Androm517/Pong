from tkinter import LEFT
from source.gui import *


root = tk.Tk()
controller = Controller(root)
# lägg till frames här
pongArea = PongArea(root, width=300, height=100, bg='white')
controller.addListenerPongArea(pongArea)
menu = Menu(root, controller.stop, controller.start, controller.printPlay)
pongArea.pack(side=LEFT)
menu.pack()

root.mainloop()
