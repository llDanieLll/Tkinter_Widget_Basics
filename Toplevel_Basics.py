from tkinter import *
#from tkinter import ttk
### toplevel widget is not in ttk module, so no need to import ttk ###



root = Tk()

window = Toplevel(root)
window.title("New Window")

window_2 = Toplevel(root)
window_2.title("New Window_2")

### use lower and lift method to change the window order ###

#window.lower()

### you can add a pramater like window.lift(window_2) ###
### so the window will be just above the window_2 widget ###

window.lift(window_2)


### to maximize the window to fit the screen size ###
#window.state("zoomed")

### to hiden from the user using withdrawn ###
### the window can not be found even in the task bar ###
#window.state("withdrawn")


### to minisize the window to the task bar ###
### use the iconic state ####
### window.iconify() and window deiconify() do the same thing ###
#window.state("iconic")

### to trun the window screen to normal ###
### using normal state ###
window.state("normal")

### window.state() without any parameter ###
### that means check which state of the window widget now is ###

window.geometry("640*480+50+100")
###using the geometry method to locate where the window initially pops up ###


window.maxsize(640,480)
window.minisize(200,200)
#window.resizable(True,True)
### to set the maximum size and minimum size of the window Toplevel widget ###


window.resizable(False,False)
### resizable method takes two parameters : (x,y) if both or each direction is resizable ###


root.mainloop()
