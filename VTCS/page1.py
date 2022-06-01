from tkinter import *
from tkinter import messagebox


def Ok():
    uname = e1.get()
    password = e2.get()

    if (uname == "" and password == ""):
        messagebox.showinfo("", "Blank Not allowed")

    elif (uname == "admin" and password == "123"):

        messagebox.showinfo("", "Login Success")
        root.destroy()
        import main

    else:
        messagebox.showinfo("", "Incorrent Username and Password")


root = Tk()
root.title("Admin Login")
root.geometry("300x200")
global e1
global e2

Label(
    root,
    text="VEHICLE TRACKING & COUNTING SYSTEM",
    padx=10,
    pady=10,
    bg='#fff'
).pack()

Label(root, text="UserName").place(x=10, y=50)
Label(root, text="Password").place(x=10, y=80)

e1 = Entry(root)
e1.place(x=140, y=50)

e2 = Entry(root)
e2.place(x=140, y=80)
e2.config(show="*")

Button(root, text="Login", command=Ok, height=2, width=10).place(x=100, y=120)

root.mainloop()