from tkinter import *


class ScollText:
    def __init__(self):
        window = Tk()
        window.title("Scoll Text Demo")

        frame1 = Frame(window)
        frame1.pack()
        scrollbar = Scrollbar(frame1)
        scrollbar.pack(side=RIGHT, fill=Y)
        text = Text(frame1, width=40, height=10, wrap=WORD, yscrollcommand=scrollbar.set)

        text.pack()
        scrollbar.config(command=text.yview)

        window.mainloop()


ScollText()
