from tkinter import *
from tkinter import ttk

root = Tk()

### In tk, you can use the notebook widget ###
### to set up mutiple pages in one widget like the web broswer ###

notebook = ttk.Notebook(root)
notebook.pack()
frame1 = ttk.Frame(notebook)
frame2 = ttk.Frame(notebook)

notebook.add(frame1, text = "One")
notebook.add(frame2, text = "Two")
### add method adds a new frame onto the right side of the previous tab ###

ttk.Button(frame1, text = "Click me").pack()

frame3 = ttk.Frame(notebook)
notebook.insert(1,frame3, text = "Three")
### insert method can add onto whatever order you want ###
### first parameter is the index will be inserted in ###

notebook.forget(1)
### only one parameter for forget_method which is the tab's index be removed ###

#notebook.select()
### returns the object of the tab is currantly selected ###
#notebook.index(notebook.select())
### returns the index if the tab is currently selected ###

notebook.tab(1,state = "disabled")
#notebook.tab(1,state = "hidden")
#notebook.tab(1,state = "normal")
### tab method like the config method of other widget ###
### state option could set the tab state to "disabled","hidden", "normal" ###

notebook.tab(0)
### if only one index parameter it returns all the info of this tab in dict format ###


root.geometry("300x300+800+300")
root.mainloop()
