from tkinter import *
from tkinter import ttk

root = Tk()

entry = ttk.Entry(root, width = 30)
### This Entry constructor is for the single line string data insert ###
### Width = 30 means the length is 30 characters space ###
entry.pack()


entry.get()
### .get function to get the value user type in ###

entry.delete(0,1)
### this index means only delete the character from index 0 to index 1 ###
### which is the first character ###
entry.delete(0,END)
### (0,END) means delete all the string user typed in ###

entry.insert(0,"Enter the password")
###Entry widget does have .set function, using .insert function instead ###
### (0, "Enter ...") the first pramater means where the string starts from ###
### the second string pramater is the text you want to insert ###

#entry.config(show = "*")
### this will encript the text user typed in into "*" ###

#entry.state (["disabled"])
#entry.state(["!disabled"])
#entry.instate(["disabled"])
### Entry widget has the state function to able or disable itself ###

#entry.state(["readonly"])
### sometimes you might also set the read only state preventing user from copying the inserted characters ###


root.geometry("300x300+800+300")
root.mainloop()


