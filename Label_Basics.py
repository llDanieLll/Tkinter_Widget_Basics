from tkinter import *
from tkinter import ttk

root = Tk()
label = ttk.Label(root, text = "Hello, Tkinter! ")
label.pack()

### Modify the text content by using the .config function ###
label.config (text = "Hello Daniel! ")
label.config (text = "Hello Daniel! It's been a while since we last met. Great to see you again!")

### if the string is too long for the window, you may use wraplength option to wrap it up ###
label.config(wraplength = 130)

label.config(justify = CENTER)
### justify option to justify the string to the CENTER , LEFT, RIGHT)###

label.config(foreground = "blue",background = "pink")
label.config(font = ("Courier",15,"bold"))
### change the string's color, background's color and font,size###

logo = PhotoImage(file = 'C:\\Users\\Daniel\'s PC\\AppData\\Local\\Programs\\Python\\Python36-32\\python_logo_small.png')
label.config(image = logo)
label.config(compound = "center")

label.img = logo
###store the image logo with the label in case of logo pic be removed, using label.img object to store it###
label.config(image = label.img)

root.geometry("300x300+800+300")
root.mainloop()
