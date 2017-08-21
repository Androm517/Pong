import tkinter as tk


class PongLogicGuiController:
    """
    Den här klassen skickar information mellan de olika widgetarna. Den innehåller också
    gameLoop som styr rörelser i PongArea. Den här klassen hämtar information från en
    widget genom att definiera en funktion som tilldelas widgeten och den skickar information
    till en widget som adderat sig som en listener av sin typ.
    """
    def __init__(self, gameLogic=None):
        self.gameLogic = gameLogic
        self.play = False
        self.root = tk.Tk()
        self.pongArea = PongArea(self.root, width=300, height=100, bg='white')
        self.pongAreaObjects = self.pongArea.objects
        menuFunctions = [self.stop, self.start, self.paus, self.restart]
        self.menu = Menu(self.root, menuFunctions)
        self.pongArea.pack(side=tk.LEFT)
        self.menu.pack()

    # menu functions
    def start(self):
        self.play = True
        self.gameLoop()

    def stop(self):
        print("sett self.play = False")
        self.play = False

    def paus(self):
        print("self.play", self.play)

    def restart(self):
        pass

    # END menu functions

    def gameLoop(self):
        if self.play:
            print("hello hello hello")
            self.root.after(1000, self.gameLoop)

    def mainloop(self):
        self.root.mainloop()


class PongArea(tk.Canvas):
    """
    Representation av spelytan. Här ritas paddlar och boll.
    """
    def __init__(self, root, **kwargs):
        super(PongArea, self).__init__(root, **kwargs)
        self.objects = []
        self.objects.append(self.create_oval(50, 25, 50 + 50, 25 + 50, fill="blue"))


class Menu(tk.Frame):
    """
    Meny med knapparna start, stop, paus, och restart.
    """
    def __init__(self, root, funcList=None, **kwargs):
        super(Menu, self).__init__(root, **kwargs)
        if funcList is None:
            funclist = [None, None, None, None]
        self.buttons = [Stop(self, text='Stop', command=funcList[0]), Start(self, text='Start', command=funcList[1]),
                        Paus(self, text='Paus', command=funcList[2]), Restart(self, text='Restart', command=funcList[3])]
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
