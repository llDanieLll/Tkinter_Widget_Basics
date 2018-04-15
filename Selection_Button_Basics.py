from tkinter import *
from tkinter import ttk

root = Tk()

checkbutton = ttk.Checkbutton(root,text = "SPAM?")
checkbutton.pack()

spam = StringVar()
spam.set("SPAM!")
### to set the String Variable ###
spam.get()
### .get function to check the StrinVar's value ###

checkbutton.config(variable = spam, onvalue = "SPAM Please!", offvalue = "Boo SPAM")
### So when the checkbutton is selected the onvalue is assigned to the spam which is a StringVar ###
### and when the checkbutton is not selected the offvalue is assigned to the spam instead ###

### similarly to the check button, radio buttton looks a little bit defferent but does the same job ###
breakfast = StringVar()
ttk.Radiobutton(root, text = "SPAM",variable = breakfast, value = "SPAM").pack()
ttk.Radiobutton(root, text = "Egg",variable = breakfast, value = "Egg").pack()
ttk.Radiobutton(root, text = "Sausage",variable = breakfast, value = "Sausage").pack()
ttk.Radiobutton(root, text = "SPAM",variable = breakfast, value = "SPAM").pack()

### Using the textvariable function the label of the checkbutton is not static string anymore ###
### the name of the checkbutton now is whatever the name of the following radiobutton selected ###
checkbutton.config(textvariable = breakfast)

root.geometry("300x300+800+300")
root.mainloop()


