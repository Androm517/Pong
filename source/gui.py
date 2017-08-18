import tkinter as tk


class Controller:
    """
    Den här klassen skickar information mellan de olika widgetarna. Den innehåller också
    gameLoop som styr rörelser i PongArea. Den här klassen hämtar information från en
    widget genom att definiera en funktion och den skickar information till en widget
    som adderat sig som en listener.
    """
    def __init__(self, master):
        self.play = False
        self.master = master
        self.listener = None
        self.objects = []

    def addListener(self, listener):
        self.listener = listener
        self.objects = [listener.create_oval(50, 25, 50 + 50, 25 + 50, fill="blue")]

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
    """
    Representation av spelytan. Här ritas paddlar och boll.
    """
    def __init__(self, master, **kwargs):
        super(PongArea, self).__init__(master, **kwargs)



class Menu(tk.Frame):
    """
    Meny med knappar start, stop, paus, och restart.
    """
    def __init__(self, master, stopFunc=None, startFunc=None, pausFunc=None, restartFunc=None, **kwargs):
        super(Menu, self).__init__(master, **kwargs)
        self.buttons = [Stop(self, text='Stop', command=stopFunc), Start(self, text='Start', command=startFunc) \
                        , Paus(self, text='Paus', command=pausFunc), Restart(self, text='Restart', command=restartFunc)]
        for button in self.buttons:
            button.pack()


class Button(tk.Button):
    """
    En knapp. Alla knapp objekt ärver den här klassen.
    """
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
