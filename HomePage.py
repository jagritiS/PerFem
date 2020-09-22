import os
from tkinter import Tk, Label, Button, Entry, Image


class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        master.title("Perfem")
        master.geometry('500x500')
        master.configure(background="light pink")
        self.label = Label(master, text="Welcome to Perfem. The only app to track your period life.",bg="teal").place(x=55,y=5)
        self.greet_button = Button(master, text="Sign Up", bg="teal",command=self.registrationPage).place(x=360, y=300)
        self.greet_button = Button(master, text="Login", bg="teal",command=self.loginpage).place(x=360, y=350)
        self.close_button = Button(master, text="Close",  bg="teal",command=master.quit).place(x = 360, y=400)

    def registrationPage(self):
        print("Greetings!")
        self.master.destroy()
        os.system('python3 RegisterPeriod.py')
    def loginpage(self):
        print("Greetings!")
        self.master.destroy()
        os.system('python3 pcal.py')

root = Tk()
my_gui = MyFirstGUI(root)
root.mainloop()