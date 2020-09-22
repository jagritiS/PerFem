import os
from tkinter import Tk, Label, Button, Entry, StringVar, IntVar, messagebox
from tkinter.ttk import Combobox
from db import insert_data
from RegistrationPage import reg_user

class RP:
    def __init__(self, master):
        self.master = master
        master.title("Perfem")
        master.geometry('500x500')
        master.configure(background="light pink")

        self.cl = StringVar()
        self.pl = StringVar()


        cl =Combobox(master, width=27, textvariable=self.cl)
        pl =Combobox(master, width=27, textvariable=self.pl)


        # Adding combobox drop down list
        cl['values'] = (' 1',' 2',' 3',' 4',' 5',' 6',' 7',' 8',' 9',' 10',' 11',
						' 12',' 13',' 14',' 15',' 16',' 17',' 18',' 19',' 20',
						' 21',' 22',' 23',' 24','25','26','27','28','29','30','31')
        cl.grid(column=1, row=2)
        # Adding combobox drop down list
        pl['values'] = (' 1',' 2',' 3',' 4',' 5',' 6',' 7')
        pl.grid(column=1, row=4)

        self.label = Label(master, text=" Period Details", bg="light pink").grid(row=1, column=0, ipadx="10")
        self.label = Label(master, text="Cycle Length", bg="light pink").grid(row=2, column=0, ipadx="10")
        self.label = Label(master, text="Period Length", bg="light pink").grid(row=4, column=0, ipadx="10")

        self.submit_button = Button(master, text="Submit", bg="light green", command=self.submit_data).grid(row=8,
                                                                                                            column=0)
        self.close_button = Button(master, text="Close", bg="light blue", command=master.quit).grid(row=8, column=2)

    def submit_data(self):
        cl = self.cl.get()
        pl = self.pl.get()

        print("check 1111========================")
        sql = "INSERT INTO period_details(user_id,cycle_length,period_length) VALUES (%s,%s,%s)"

        val = (reg_user,cl,pl)
        insert_data(sql, val)
        self.master.destroy()
        os.system('python3 HomePage.py')
        messagebox.showinfo("Details", "Details Added Successfully")

root = Tk()
my_gui = RP(root)
root.mainloop()
