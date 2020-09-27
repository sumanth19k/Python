from tkinter import *

root = Tk()

e = Entry(root, width=50, border=4)
e.pack()

def myClick():
    myLabel = Label(root, text="hello "+e.get()+" have a good day!!")
    myLabel.pack()

myButton = Button(root, text="click me!", command = myClick, bg="blue", fg="#ffffff", )
myButton.pack()


root.mainloop()