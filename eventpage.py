#Import the required libraries and extensions.
import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import webbrowser
import sqlite3
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

#For fetching the assets in use.
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"D:\Documents\Academics\CT\TKDesigner Projects\ePage1\build\assets\frame0")
ASSETS_PATH2 = OUTPUT_PATH / Path(r"D:\Documents\Academics\CT\TKDesigner Projects\ePage2\build\assets\frame0")
ASSETS_PATH3 = OUTPUT_PATH / Path(r"D:\Documents\Academics\CT\TKDesigner Projects\ePage3\build\assets\frame0")
ASSETS_PATH4 = OUTPUT_PATH / Path(r"D:\Documents\Academics\CT\TKDesigner Projects\ePage4\build\assets\frame0")
ASSETS_PATH5 = OUTPUT_PATH / Path(r"D:\Documents\Academics\CT\TKDesigner Projects\ePage5\build\assets\frame0") 
def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)
def relative_to_assets2(path: str) -> Path:
    return ASSETS_PATH2 / Path(path)
def relative_to_assets3(path: str) -> Path:
    return ASSETS_PATH3 / Path(path)
def relative_to_assets4(path: str) -> Path:
    return ASSETS_PATH4 / Path(path)
def relative_to_assets5(path: str) -> Path:
    return ASSETS_PATH5 / Path(path)

