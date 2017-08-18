import tkinter as tk


class Controller:
    def __init__(self, master):
        self.play = False
        self.master = master

    def start(self):
        self.play = True
        self.gameLoop()

    def gameLoop(self):
        if self.play:
            print("hello hello hello")
            self.master.after(1000, self.gameLoop)

    def stop(self):
        print("sett self.play = False")
        self.play = False

    def printPlay(self):
        print("self.play", self.play)


class PongArea(tk.Canvas):
    def __init__(self, master, **kwargs):
        super(PongArea, self).__init__(master, **kwargs)
        self.objects = [self.create_oval(50, 25, 50 + 50, 25 + 50, fill="blue")]


class Menu(tk.Frame):
    def __init__(self, master, stopFunc=None, startFunc=None, pausFunc=None, restartFunc=None, **kwargs):
        super(Menu, self).__init__(master, **kwargs)
        self.buttons = [Stop(self, text='Stop', command=stopFunc), Start(self, text='Start', command=startFunc) \
                        , Paus(self, text='Paus', command=pausFunc), Restart(self, text='Restart', command=restartFunc)]
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
