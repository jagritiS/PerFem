import os
from tkinter import Tk, Label, Button, Entry, StringVar, IntVar, messagebox, Text, END
from db import insert_data, read_data


class LoginPage:
    def __init__(self, master):
        self.master = master
        master.title("Perfem")
        master.geometry('500x500')
        master.configure(background="light pink")

        self.cl = StringVar()

        self.label = Label(master, text=" Add Notes Here", bg="light pink").grid(row=1, column=0, ipadx="10")

        #Entry(master, textvariable=self.cl).grid(row=2, column=1)
        self.cl = Text(master,height=20,width=60).grid(row=2, column=0)
        self.submit_button = Button(master, text="Submit", bg="light green", command=self.submit_data). \
            place(x=20, y=400)
        self.back_button = Button(master, text="Back", bg="light green", command=self.back_data). \
            place(x=100, y=400)
        self.close_button = Button(master, text="Close", bg="light blue", command=master.quit). \
            place(x=180, y=400)

    def back_data(self):
        self.master.destroy()
        os.system('python3 pcal.py')
    def submit_data(self):
        print("i m here ")
        result = self.cl.get("1.0", "end")
        print(result)
        sql2 = "INSERT INTO notes(note) VALUES (%s)"
        val = (result)
        vals = insert_data(sql2, val)
        if (vals == 1):
            print("success")
        else:
            print("not success")


root = Tk()
my_gui = LoginPage(root)
root.mainloop()
