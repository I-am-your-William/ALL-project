from tkinter import * 
import sqlite3
from turtle import bgcolor, color


with sqlite3.connect("registeration.db") as db:
    cursor=db.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS registers(id integer PRIMARY KEY AUTOINCREMENT, newUsername text NOT NULL,newEmailAdress text NOT NULL ,newPhoneNumber integer NOT NULL , newpassword text NOT NULL,newProgram text NOT NULL , newAge integer NOT NULL   )""")

def add_new_register():
    
    newUsername = username.get()
    newPassword = password.get()
    newEmailAdress = email.get()
    newPhoneNumber = phonenumber.get()
    newAge = age.get()
    newProgram = programmecode.get()
    if newUsername == "":
        error["text"] = "Error: Please enter user Id"
    else:
        cursor.execute("SELECT COUNT(*) from registers WHERE newUsername='" + newUsername + "'")
        result = cursor.fetchone()

        if int(result[0])> 0:
            error["text"] = " Error: Username already exist"
    
        
            
        else:
            error["text"]="Added new user"
            cursor.execute("INSERT INTO registers(newUsername,newpassword,newEmailAdress,newPhoneNumber,newAge,newProgram)VALUES(?,?,?,?,?,?)",(newUsername,newPassword, newEmailAdress,newPhoneNumber,newAge,newProgram))
            result1 = cursor.fetchone()
            db.commit()


   


def nextPage():
    windows.destroy()
    import Login
    











#
windows=Tk()
windows.geometry("600x500")
windows.config(bg="darkgrey")
windows.title("Register page")

#
error=Message(text="",width=180)
error.place(x=30 , y=20)
error.config(padx=0)
#
label1=Label(text="Enter Username")
label1.place(x=60 , y=40)
label1.config(bg='darkgrey', padx =0)
#
username = Entry(text="")
username.place(x=200, y=40 , width=200,height=25)
#
label2 = Label(text = "Enter password :")
label2.place(x = 60 , y=80)
label2.config(bg='darkgrey',padx=0)
#
password = Entry(text="" , show="*")
password.place(x=200 , y=80 ,width = 200 , height =25)
#
label3 = Label(text="Enter email:")
label3.place(x=60,y=120)
label3.config(bg='darkgrey',padx=0)
#
email=Entry(text="")
email.place(x=200,y=120,width=200,height=25)
#
label4=Label(text="Enter phone number")
label4.place(x=60,y=160)
label4.config(bg='darkgrey',padx=0)
#
phonenumber=Entry(text="")
phonenumber.place(x=200,y=160,width=200,height=25)
#
label5=Label(text="Enter age:")
label5.place(x=60,y=200)
label5.config(bg="darkgrey",padx=0)
#
age=Entry(text="")
age.place(x=200,y=200,width=200,height=25)
#
label6=Label(text="Enter programme code:")
label6.place(x=60,y=240)
label6.config(bg="darkgrey",padx=0)
#
programmecode=Entry(text="")
programmecode.place(x=200,y=240, width=200,height=25)
#
button=Button(text="SUBMIT" , command=add_new_register)
button.place(x=150,y=280,width=100,height=25)
button.config(bg="darkgrey")
#
button=Button(text="LOGIN PAGE", command =nextPage)
button.place(x=280,y=280,width=100,height=25)
button.config(bg="darkgrey")


windows.mainloop()
