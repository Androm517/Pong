import tkinter as tk


class Controller:
    """
    Den här klassen skickar information mellan de olika widgetarna. Den innehåller också
    gameLoop som styr rörelser i PongArea. Den här klassen hämtar information från en
    widget genom att definiera en funktion som tilldelas widgeten och den skickar information
    till en widget som adderat sig som en listener av sin typ.
    """
    def __init__(self, root):
        self.play = False
        self.root = root
        self.listener = None
        self.objects = []

    def addListenerPongArea(self, pongArea):
        self.listener = pongArea
        self.objects = [pongArea.create_oval(50, 25, 50 + 50, 25 + 50, fill="blue")]

    def start(self):
        self.play = True
        self.gameLoop()

    def gameLoop(self):
        if self.play:
            print("hello hello hello")
            self.root.after(1000, self.gameLoop)

    def stop(self):
        print("sett self.play = False")
        self.play = False

    def printPlay(self):
        print("self.play", self.play)


class PongArea(tk.Canvas):
    """
    Representation av spelytan. Här ritas paddlar och boll.
    """
    def __init__(self, root, **kwargs):
        super(PongArea, self).__init__(root, **kwargs)


class Menu(tk.Frame):
    """
    Meny med knapparna start, stop, paus, och restart.
    """
    def __init__(self, root, stopFunc=None, startFunc=None, pausFunc=None, restartFunc=None, **kwargs):
        super(Menu, self).__init__(root, **kwargs)
        self.buttons = [Stop(self, text='Stop', command=stopFunc), Start(self, text='Start', command=startFunc),
                        Paus(self, text='Paus', command=pausFunc), Restart(self, text='Restart', command=restartFunc)]
        for button in self.buttons:
            button.pack()


class Button(tk.Button):
    """
    En knapp. Alla knapp objekt ärver den här klassen.
    """
    def __init__(self, root, **kwargs):
        super(Button, self).__init__(root, **kwargs)


class Start(Button):
    def __init__(self, root, **kwargs):
        super(Start, self).__init__(root, **kwargs)


class Stop(Button):
    def __init__(self, root, **kwargs):
        super(Stop, self).__init__(root, **kwargs)


class Paus(Button):
    def __init__(self, root, **kwargs):
        super(Paus, self).__init__(root, **kwargs)


class Restart(Button):
    def __init__(self, root, **kwargs):
        super(Restart, self).__init__(root, **kwargs)
