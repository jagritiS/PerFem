import os
from tkinter import *

from db import insert_data

master = Tk()
master.title("PerFem User Symptoms ")
master.geometry('500x500')
master.configure(background = "light pink")


def var_states():
   print("Abdominal or pelvic cramping: %d,"
         "\nLower back pain: %d,\
         nBloating and sore breasts: %d,"
         "\nFood cravings: %d,"
         "\nMood swings and irritability: %d,"
         "\nHeadache: %d,\nFatigue: %d,\nAcne: %d,\nItchiness: %d,\nWeight gain: %d"
         % (var1.get(), var2.get(), var3.get(), var4.get(), var5.get(),
            var6.get(), var7.get(), var8.get(), var9.get(), var10.get()))
   result = "Headache"
   sql2 = "INSERT INTO symptoms(symp) VALUES (%s)"
   val = (result)
   vals = insert_data(sql2, val)
   if (vals == 1):
       print("success")
   else:
       print("not success")


def back_btn():
    print("back")
    master.destroy()
    os.system('python3 pcal.py')
Label(master, text="Your symptoms:",bg="light pink").grid(row=0, sticky=W)
var1 = IntVar()
Checkbutton(master, text="Abdominal or pelvic cramping", variable=var1,bg="light pink").grid(row=1, sticky=W)
var2 = IntVar()
Checkbutton(master, text="Lower back pain", variable=var2,bg="light pink").grid(row=2, sticky=W)
var3 = IntVar()
Checkbutton(master, text="Bloating and sore breasts", variable=var3,bg="light pink").grid(row=3, sticky=W)
var4 = IntVar()
Checkbutton(master, text="Food cravings", variable=var4,bg="light pink").grid(row=4, sticky=W)
var5 = IntVar()
Checkbutton(master, text="Mood swings and irritability", variable=var5,bg="light pink").grid(row=5, sticky=W)
var6 = IntVar()
Checkbutton(master, text="Headache", variable=var6,bg="light pink").grid(row=6, sticky=W)
var7 = IntVar()
Checkbutton(master, text="Fatigue", variable=var7,bg="light pink").grid(row=7, sticky=W)
var8 = IntVar()
Checkbutton(master, text="Acne", variable=var8,bg="light pink").grid(row=8, sticky=W)
var9 = IntVar()
Checkbutton(master, text="Itchiness", variable=var9,bg="light pink").grid(row=9, sticky=W)
var10 = IntVar()
Checkbutton(master, text="Weight gain", variable=var10,bg="light pink").grid(row=10, sticky=W)
Button(master, text='Quit', command=master.quit,bg="light green").grid(row=11,column=3, sticky=W, pady=10)
Button(master, text='Save', command=var_states,bg="light blue").grid(row=11,column=2, sticky=W, pady=10)
Button(master, text='Back', command=back_btn,bg="light yellow").grid(row=11,column=1, sticky=W, pady=10)


mainloop()