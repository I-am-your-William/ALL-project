from tkinter import *
import sqlite3 
from tkinter import messagebox
with sqlite3.connect("registeration.db") as db:
    cursor=db.cursor()

cursor.execute(""" DELETE FROM registers WHERE newUsername="" """)

def add_new_user():

    newUsername = username.get()
    newPassword = password.get()

    cursor.execute("SELECT COUNT(*) from registers WHERE newUsername='" + newUsername + "' AND newPassword='" + newPassword +"'")
    result = cursor.fetchone()
    
    if newUsername=="Admin" and newPassword=="Admin":
        root.destroy()
        import admin
        exit()
    
        

    if int(result[0])> 0:
            error["text"]="Sucessful Login"
            db.commit()
            root.destroy()
            import Homepage2
    else:
        error["text"] = "Register First"
        messagebox.showerror("Invalid username and password","Invalid username and password")
       



def Register():
    root.destroy()
    import Registeration






    


root=Tk()
root.geometry("450x180")
root.title("Login page")
root.iconbitmap("C:/Users/MyAcer/Desktop/INTI/2693560.ico")
#
error = Message(text="",width =160)
error.place(x=30,y=10)
error.config(padx=0)
#
label1 = Label(text = "Enter username")
label1.place(x = 30,y = 40)
label1.config(bg='yellow' ,padx=0)
#
username = Entry(text="")
username.place(x=150, y=40 , width=200,height=25)
#
label2 = Label(text = "Enter passowrd :")
label2.place(x = 30 , y=80)
label2.config(bg='yellow',padx=0)
#
password = Entry(text="" , show="x")
password.place(x=150 , y=80 ,width = 200 , height =25)
#
button=Button(text= "LOGIN" , command = add_new_user, )
button.place(x=150 , y=120 , width = 90 , height = 35)
button=Button(text="Register",command = Register,)
button.place(x=250, y=120 , width = 90 , height = 35)






root.mainloop()
