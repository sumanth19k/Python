from tkinter import *
root = Tk()
root.title('Frames')

frame1 = LabelFrame(root, text='First Frame', padx=50, pady=50)
frame1.pack(padx=10, pady=10)

b = Button(frame1, text='dont click here')
b.pack()

root.mainloop()