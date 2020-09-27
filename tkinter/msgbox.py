from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('message box')

def popup():
    response = messagebox.askyesno('this is my popup', 'hello world!')
    if response == 1:
        Label(root, text="you clicked yes!").pack()
    else:
        Label(root, text="you clicked no!!").pack()
#showerror, showwarning, showinfo, askquestion, askokcancel

Button(root, text='popup', command=popup).pack()

Button(root, text="exit", command=root.quit).pack()
root.mainloop()
