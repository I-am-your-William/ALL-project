#Import the required libraries
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import webbrowser

#Window
root=Tk()
root.geometry("1200x1000")
root.title("Homepage")

def event():
    root.destroy()
    import eventpage
    
def back():
    root.destroy()
    import Login
    exit()
def Calendar():
    root.destroy()
    import Calender_reminder_revised
    
def CttH(url):
	webbrowser.open_new_tab(url)

mainbg = Image.open("D:/Pictures/pStuff/silver polynomial bg.jpg")
img1 = mainbg.resize((1200,1000))
image1 = ImageTk.PhotoImage(img1)
canvas = Canvas(root,width=1200, height=1000)
canvas.pack(fill="both", expand=True)
canvas.create_image(0,0, image=image1, anchor=NW)

#INTI Logo
logo = Image.open("D:/Pictures/pStuff/INTI Logo.png")
img2 = logo.resize((500,100))
image2 = ImageTk.PhotoImage(img2)
canvas.create_image(0,0,image=image2,anchor=NW)

#Welcome Message
canvas.create_text(400,150, text="Welcome to the Event Reporting System!",font=("Century Gothic",30),fill="black")

#Profile Label
pflelabel = Label(root,text="Hi,User1234!",font=("Century Gothic",18),bg="grey",borderwidth=0)
button1_window = canvas.create_window(700,15,anchor=NW,window=pflelabel)

#Navigation Buttons
#Log Out Button
lgtButton = Button(root,text="Logout",font=("Century Gothic",20),bg="red",borderwidth=1,command= back)
button2_window = canvas.create_window(1080,10,anchor=NW,window=lgtButton)
#Event Button
button3 = Image.open("D:/Pictures/pStuff/event icon(b).png")
img3 = button3.resize((300,200))
nb1 = ImageTk.PhotoImage(img3)
EventButton = Button(root, image=nb1, borderwidth=0,command=event)
button3_window = canvas.create_window(150,230,anchor=NW,window=EventButton)
#Calendar Button
button4 = Image.open("D:/Pictures/pStuff/calendar icon(b).png")
img4 = button4.resize((300,200))
nb2 = ImageTk.PhotoImage(img4)
CldrButton = Button(root, image=nb2, borderwidth=0,command=Calendar)
button4_window = canvas.create_window(720,230,anchor=NW,window=CldrButton)
#Contact Support Button
button5 = Image.open("D:/Pictures/pStuff/support.png")
img5 = button5.resize((200,200))
nb3 = ImageTk.PhotoImage(img5)
CttHpButton = Button(root, image=nb3, borderwidth=0, command=CttH)
CttHpButton.bind("<Button-1>", lambda e:
CttH("https://forms.gle/pg5zMWGk1MtjsDNU7"))
button5_window = canvas.create_window(480,530,anchor=NW,window=CttHpButton)
canvas.create_text(580,750, text="Contact Support",font=("Century Gothic",20),fill="black")

root.mainloop()