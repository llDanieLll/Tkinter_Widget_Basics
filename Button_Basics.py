from tkinter import *
from tkinter import ttk

root = Tk()

button = ttk.Button(root, text = "Click me ")
button.pack()
def callback():
    print("Clicked!")

button.config(command = callback)
### make the button functional using the command option###


button.invoke()
### use the invoke function stimulately trigger the button widget ###
button.state(["disabled"])

### use the state function to disable the button ###
button.instate(["disabled"])
### this command will return a boolean value: true or false ###

###use the state function to able the button again ###
button.state(["!disabled"])


root.geometry("300x300+800+300")
root.mainloop()


