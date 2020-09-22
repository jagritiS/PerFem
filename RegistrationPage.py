import os
from datetime import datetime
from tkinter import Tk, Label, Button, Entry, StringVar, IntVar, messagebox
from tkinter.ttk import Combobox

from mysql.connector import Date

import db
from db import insert_data, getUsers, read_data

reg_user = ""
class RegistrationPage:
    def __init__(self, master):
        self.master = master
        master.title("Perfem")
        master.geometry('600x400')
        master.configure(background="light pink")

        self.name = StringVar()
        self.email = StringVar()
        self.contact = StringVar()
        self.dob = StringVar()
        self.dob_year = StringVar()
        self.dob_month = StringVar()
        self.dob_day = StringVar()
        self.username = StringVar()
        self.password = StringVar()

        dob_year = Combobox(master, width=5, textvariable=self.dob_year)
        dob_month = Combobox(master, width=8, textvariable=self.dob_month)
        dob_day = Combobox(master, width=5, textvariable=self.dob_day)

        # Adding combobox drop down list
        dob_day['values'] = (' 1', ' 2', ' 3', ' 4', ' 5', ' 6', ' 7', ' 8', ' 9', ' 10', ' 11',
                        ' 12', ' 13', ' 14', ' 15', ' 16', ' 17', ' 18', ' 19', ' 20',
                        ' 21', ' 22', ' 23', ' 24', '25', '26', '27', '28', '29', '30', '31')
        dob_month['values'] = ('jan','feb','mar','apr','may','jun','jul','aug','sept','oct','nov','dec')
        dob_year['values']=('1980','1981','1982','1983','1984','1995','1996','1997','1998','2000','2001','2003')


        self.label = Label(master, text="User Registration.", bg="light pink").place(x=150,y=10)
        self.label = Label(master, text=" Name", bg="light pink").place(x=10,y=40)
        self.label = Label(master, text="Email Id", bg="light pink").place(x=10,y=70)
        self.label = Label(master, text="Contact Number", bg="light pink").place(x=10,y=110)
        self.label = Label(master, text="DOB", bg="light pink").place(x=10,y=140)
        self.label = Label(master, text="Password", bg="light pink").place(x=10,y=170)
        #self.label = Label(master, text="", bg="light pink").grid(row=8, column=0)
        Entry(master, textvariable=self.name).place(x=150,y=40)
        Entry(master, textvariable=self.email).place(x=150,y=70)
        Entry(master, textvariable=self.contact).place(x=150,y=110)
        dob_day.place(x=150,y=140)
        dob_month.place(x=210,y=140)
        dob_year.place(x=300,y=140)
        Entry(master, textvariable=self.password).place(x=150,y=170)
        self.submit_button = Button(master, text="Submit", bg="light green", command=self.submit_data).place(x=150,y=200)
        self.close_button = Button(master, text="Close", bg="light blue", command=master.quit).place(x=250,y=200)

    def submit_data(self):

        global reg_user
        name = self.name.get()
        email = self.email.get()
        contact = self.contact.get()
        dob_year = self.dob_year.get()
        dob_month = self.dob_month.get()
        dob_day = self.dob_day.get()
        print(dob_month)

        mth = ''
        if(dob_month=='jan'):
            mth = '1'
        elif(dob_month=='feb'):
            mth = '2'
        elif (dob_month == 'mar'):
            mth = '3'
        elif (dob_month == 'apr'):
            mth = '4'
        elif (dob_month == 'may'):
            mth = '5'
        elif (dob_month == 'jun'):
            mth = '6'
        elif (dob_month == 'jul'):
            mth = '7'
        elif (dob_month == 'aug'):
            mth = '8'
        elif (dob_month == 'sept'):
            mth = '9'
        elif (dob_month == 'oct'):
            mth = '10'
        elif (dob_month == 'nov'):
            mth = '11'
        elif (dob_month == 'dec'):
            mth = '12'
        date_str = mth+'-'+dob_day+'-'+dob_year
        print(date_str)
        date_object = datetime.strptime(date_str, '%m-%d-%Y').date()
        print(type(date_object))
        print(date_object)
        password = self.password.get()
        if(name and email and contact and date_object and password):
            print("test")
            print(name)
            print(email)
            print(contact)
            print(date_object)
            print(password)
            sql = "INSERT INTO users(uname,email,dob,contact,password) VALUES (%s,%s,%s,%s,%s)"
            val = (name, email, date_object,contact,password)
            success =  insert_data(sql, val)
            db.setEmail(email)
            if(success == 1):
                sql2 = "SELECT * FROM users where email='" + email + "' and password='" + password + "'"
                reg_user = getUsers(sql2)
                print("current registered id is ")
                print(reg_user)
            #os.system('python3 RegisterPeriod.py')
            messagebox.showinfo("Registration Message", "Successfully Registered ")
            self.master.destroy()

        else:
            print("Error Occured")
            messagebox.showerror("User Registration", "Some Error Occured Please Try Again")



root = Tk()
my_gui = RegistrationPage(root)
root.mainloop()
