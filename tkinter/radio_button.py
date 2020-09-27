from tkinter import *
root= Tk()
root.title('radio')

MODES = [
    ("farmhouse", "farmhouse"),
    ("pepperoni", "pepperoni"),
    ("onion", "onion"),
    ("mushroom", "mushroom")
]

pizza  = StringVar()
pizza.set(None)


for x, y in MODES:
    Radiobutton(root, text=x, variable=pizza, value=y).pack(anchor=W)
    

def clicked(value):
    myLabel = Label(root, text=value)
    myLabel.pack()

# myLabel = Label(root, text=pizza.get())
# myLabel.pack()

myButton = Button(root, text="Click me", command=lambda: clicked(pizza.get()))
myButton.pack()

root.mainloop()