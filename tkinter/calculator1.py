from tkinter import *
root = Tk()
root.title("Simple Calculator")
f_num =""
math=""

e = Entry(root, width=30, fg="black", border=5)
e.grid(row = 0, column=0, columnspan=4, padx=15, pady=15)

def buttonClick(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current)+str(number))

def buttonClear():
    e.delete(0, END)

def buttonAdd():
    global f_num
    global math
    math="addition" 
    first_number = e.get() 
    f_num = int(first_number)
    e.delete(0, END)

def buttonSub():
    global f_num
    global math
    math="subtraction" 
    first_number = e.get() 
    f_num = int(first_number)
    e.delete(0, END)
    

def buttonMul():
    global f_num
    global math
    math="multiplication" 
    first_number = e.get() 
    f_num = int(first_number)
    e.delete(0, END)

def buttonDiv():
    global f_num
    global math
    math="division" 
    first_number = e.get() 
    f_num = int(first_number)
    e.delete(0, END)

def buttonEqual():
    second_number = e.get()
    e.delete(0, END)
    if math=="addition":
         e.insert(0, f_num + int(second_number))
    if math=="subtraction":
         e.insert(0, f_num - int(second_number))
    if math=="multiplication":
         e.insert(0, f_num * int(second_number))
    if math=="division":
         e.insert(0, f_num / int(second_number))


button_1 = Button(root, text="1", padx=30, pady=25, command= lambda: buttonClick(1))
button_1.grid(row=3, column=1)

button_2 = Button(root, text="2", padx=30, pady=25, command= lambda: buttonClick(2))
button_2.grid(row=3, column=2)

button_3 = Button(root, text="3", padx=30, pady=25, command= lambda: buttonClick(3))
button_3.grid(row=3, column=3)

button_4 = Button(root, text="4", padx=30, pady=25, command= lambda: buttonClick(4))
button_4.grid(row=2, column=1)

button_5 = Button(root, text="5", padx=30, pady=25, command= lambda: buttonClick(5))
button_5.grid(row=2, column=2)

button_6 = Button(root, text="6", padx=30, pady=25, command= lambda: buttonClick(6))
button_6.grid(row=2, column=3)

button_7 = Button(root, text="7", padx=30, pady=25, command= lambda: buttonClick(7))
button_7.grid(row=1, column=1)

button_8 = Button(root, text="8", padx=30, pady=25, command= lambda: buttonClick(8))
button_8.grid(row=1, column=2)

button_9 = Button(root, text="9", padx=30, pady=25, command= lambda: buttonClick(9))
button_9.grid(row=1, column=3)

button_0 = Button(root, text="0", padx=30, pady=25, command= lambda: buttonClick(0))
button_0.grid(row=4, column=1)

button_clear = Button(root, text="clear", padx=60, pady=25, command=buttonClear)
button_clear.grid(row=4, column=2, columnspan=2)

button_plus = Button(root, text="+", padx=30, pady=25, command=buttonAdd)
button_plus.grid(row=5, column=1)

button_equal = Button(root, text="=", padx=70, pady=25, command=buttonEqual)
button_equal.grid(row=6,column=2, columnspan=2)

button_minus = Button(root, text="-", padx=31, pady=25, command=buttonSub)
button_mult = Button(root, text="*", padx=33, pady=25, command=buttonMul)
button_div = Button(root, text="/", padx=33, pady=25, command=buttonDiv)

button_minus.grid(row=5,column=2)
button_mult.grid(row=5,column=3)
button_div.grid(row=6,column=1)



root.mainloop()