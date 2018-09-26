from tkinter import *


class MouseKeyEventDemo:
    def __init__(self):
        window = Tk()
        window.title("Event Demo")
        canvas = Canvas(window, bg="white", width=200, height=100)
        canvas.pack()

        canvas.bind("<Button-1>", self.processMouseEvent)

        canvas.bind("<Key>", self.processKeyEvent)
        canvas.focus_set()

        window.mainloop()

    def processMouseEvent(self, event):
        print("clicked at", event.x, event.y)
        print("Position in the screen", event.x_root, event.y_root)
        print("Which button is clicked?", event.num)

    def processKeyEvent(self, event):
        print("Keysym?", event.keysym)
        print("char?", event.char)
        print("Keycode?", event.keycode)


MouseKeyEventDemo()
