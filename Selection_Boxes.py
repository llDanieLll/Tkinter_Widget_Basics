from tkinter import *
from tkinter import ttk

root = Tk()

month = StringVar()
combobox = ttk.Combobox(root, textvariable = month)
combobox.pack()
combobox.config(values =("Jan","Feb","Mar","Apr","May",
                      "Jun","Jul","Aug","Sep","Oct","Nov","Dec") )

#combobox.get()
### to get the variable in the combobox ###

#combobox.set("Dec")
#Combobox.set("Not a month")
### to set the variable in the combobox ###

year = StringVar()
spinbox = Spinbox(root, from_ = 1990, to = 2018, textvariable = year).pack()
#year.get()
### to the the value of the year string variable ###


root.geometry("300x300+800+300")
root.mainloop()
