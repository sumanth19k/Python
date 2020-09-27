from tkinter import *

root = Tk()

def myClick():
    myLabel = Label(root, text="i clicked a button!")
    myLabel.pack()

myButton = Button(root, text="click me!", command = myClick, bg="blue", fg="#ffffff")
myButton.pack()

root.mainloop()