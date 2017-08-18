import tkinter as tk




class PongArea:
    pass


class Menu(tk.Frame):
    def __init__(self, master, **kwargs):
        super(Menu, self).__init__(master, **kwargs)
        self.buttons = [Stop(master, text='Stop', command=None), Start(master, text='Start', command=None) \
                        , Paus(master, text='Paus', command=None), Restart(master, text='Restart', command=None)]
        for button in self.buttons:
            button.pack()


class Button(tk.Button):
    def __init__(self, master, **kwargs):
        super(Button, self).__init__(master, **kwargs)


class Start(Button):
    def __init__(self, master, **kwargs):
        super(Start, self).__init__(master, **kwargs)


class Stop(Button):
    def __init__(self, master, **kwargs):
        super(Stop, self).__init__(master, **kwargs)


class Paus(Button):
    def __init__(self, master, **kwargs):
        super(Paus, self).__init__(master, **kwargs)


class Restart(Button):
    def __init__(self, master, **kwargs):
        super(Restart, self).__init__(master, **kwargs)


top = tk.Tk()
# lägg till frames här
menu = Menu(top)

top.mainloop()
