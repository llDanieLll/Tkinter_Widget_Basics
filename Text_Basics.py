from tkinter import *
#from tkinter import ttk
### Text widget is not in ttk module ###

root = Tk()

text = Text(root, width =40, height = 10)
text.pack()
text.config(wrap = 'word')
### wrap option has three values:char ,word ,none ###

text.get ('1.0','end')
### get method to retrieve the text from line 1 char 0 to the end of the text ###
### which means get all the text content in the text widget ###
### line starts from 1 char starts from 0 ###

text.get('1.0','1.end')
### this means get all the content in the first logical line ###

text.insert('1.0 + 2 lines','Insert message')
### insert the message down two logical lines ###
### the second parameter is the string inserted in ###

text.insert('1.0 + 2 lines lineend', 'and\nmore and\nmore')
### pay attention to the 'and' added to the end of the 'Insert message' then newline ###

text.delete('1.0')
### this will delete the first character of the first text line###

text.delete('1.0','1.0 lineend')
### '1.0 lineend ' this modifier will ignore the last character which is '\n' ###

text.delete('1.0','3.0 lineend + 1 chars')
### '+ 1 chars' will do a perfect job to include the last '\n' character ###

text.replace('1.0','1.0 lineend','This is the first line.')
### replace the first whole line with the string in thrid parameter ###

text.config(state = 'disabled')
### set the state to 'disabled' not only prevent the text being edited in the widget ###
### but also being edited in the program ###
### for example the delete method won't work after set it to 'disabled' ###

text.config(state ='normal')
### reset the text widget to nromal which could be edited again ###


















root.geometry("300x300+800+300")
root.mainloop()
