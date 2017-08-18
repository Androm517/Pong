import tkinter as tk




class PongArea(tk.Canvas):
    def __init__(self, master, **kwargs):
        super(PongArea, self).__init__(master, **kwargs)


class Menu(tk.Frame):
    def __init__(self, master, **kwargs):
        super(Menu, self).__init__(master, **kwargs)
        self.buttons = [Stop(self, text='Stop', command=None), Start(self, text='Start', command=None) \
                        , Paus(self, text='Paus', command=None), Restart(self, text='Restart', command=None)]
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
