from tkinter import *
from tkinter import ttk

root = Tk()
frame = ttk.Frame(root)
frame.pack()
frame.config(height = 100, width = 200)
frame.config(relief = RIDGE)
### when using the relief function make sure value must be all captal letters ###
### relief function could be used to change the frame style ###
### frame style options: FLAT(No Border),RAISED,SUNKEN,SOLID,RIDGE,GROOVE ###

ttk.Button(frame, text = "Click Me").grid()
### when we added a button widget into the frame ###
### the frame size will automatically close down to fir the button widget###

### we can use the padding option to add the padding around the button widget ###
frame.config(padding = (30,15))

### another frame style called label frame ###
ttk.LabelFrame(root, height = 100, width =200,text = "My Frame").pack()


root.geometry("300x300+800+300")
root.mainloop()

