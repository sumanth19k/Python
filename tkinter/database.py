from tkinter import *
import sqlite3 as sql

root = Tk()
root.title('database')
root.geometry('400x400')

conn = sql.connect('address.db')

c=conn.cursor()
# c.execute("""CREATE TABLE address(
#         first_name text,
#         last_name text,
#         address text,
#         city text,
#         zipcode integer
# )
# """)

def add():
    conn = sql.connect('address.db')
    c = conn.cursor()
    c.execute("INSERT INTO address VALUES (:f_name, :l_name, :address, :city, :zipcode)",
    {
        'f_name': f_name.get(),
        'l_name': l_name.get(),
        'address': address.get(),
        'city': city.get(),
        'zipcode': zipcode.get()

    })


    conn.commit()
    conn.close()

    f_name.delete(0, END)
    l_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    zipcode.delete(0, END)

def show():
    conn = sql.connect('address.db')
    c=conn.cursor()

    c.execute('select *,oid from address')
    records = c.fetchall()
    print(records)

    conn.commit()
    conn.close()

f_name = Entry(root, width=30)
f_name.grid(row=0, column=1, padx=20, pady=20)
l_name = Entry(root, width=30)
l_name.grid(row=1, column=1, padx=20, pady=20)
address = Entry(root, width=30)
address.grid(row=2, column=1, padx=20, pady=20)
city = Entry(root, width=30)
city.grid(row=3, column=1, padx=20, pady=20)
zipcode = Entry(root, width=30)
zipcode.grid(row=4, column=1, padx=20, pady=20)

f_name_label = Label(root, text="first name")
f_name_label.grid(row=0, column=0)

l_name_label = Label(root, text="last name")
l_name_label.grid(row=1, column=0)

address_label = Label(root, text="address")
address_label.grid(row=2, column=0)

city_label = Label(root, text="city")
city_label.grid(row=3, column=0)

zipcode_label = Label(root, text="zipcode")
zipcode_label.grid(row=4, column=0)

submit_btn = Button(root, text="Add the record", command=add)
submit_btn.grid(row=5, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

show_btn = Button(root, text="show records", command=show)
show_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

conn.commit()

conn.close()

root.mainloop()

