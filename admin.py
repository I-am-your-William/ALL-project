import tkinter as tk
from tkinter import *
import PIL 
from PIL import Image,ImageTk
import sqlite3
import turtle
from tkinter import filedialog
from tkinter.filedialog import askopenfile

with sqlite3.connect("LOL.db")as db:
    c=db.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS events(id integer PRIMARY KEY AUTOINCREMENT,Image text NOT NULL , Events_date integer NOT NULL , Events_detail_link text NOT NULL)""")

def add():
    Image_path=image.get()
    Eventsd=date.get()
    Eventslink=link.get()
    
    #
    if Image_path=="" or Eventsd=="" or Eventslink=="":
        error["text"] = "Error: Zero entry"
    else:
        error["text"]="Added new events"
        c.execute("INSERT INTO events(Image , Events_date ,Events_detail_link )VALUES(?,?,?,)",(Image_path,Eventsd,Eventslink))
        result1 = c.fetchone()
        db.commit()









root=Tk()
root.geometry("300x400")
root.config(bg="#11FFF1")
root.title("Admin page")

error=Message(text="",width=180)
error.place(x=30 , y=20)
error.config(padx=0)
#
label1=Label(text="Enter Image Path")
label1.place(x=60 , y=40)
label1.config(bg='cyan', padx =0)
#
l1 = tk.Label(root,text='Add Student Data with Photo',width=30,font="Arial")  
l1.grid(row=1,column=1)
b1 = tk.Button(root, text='Upload File', 
   width=20,command = lambda:upload_file())
b1.grid(row=30,column=20) 

def upload_file():
    global img
    f_types = [('Jpg Files', '*.jpg')]
    filename = filedialog.askopenfilename(filetypes=f_types)
    img = ImageTk.PhotoImage(file=filename)
    b2 =tk.Button(root,image=img) # using Button 
    b2.grid(row=30,column=30)
#
image = Entry(text="")
image.place(x=250, y=40 , width=200,height=25)
#
label2 = Label(text = "Image date")
label2.place(x = 60 , y=80)
label2.config(bg='cyan',padx=0)
#
date = (Entry(text="" ))
date.place(x=250 , y=80 ,width = 200 , height =25)
#
label3 = Label(text="Please enter the link of events")
label3.place(x=60,y=120)
label3.config(bg='darkgrey',padx=0)
#
link=Entry(text="")
link.place(x=250,y=120,width=200,height=25)

button1=Button(text="enter" , font="Arial" , command=add)
button1.place(x=250,y=150 , width=100 , height=25)



root.mainloop()