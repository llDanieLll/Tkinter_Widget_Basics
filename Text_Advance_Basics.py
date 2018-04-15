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

#text.config(state = 'disabled')
### set the state to 'disabled' not only prevent the text being edited in the widget ###
### but also being edited in the program ###
### for example the delete method won't work after set it to 'disabled' ###

#text.config(state ='normal')
### reset the text widget to nromal which could be edited again ###

################################################################################
################################################################################
###############################Text_Advaned_Basics##############################

text.tag_add('my_tag','1.0','1.0 wordend')
### add a tag for the first word ###
text.tag_config('my_tag', background = 'yellow')
### set the tag background color ###
text.tag_remove('my_tag','1.1','1.3')
### remove the tag for the second char and third char ###
text.tag_ranges('my_tag')
### returns the textindex object being tagged by my_tag ###
text.tag_names()
### returns a tuple listing all the existing tag's names ###
text.replace('my_tag.first','my_tag.last','That')
### this replaces the string tagged by my_tag with 'That' string ###
text.tag_delete('my_tag')
### to delete the tag type no longer useful ###

#text.insert('insert','_')
### insert method takes two string parameter:
### first is insert type
### secind is the insert content 
### insert - current index of the insertion cursor ###
### current - index of character under mouse position ###

### to set your own insert type using text.mark_set ###
text.mark_set('my_mark','end')
### mark_gravity to set which side you want the mark to be located around the word ###
text.mark_gravity('my_mark','left')
#text.insert('my_mark','12345')

### to unset the mark using mark_unset ###
text.mark_unset('my_mark')

### you can also add image or button widget in a text widget ###
image = PhotoImage(file = 'C:\\Users\\Daniel\'s PC\\AppData\\Local\\Programs\\Python\\Python36-32\\python_logo_small.png')

### using image_create constructor to put the image into the text widget ###
text.image_create('insert',image = image)

button = Button(text,text ='Click Me')
text.window_create('insert',window = button)
### once the button widget created, using window_create geometry manager in stead of pack() ###
### assign the button widget to window parameter ### 

root.geometry("300x300+800+300")
root.mainloop()
