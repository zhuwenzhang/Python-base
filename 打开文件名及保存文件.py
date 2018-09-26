from tkinter.filedialog import *

filenameforReading = askopenfilename()
print("you can read from" + filenameforReading)

filenameforWriting = asksaveasfilename()
print("you can write data to" + filenameforWriting)
