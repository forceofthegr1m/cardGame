from tkinter import *
from tkinter import ttk


score1 = 0
score2 = 0
score3 = 0
score4 = 0
score5 = 0
score6 = 0


class Main():
    list1 = ["1", "2", "3", "4", "5"]

    def __init__(self, root):
        global score1
        global score2
        global score3
        global score4
        global score5
        global score6

        root.title("What Will One Day Hopefully Be A Game (tm)")
        root.geometry('700x600+30+30')

        # Frames
        mainframe = ttk.Frame(root, relief='raised')
        mainframe.grid(column=0, row=0, padx=10, pady=10, sticky='N, W, E, S')

        playframe = ttk.Frame(mainframe, relief='ridge')
        playframe.grid(column=0, row=0, padx=10, pady=10, sticky='N, W, E, S')

        controlframe = ttk.Frame(mainframe, relief='ridge')
        controlframe.grid(column=1, row=0, padx=10, pady=10)

        van1 = ttk.Frame(playframe, relief='solid')
        van1.grid(column=0, row=1, padx=15, pady=15, sticky='N, W, E, S')

        van2 = ttk.Frame(playframe, relief='solid')
        van2.grid(column=0, row=3, padx=15, pady=15, sticky='N, W, E, S')

        van3 = ttk.Frame(playframe, relief='solid')
        van3.grid(column=1, row=1, padx=15, pady=15, sticky='N, W, E, S')

        van4 = ttk.Frame(playframe, relief='solid')
        van4.grid(column=1, row=3, padx=15, pady=15, sticky='N, W, E, S')

        van5 = ttk.Frame(playframe, relief='solid')
        van5.grid(column=2, row=1, padx=15, pady=15, sticky='N, W, E, S')

        van6 = ttk.Frame(playframe, relief='solid')
        van6.grid(column=2, row=3, padx=15, pady=15, sticky='N, W, E, S')

        score1 = ttk.Frame(playframe, relief='solid')
        score1.grid(column=0, row=0, padx=5, pady=5, sticky='N, W, E, S')

        score2 = ttk.Frame(playframe, relief='solid')
        score2.grid(column=0, row=2, padx=5, pady=5, sticky='N, W, E, S')

        score3 = ttk.Frame(playframe, relief='solid')
        score3.grid(column=1, row=0, padx=5, pady=5, sticky='N, W, E, S')

        score4 = ttk.Frame(playframe, relief='solid')
        score4.grid(column=1, row=2, padx=5, pady=5, sticky='N, W, E, S')

        score5 = ttk.Frame(playframe, relief='solid')
        score5.grid(column=2, row=0, padx=5, pady=5, sticky='N, W, E, S')

        score6 = ttk.Frame(playframe, relief='solid')
        score6.grid(column=2, row=2, padx=5, pady=5, sticky='N, W, E, S')

        # Buttons
        cardplay = ttk.Button(controlframe, text="Play A Card")
        cardplay.grid(column=0, row=0, padx=5, pady=5)

        facecardplay = ttk.Button(controlframe, text="Play A Face Card")
        facecardplay.grid(column=0, row=1, padx=5, pady=5)

        testbtn = ttk.Button(controlframe, text="Populate Lists", command=self.test)
        testbtn.grid(column=0, row=2, padx=5, pady=5)

        # StringVars
        self.score1str = StringVar()
        self.score2str = StringVar()
        self.score3str = StringVar()
        self.score4str = StringVar()
        self.score5str = StringVar()
        self.score6str = StringVar()

        self.van1listvar = StringVar(value=self.list1)
        self.van1listvar.set(self.list1)

        # Labels
        score1lbla = ttk.Label(score1, text="Value: ")
        score1lbla.grid(column=0, row=0, padx=5, pady=5)

        score1lblb = ttk.Label(score1, textvariable=self.score1str)
        score1lblb.grid(column=1, row=0, padx=5, pady=5)

        score2lbla = ttk.Label(score2, text="Value: ")
        score2lbla.grid(column=0, row=0, padx=5, pady=5)

        score2lblb = ttk.Label(score2, textvariable=self.score2str)
        score2lblb.grid(column=1, row=0, padx=5, pady=5)

        score3lbla = ttk.Label(score3, text="Value: ")
        score3lbla.grid(column=0, row=0, padx=5, pady=5)

        score3lblb = ttk.Label(score3, textvariable=self.score3str)
        score3lblb.grid(column=1, row=0, padx=5, pady=5)

        score4lbla = ttk.Label(score4, text="Value: ")
        score4lbla.grid(column=0, row=0, padx=5, pady=5)

        score4lblb = ttk.Label(score4, textvariable=self.score4str)
        score4lblb.grid(column=1, row=0, padx=5, pady=5)

        score5lbla = ttk.Label(score5, text="Value: ")
        score5lbla.grid(column=0, row=0, padx=5, pady=5)

        score5lblb = ttk.Label(score5, textvariable=self.score5str)
        score5lblb.grid(column=1, row=0, padx=5, pady=5)

        score6lbla = ttk.Label(score6, text="Value: ")
        score6lbla.grid(column=0, row=0, padx=5, pady=5)

        score6lblb = ttk.Label(score6, textvariable=self.score6str)
        score6lblb.grid(column=1, row=0, padx=5, pady=5)

        # Listboxes
        self.van1cards = Listbox(van1, relief='ridge')
        self.van1cards.grid(column=0, row=0, padx=5, pady=5)

        self.van2cards = Listbox(van2, relief='ridge')
        self.van2cards.grid(column=0, row=0, padx=5, pady=5)

        self.van3cards = Listbox(van3, relief='ridge')
        self.van3cards.grid(column=0, row=0, padx=5, pady=5)

        self.van4cards = Listbox(van4, relief='ridge')
        self.van4cards.grid(column=0, row=0, padx=5, pady=5)

        self.van5cards = Listbox(van5, relief='ridge')
        self.van5cards.grid(column=0, row=0, padx=5, pady=5)

        self.van6cards = Listbox(van6, relief='ridge')
        self.van6cards.grid(column=0, row=0, padx=5, pady=5)

    def test(self):
        self.list1.append('6')
        self.van1listvar.set(self.list1)


if __name__ == "__main__":
    root = Tk()
    Main(root)
    root.mainloop()