import os
import datetime
from tkinter import Tk, Label, Button, Entry, StringVar, IntVar, messagebox

import db

from db import insert_data, read_data, getUsers
from models.data import data

current_user = ""
class LoginPage:
    def __init__(self, master):
        self.master = master
        master.title("Perfem")
        master.geometry('500x500')
        master.configure(background="light pink")

        self.cl = StringVar()
        self.pl = StringVar()

        self.label = Label(master, text=" User Login ", bg="light pink").grid(row=1, column=0, ipadx="10")
        self.label = Label(master, text="Username", bg="light pink").grid(row=2, column=0, ipadx="10")
        self.label = Label(master, text="Password", bg="light pink").grid(row=4, column=0, ipadx="10")

        Entry(master, textvariable=self.cl).grid(row=2, column=1)
        Entry(master, textvariable=self.pl).grid(row=4, column=1)

        self.submit_button = Button(master, text="Submit", bg="light green", command=self.submit_data).grid(row=8,
                                                                                                            column=0)
        self.close_button = Button(master, text="Close", bg="light blue", command=master.quit).grid(row=8, column=2)

    def submit_data(self):

        cl = self.cl.get()
        pl = self.pl.get()
        sql = "SELECT * FROM users where email='"+cl+"' and password='"+pl+"'"
        flag = read_data(sql)
        if(flag == 1):
            global current_user
            print("login successful ")
            active_user = getUsers(sql)
            print("current user id is ")
            print(active_user)
            current_user = active_user
            today = datetime.date.today()
            end_date = today + datetime.timedelta(days=7)
            #sql1 = "SELECT * FROM p_cal WHERE user_id="+"'"+current_user+"'"
            #flag2 = read_data(sql)
            db.setId(current_user)
            messagebox.showinfo("Login Message", "Successfully Logged In ")
            d = data("current_user")
            d.setName("current_user")
            self.master.destroy()
            #os.system('python3 pcal.py')
        else:
            print("login failed")
            messagebox.showerror("Login Message", "Please Try Again")

root = Tk()
my_gui = LoginPage(root)
root.mainloop()