#Event Database Creation
with sqlite3.connect("Events.db")as db:
	cursor=db.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS events(EventID integer PRIMARY KEY AUTOINCREMENT, EventName string NOT NULL, Date date NOT NULL, Time time NOT NULL, Venue string NOT NULL)""")

root = tk.Tk()
root.title('Event Page')

#Update Result Box
def update(Results):
	#Clear the Result Box
	srBox.delete(0, END)

	#Add Data to Result Box
	for item in Results:
		srBox.insert(END, item)

# Update Search Box with ResultBox clicked
def fillout(e):
	# Delete anything in the Search box
	sBox.delete(0, END)

	#Add clicked result into Search Box
	sBox.insert(0, srBox.get(ACTIVE))

#Create function to check Search vs ResultBox
def check(e):
	#Grab what was typed
	typed = sBox.get()
	if typed == '':
		Results = ename
	else:
		Results = []
		for item in ename:
			if typed.lower() in item.lower():
				Results.append(item)
	
	#Update ResultBox with selected items
	update(Results)

#LEFT Frame Buttons function(EXCLUDING SEARCH)
#Register Event Button
def eRedirect(url):
	webbrowser.open_new_tab(url)

#Define a redirect function for the event banners
def redirect1(url):
	webbrowser.open_new_tab(url)
	elabel1.config(text="Redirecting to event website...")
def redirect2(url):
	webbrowser.open_new_tab(url)
	elabel2.config(text="Redirecting to event website...")
def redirect3(url):
	webbrowser.open_new_tab(url)
	elabel3.config(text="Redirecting to event website...")

def showevents():
    e_text = sBox.get()
    if e_text=="WCIT 2022"  or e_text=="wcit 2022":
        epage1 = Toplevel(root)
        epage1.geometry("690x690"),epage1.title('WCIT 2022')
        epage1.configure(bg = "#FFFFFF")
        global image_image_1, image_image_2,canvas
        canvas = Canvas(epage1,bg = "#FFFFFF",height = 690,width = 690,
        bd = 0,highlightthickness = 0,relief = "ridge")
        canvas.place(x = 0, y = 0)
        image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
        image_1 = canvas.create_image(345.0,345.0,image=image_image_1)
        image_image_2 = PhotoImage(file=relative_to_assets("image_2.png"))
        image_2 = canvas.create_image(345.0,182.0,image=image_image_2)
        canvas.create_text(57,60,anchor="nw",text="World Congress on Innovation & Technology 2022\n",fill="#FFFFFF",font=("InriaSans Regular", 27 * -1))
        canvas.create_text(45,270,anchor="nw",
        text="Event Date: 13 Sept 2022 - 15 Sept 2022\
        \nEvent Time: 8:00 am - 6:00 pm\
        \nVenue: SETIA SPICE Convention Centre\
        \nFor more info, visit: https://wcit2022.com/wcit/home\
        \n\nWCIT 2022 Malaysia is the 26th edition of World Congress on\
        \nInnovation & Technology and it is returning to Malaysia this September.\
        \nAs one of the world's largest and most prestigious ICT events,\
        \nit features discussions with visionaries, captains of industry,\
        \ngovernment leaders, innovators and academics from over 80 countries.\
        \nCommonly referred to as the 'Olympics of the World’s Information\
        \nTechnology Industry', WCIT 2022 MALAYSIA sets out to be the gateway\
        \nto Southeast Asia; connecting and transforming the world via\
        \n a definitive global event of technology businesses.",
        fill="#FFFFFF",
        font=("Helvetica", 20 * -1))

    elif e_text=="Business Networking Event" or e_text=="business networking event":
        epage2 = Toplevel(root)
        epage2.geometry("690x690"),epage2.title('Business Networking Event')
        epage2.configure(bg = "#FFFFFF")
        global image_image_3, image_image_4,canvas2
        canvas2 = Canvas(epage2,bg = "#FFFFFF",height = 690,width = 690,
        bd = 0,highlightthickness = 0,relief = "ridge")
        canvas2.place(x = 0, y = 0)
        image_image_3 = PhotoImage(file=relative_to_assets2("image_3.png"))
        image_3 = canvas2.create_image(345.0,345.0,image=image_image_3)
        image_image_4 = PhotoImage(file=relative_to_assets2("image_4.png"))
        image_4 = canvas2.create_image(345.0,196.0,image=image_image_4)
        canvas2.create_text(44.0,30.0,anchor="nw",text="Business Networking Event with \nProfessional Network Connections",fill="#000000",font=("Iceberg Regular", 27 * -1))
        canvas2.create_text(30.0,310.0,anchor="nw",
        text="Event Date: 20/10/22\
        \nEvent Time: 2:00 pm - 4:00 pm\
        \nVenue: LR 405\
        \nFor more info, visit: https://pnconnections.org\
        \n\nJoin with the one and only Professional Network Connections to\
        \ndiscuss about the future of business in INTI International College Penang.\
        \nYou will be able to meet the best of bests in the industry and\
        \nthey will be here to guide and give you some solid advices that will\
        \nassist you in the near future or you could ask them for an internship\
        \nto learn what they can provide after graduation.\n\n",
        fill="#000000",font=("Helvetica", 20 * -1))

    elif e_text=="13th Annual Fun Run" or e_text=="13th annual fun run":
        epage3 = Toplevel(root)
        epage3.geometry("690x690"),epage3.title('13th Annual Fun Run')
        epage3.configure(bg = "#FFFFFF")
        global image_image_5, image_image_6,canvas3
        canvas3 = Canvas(epage3,bg = "#FFFFFF",height = 690,width = 690,
        bd = 0,highlightthickness = 0,relief = "ridge")
        canvas3.place(x = 0, y = 0)
        image_image_5 = PhotoImage(file=relative_to_assets3("image_5.png"))
        image_5 = canvas3.create_image(345.0,345.0,image=image_image_5)
        image_image_6 = PhotoImage(file=relative_to_assets3("image_6.png"))
        image_6 = canvas3.create_image(345.0,207.0,image=image_image_6)
        canvas3.create_text(180.0,23.0,anchor="nw",text="13th Annual Fun Run",fill="#000000",font=("Helvetica", 32 * -1))
        canvas3.create_text(30.0,355.0,anchor="nw",
        text="Event Date: 1/11/22\
        \nEvent Time: 8:30 am - 11:30 am\
        \nVenue: Gurney Plaza\
        \nFor more info, visit: https://www.jomrun.com/events\
        \n\nJoin the 13th annual Fun Run and win prizes along getting to run by\
        \nyour best buddies side. Participants will be getting a free T-shirt\
        \nfrom the officials just by registering, those who finish the run will be\
        \nentitled to a medal and certificate, and for those who finish in the certain\
        \nsaid time limit will have  a chance to win  up to RM3000 worth of prizes\
        \nin the Lucky Draw segment after the run.\n\n\n",
        fill="#000000",font=("Helvetica", 20 * -1))

    elif e_text=="IICP Hackathon 2023" or e_text=="iicp hackathon 2023":
        epage4 = Toplevel(root)
        epage4.geometry("690x690"),epage4.title('IICP Hackathon 2023')
        epage4.configure(bg = "#FFFFFF")
        global image_image_7, image_image_8,canvas4
        canvas4 = Canvas(epage4,bg = "#FFFFFF",height = 690,width = 690,
        bd = 0,highlightthickness = 0,relief = "ridge")
        canvas4.place(x = 0, y = 0)
        image_image_7 = PhotoImage(file=relative_to_assets4("image_7.png"))
        image_7 = canvas4.create_image(345.0,345.0,image=image_image_7)
        image_image_8 = PhotoImage(file=relative_to_assets4("image_8.png"))
        image_8 = canvas4.create_image(344.0,210.0,image=image_image_8)
        canvas4.create_text(110.0,35.0,anchor="nw",text="INTIMA Hackathon 2023",fill="#FEFDFF",font=("Inter", 40 * -1))
        canvas4.create_text(30.0,345.0,anchor="nw",
        text="Event Date: 20/2/23\
        \nEvent Time: 1:00 pm - 4:00 pm\
        \nVenue: LR503\
        \nFor more info, visit: https://www.facebook.com/IICP.INTIMA/\
        \n\nEver dream of being a hacker? Well, you are in luck, join the INTIMA\
        \nHackathon in LR503 on the 20th of February to stretch your hacking skills\
        \nand compete with fellow peers to earn prizes. Stay tuned for more info\
        \nand check INTIMA’s socials for further updates.",
        fill="#FFFFFF",font=("Inter", 20 * -1))

    elif e_text=="IICP Nerf WAR" or e_text==" IICP Nerf WAR" or e_text=="iicp nerf war" or e_text==" iicp nerf war":
        epage5 = Toplevel(root)
        epage5.geometry("690x690"),epage5.title('IICP Nerf WAR')
        epage5.configure(bg = "#FFFFFF")
        global image_image_9, image_image_10,canvas5
        canvas5 = Canvas(epage5,bg = "#FFFFFF",height = 690,width = 690,
        bd = 0,highlightthickness = 0,relief = "ridge")
        canvas5.place(x = 0, y = 0)
        image_image_9 = PhotoImage(file=relative_to_assets5("image_9.png"))
        image_9 = canvas5.create_image(345.0,345.0,image=image_image_9)
        image_image_10 = PhotoImage(file=relative_to_assets5("image_10.png"))
        image_10 = canvas5.create_image(345.0,200.0,image=image_image_10)
        canvas5.create_text(46.0,42.0,anchor="nw",text="IICP Nerf Club Event: Nerf WAR",fill="#F9FF00",font=("Inter", 40 * -1))
        canvas5.create_text(30.0,315.0,anchor="nw",
        text="Event Date: 3/3/23\
        \nEvent Time: 3:00 pm - 6:00 pm\
        \nVenue: LR601\
        \nFor more info, visit:https://ms-my.facebook.com/IICP.INTIMA\
        \n\nIs your trigger finger itching for some nerf battle? Well, you are in luck\
        \nbecause the IICP Nerf Club is helding an event on the 3th of March 2023\
        \nin INTI International College Penang. Please remember to prepare\
        \nyour own respective blasters and additional equipments(ammunition).\
        \nStay tuned for more info and check INTIMA’s socials for further updates.",
        fill="#F9FF00",font=("Inter", 20 * -1))

#Main Frame
mframe= LabelFrame(root,bg="grey")
mframe.grid(column=0,row=0,sticky=tk.NSEW)

#Grid Configuration
mframe.columnconfigure(0, weight=1)
mframe.columnconfigure(1, weight=1)
mframe.columnconfigure(2, weight=1)

#Left Frame
lframe= LabelFrame(mframe,text="Registration & Navigation",font=("Arial",14),fg="cyan",bg="navy")
lframe.grid(column=0,row=0,sticky=tk.NSEW)
#Center Frame
cframe= LabelFrame(mframe,text="Current Events",font=("Arial",14),fg="black",bg="#BFC9CA")
cframe.grid(column=1,row=0,sticky=tk.NSEW)
#Right Frame
rframe= LabelFrame(mframe,text="Events & Announcements",font=("Arial",14),fg="cyan",bg="navy")
rframe.grid(column=2,row=0,sticky=tk.NSEW)

#LEFT FRAME SECTION
#Search Box
sBox = Entry(lframe, font=("Arial", 12),width=30)
sBox.pack(anchor=W)

#Search Results Box
srBox = Listbox(lframe, width=40)
srBox.pack(anchor=W,pady=10)

#Add Data into Results Box
cursor.execute("SELECT *,oid FROM events")
edata = cursor.fetchall()
rcount = 0
ename=[]
for i in edata:
    ename.insert(0,str(i[1]))
    rcount += 1
update(ename)

#Create a binding on Results Box on click
srBox.bind("<<ListboxSelect>>", fillout)

#Create a binding on the Search Box
sBox.bind("<KeyRelease>", check)

#Search Event Button
sButton = Button(lframe, text="Search",font=("Arial",14),bg="cyan", command = showevents)
sButton.pack(anchor=W,pady=15)

#Register into Event Button
rButton = Button(lframe, text="Register into Events",font=("Arial",14),bg="magenta", command = eRedirect)
rButton.bind("<Button-1>", lambda e:
eRedirect("https://docs.google.com/forms/d/1beZALmEZ4t9as3RgkyYUCZQMwOkOjGiYm2lsglh6cCM/edit"))
rButton.pack(anchor=W,pady=20)

#Navigation Buttons
hpButton = Button(lframe, text="Homepage",font=("Arial",14),bg="red",width=10)
cldrButton = Button(lframe, text="Calendar",font=("Arial",14),bg="yellow",width=10)
lgtButton = Button(lframe,text="Logout",font=("Arial",14),bg="green",width=10)
hpButton.pack(anchor=W,pady=15)
cldrButton.pack(anchor=W,pady=15)
lgtButton.pack(anchor=W,pady=15)

#CENTER FRAME SECTION
#Current Events Label
celbl = Label(cframe,text = "Get the latest updates from the event websites by clicking the banners below.", font=("Arial",12),fg="black",bg="#BFC9CA")
celbl.pack(anchor=NW,pady=5)

#Event Button 1
image1 = Image.open("D:/Pictures/Snips/ExampleButtonImage1.png")
img1 = image1.resize((600,100))
Button1 = ImageTk.PhotoImage(img1)
eButton1 = Button(cframe, image=Button1, command=redirect1, borderwidth=0)
eButton1.pack(pady=20)
eButton1.bind("<Button-1>", lambda e:
redirect1("https://wcit2022.com/wcit/home"))
elabel1 = Label(cframe,text='',bg="#BFC9CA")
elabel1.place(x=0,y=156)

#Event Button 2
image2 = Image.open("D:/Pictures/Snips/ExampleButtonImage2.png")
img2 = image2.resize((600,100))
Button2 = ImageTk.PhotoImage(img2)
eButton2 = Button(cframe, image=Button2, command=redirect2, borderwidth=0)
eButton2.pack(pady=90)
eButton2.bind("<Button-1>", lambda e:
redirect2("https://pnconnections.org"))
elabel2 = Label(cframe,text='',bg="#BFC9CA")
elabel2.place(x=0,y=377)

#Event Button 3
image3 = Image.open("D:/Pictures/Snips/ExampleButtonImage3.png")
img3 = image3.resize((600,100))
Button3 = ImageTk.PhotoImage(img3)
eButton3 = Button(cframe, image=Button3, command=redirect3, borderwidth=0)
eButton3.pack(pady=50)
eButton3.bind("<Button-1>", lambda e:
redirect3("https://www.jomrun.com/events"))
elabel3 = Label(cframe,text='',bg="#BFC9CA")
elabel3.place(x=0,y=620)

#RIGHT FRAME SECTION
#Event Table
s = ttk.Style()
s.configure('Treeview', rowheight=30)
etb = ttk.Treeview(rframe)
#Define Columns
etb['columns'] =("Event","Date","Time","Place")
#Format Columns
etb.column("#0", width=0, stretch=NO)
etb.column("Event", anchor=W, width=130)
etb.column("Date", anchor=W, width=105)
etb.column("Time", anchor=W, width=110)
etb.column("Place", anchor=W, width=150)
#Create Headings
etb.heading("#0", text="No",anchor=W)
etb.heading("Event", text="Event", anchor=CENTER)
etb.heading("Date", text="Date", anchor=CENTER)
etb.heading("Time", text="Time", anchor=CENTER)
etb.heading("Place", text="Venue", anchor=CENTER)
#Fetch Data
ecount = 0
for i in edata:
    etb.insert(parent='', index='end', iid=ecount, text="", values=(str(i[1]), str(i[2]), str(i[3]), str(i[4])))
    ecount += 1
#Pack to the screen
etb.pack(anchor=N)

#Announcement Table
atb = ttk.Treeview(rframe)
#Define Columns
atb['columns'] =("Events","Announcements")
#Format Columns
atb.column("#0", width=0, stretch=NO)
atb.column("Events", anchor=W, width=120)
atb.column("Announcements", anchor=W, width=360)
#Create Headings
atb.heading("#0", text="No",anchor=W)
atb.heading("Events", text="Related Events", anchor=W)
atb.heading("Announcements", text="Announcement Details", anchor=CENTER)
#Add Announcements
Alist = [
	["WCIT 2022","Shuttle bus service is not available. Prepare your own transports."],
	["13th Annual Fun Run","Event postponed due to rainy weather." "\n" "Check event website for further updates."],
    ["Nerf Club Event","Please prepare your own equipment."]
]
acount=0
for arecord in Alist:
	atb.insert(parent='', index='end', iid=acount, text="", values=(arecord[0], arecord[1]))
	acount += 1
#Pack to the screen
atb.pack(pady=60)

root.mainloop()