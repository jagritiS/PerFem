from LoginPage import current_user

import os
import datetime
from tkcalendar import Calendar, DateEntry
from db import get_p_data, insert_data
from models.data import data

try:
    import tkinter as tk
    from tkinter import ttk
except ImportError:
    import Tkinter as tk
    import ttk
def example1():
    print("=====================================================")
    print(current_user)
    print()
    def print_sel():
        print("check 1",cal.selection_get())
        print(cal.selection_get())
        save_p_date(cal.selection_get(),current_user)
        cal.see(datetime.date(year=2016, month=2, day=5))
    top = tk.Toplevel(root)
    today = datetime.date.today()
    #mindate = datetime.date(year=2020, month=1, day=1)
    mindate = today - datetime.timedelta(days=15)
    maxdate = today + datetime.timedelta(days=365)
    print(mindate, maxdate)

    cal = Calendar(top, font="Arial 14", selectmode='day', locale='en_US',
                   mindate=mindate, maxdate=maxdate, disabledforeground='red',
                   cursor="hand1", year=2020, month=1, day=1)
    cal.pack(fill="both", expand=True)
    ttk.Button(top, text="ok", command=print_sel).pack()

def setvalues(ep):
    print("value got from login ")
    print(ep)

def save_p_date(startDate,id):
    print(startDate)
    print("id from login to pcal is ")
    print(id)
    daystart = startDate
    #read data from period_details
    sql= "select * from period_details where user_id="+str(id)+""
    var = get_p_data(sql)
    cycle_length = var[2]
    period_legth = var[3]

    print("the data from period is ")
    print(var)

    dayend = startDate + datetime.timedelta(days=int(period_legth))
    next_period =dayend+ datetime.timedelta(days=int(cycle_length))

    sql2 = "INSERT INTO period_dates(user_id,start_date,end_date,next_date) VALUES (%s,%s,%s,%s)"
    val = (id,startDate,dayend,next_period)
    vals = insert_data(sql2, val)
    if(vals==1):
        print("success")
    else:
        print("not success")

def symptoms(userid):
    print("symptoms")
    root.destroy()
    os.system('python3 Symptoms.py')

def sendNotification(id):
    print("process to send notification ")
def mail(answer):
        # import smtplib for mailing and sql for DB
        import smtplib
        sender_email = 'perfem.aaj@gmail.com'
        rec_email = "jagriti.sunway@gmail.com"
        password = "12345aaj!@#"
        subject = 'Notification from Perfem'
        body = answer
        message = 'Subject:{}\n\n{}'.format(subject, body)
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, password)
        print('Login sucessful')
        server.sendmail(sender_email, rec_email, message)
        print('Email has been sent to ', rec_email)
        server.quit()

def notes(userid):
    print("symptoms")
    root.destroy()
    os.system('python3 Notes.py')

root = tk.Tk()
#top = tk.Toplevel(root)
root.title("Perfem")
root.geometry('500x500')
root.configure(background="light pink")
cal = Calendar(root, selectmode='none')
date = cal.datetime.today() + cal.timedelta(days=2)
#cal.calevent_create(date, 'Period Ends', 'message')
sql3 = "select * from period_dates where user_id="+"'"+str(current_user)+"'"
var3 = get_p_data(sql3)
print("data to show in calendar is ")
print(var3)
if(var3):
    edate = var3[3]
    sdate = var3[2]
    ndate = var3[4]
    today = datetime.date.today()
    dateDiff = ndate- today
    print("difference between dates is ")
    print(dateDiff)
    if(dateDiff<cal.timedelta(days=4)):
        print("less than 2 days ")
        sendNotification(id)
        findemail = "select * from users where id="+"'"+str(current_user)+"'"
        var4 = get_p_data(findemail)
        print("the data from users is ")
        print(var4)
        email = var4[2]
        message = "Hello, "+var4[1]+"\n Your Period Day is about to come please be alert."
        mail(message)
    else:
        print("more than 4 days ")
    print("data available")
    cal.calevent_create(sdate,'Period Starts','reminder')
    cal.calevent_create(edate,'Period ends','reminder')
    cal.calevent_create(ndate,'Next Period start','reminder')
    #cal.calevent_create(date, 'Period Ends', 'reminder')
    #cal.calevent_create(date + cal.timedelta(days=-2), 'Period Starts ', 'reminder')
    #cal.calevent_create(date + cal.timedelta(days=3), 'Message', 'message')
    cal.tag_config('reminder', background='red', foreground='yellow')
else:
    cal.calevent_create(date, 'Period Ends', 'reminder')
    cal.calevent_create(date + cal.timedelta(days=-2), 'Period Starts ', 'reminder')
    cal.calevent_create(date + cal.timedelta(days=3), 'Message', 'message')
    cal.tag_config('reminder', background='red', foreground='yellow')

cal.pack(fill="both", expand=True)
ttk.Label(root, text="Hover for dates.").pack()

ttk.Button(root, text='Calendar', command=example1).pack(padx=10, pady=10)
ttk.Button(root, text='Symptoms', command=symptoms).pack(padx=10, pady=10)
ttk.Button(root, text='Notes', command=notes).pack(padx=10, pady=10)


root.mainloop()
