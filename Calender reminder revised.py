from tkinter import *
from tkcalendar import Calendar
import sqlite3
from turtle import bgcolor, color

with sqlite3.connect("registeration.db") as db:
    cursor=db.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS reminder(id integer PRIMARY KEY AUTOINCREMENT, newSelectedDate text NOT NULL , newEventName integer NOT NULL   )""")

tkobj = Tk()

tkobj.geometry("500x600")
tkobj.title("Calendar reminder")

tkc = Calendar(tkobj,selectmode = "day",year=2022,month=1,date=1)

tkc.pack(pady=40)

def fetch_date():
    date.config(text = "Selected Date is: " + tkc.get_date())

def back():
    tkobj.destroy()
    import Homepage2
    exit()

but3= Button(tkobj , text = "Homepage" , command = back , bg= "cyan" , fg="black")

but3.pack()

but = Button(tkobj,text="Select Date",command=fetch_date, bg="black", fg='white')

but.pack()

date = Label(tkobj,text="",bg='black',fg='white')
date.pack(pady=20)

def add_new_reminder():
    
    newReminder = reminder.get()
    newDate = date.get() 

    return add_new_reminder()

label1=Label(text="Enter event/task")
label1.place(x=60 , y=350)
label1.config(bg='darkgrey', padx =0)

reminder=Entry(text="")
reminder.place(x=220,y=350,width=200,height=25)

label2=Label(text="Enter date (DD/MM/YYYY)")
label2.place(x=60 , y=390)
label2.config(bg='darkgrey', padx =0)

reminder=Entry(text="")
reminder.place(x=220,y=390,width=200,height=25)

button=Button(text="ADD REMINDER" , command=add_new_reminder)
button.place(x=200,y=480,width=100,height=25)
button.config(bg="darkgrey")

tkobj.mainloop()


