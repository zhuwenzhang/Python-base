from tkinter import *


class P:
    def __init__(self):
        window = Tk()

        btok = Button(window, text="OK", fg="red", command=self.processOK)
        buCancel = Button(window, text="Cancel", bg="yellow", command=self.proccessCancel)

        btok.pack()
        buCancel.pack()
        window.mainloop()

    def processOK(self):
        print("OK button is clicked")

    def proccessCancel(self):
        print("Cancel button is clicked")


P()
