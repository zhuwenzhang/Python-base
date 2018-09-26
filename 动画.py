from tkinter import *


class AnimationDemo:
    def __init__(self):
        window = Tk()
        window.title("Animation Demo")

        width = 250
        canvas = Canvas(window, bg="white", width=250, height=50)
        canvas.pack()

        x = 0
        canvas.create_text(x, 30, text="Message moving?", tags="text")

        dx = 3
        while True:
            canvas.move("text", dx, 0)
            canvas.after(100)
            canvas.update()
            if x < width:
                x += dx
            else:
                x = 0
                canvas.delete("text")
                canvas.create_text(x, 30, text="Message moving?", tags="text")

        window.mainloop()


AnimationDemo()
