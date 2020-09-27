from tkinter import *
from PIL import ImageTk, Image

myLabel=""
button_back=""
button_forward=""
root = Tk()
root.title("Image viewer")

def forward(image_num):
    global myLabel
    global button_back
    global button_forward
    myLabel.grid_forget()
    myLabel = Label(image=image_list[image_num-1])
    button_forward=Button(root, text='>>', command=lambda: forward(image_num+1))
    button_back = Button(root, text='<<', command= lambda: back(image_num-1))

    if image_num == 5:
        button_forward = Button(root, text='>>', state=DISABLED)
    myLabel.grid(row = 0, column=0, columnspan = 3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row = 1, column=2)

    

def back(image_num):
    global myLabel
    global button_back
    global button_forward
    myLabel.grid_forget()
    myLabel = Label(image=image_list[image_num-1])
    button_forward=Button(root, text='>>', command=lambda: forward(image_num+1))
    button_back = Button(root, text='<<', command= lambda: back(image_num-1))

    if image_num == 1:
        button_back = Button(root, text='<<', state=DISABLED)
    myLabel.grid(row = 0, column=0, columnspan = 3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row = 1, column=2)

my_pic1 = Image.open("img/model1.jpg")
resized1 = my_pic1.resize((183,275),Image.ANTIALIAS)


my_pic2 = Image.open("img/model2.jpg")
resized2 = my_pic2.resize((183,275),Image.ANTIALIAS)

my_pic3 = Image.open("img/model3.jpg")
resized3 = my_pic3.resize((183,275),Image.ANTIALIAS)

my_pic4 = Image.open("img/model4.jpg")
resized4 = my_pic4.resize((183,275),Image.ANTIALIAS)

my_pic5 = Image.open("img/model5.jpg")
resized5 = my_pic5.resize((275, 183),Image.ANTIALIAS)

my_pic6 = Image.open("img/model6.jpg")
resized6 = my_pic6.resize((480,480),Image.ANTIALIAS)

my_pic7 = Image.open("img/model7.jpg")
resized7 = my_pic7.resize((480,480),Image.ANTIALIAS)


new_pic1 = ImageTk.PhotoImage(resized1)
new_pic2 = ImageTk.PhotoImage(resized2)
new_pic3 = ImageTk.PhotoImage(resized3)
new_pic4 = ImageTk.PhotoImage(resized4)
new_pic5 = ImageTk.PhotoImage(resized5)
new_pic6 = ImageTk.PhotoImage(resized6)
new_pic7 = ImageTk.PhotoImage(resized7)

image_list = [new_pic1,new_pic2,new_pic3,new_pic4,new_pic5]
myLabel=Label(image=new_pic1)
myLabel.grid(row=0,column=0,columnspan=3)

button_back = Button(root, text="<<", command= lambda: back(1))
button_quit = Button(root, text="Quit", command = root.quit)
button_forward = Button(root, text=">>", command =lambda: forward(2))

button_back.grid(row=1, column=0)
button_quit.grid(row=1, column=1)
button_forward.grid(row = 1, column=2)

root.mainloop()