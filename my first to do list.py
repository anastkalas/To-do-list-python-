from tkinter import *
from tkinter import Listbox
from tkinter import messagebox
from tkinter import filedialog
import pickle
from tkinter import ttk

#set up the window
root=Tk()

root.geometry('400x400')
root.title('TO DO LIST')
root.config(bg='orange')

label=Label(root,text='TO DO LIST',bg='orange',font=('havetica',15,'bold'))
label.pack()

    #get the errands
entry1=Entry(root,text='add',font='Havetica')
entry1.pack()

#functions for buttons
count=0

def add_item():
    global second
    global count
    var=entry1.get()
    if count==0:
        second=var
        my_list.insert(END,var)
    elif count>0:
        if second==var:
            messagebox.showinfo('showinfo','you cannot add the same errand')
        else:
            my_list.insert(END,var)
    print(count)
    count=count+1
    print(second,var)
    second=var

def save_file():
    name=str(input('Enter the name of the file you want' ,))
    errands=my_list.get(0,END)
    filename="C:/Users/anami/Desktop/python/"+name
    output_file=open(filename,'wb')
    pickle.dump(errands,output_file)
    messagebox.showinfo('showinfo','The file is saved successfully!!')

save_button=Button(text='SAVE',command=save_file)
save_button.pack()

def delete():
    my_list.delete(0,END)
    my_list.pack()
    
#buttons
button1=Button(root,text='ADD',command=add_item,bg='black',fg='white')
button1.pack()

delete=Button(root,text='DELETE',command=delete,bg='black',fg='white')
delete.pack()

#listbox for a thing
my_list=Listbox(root,height=15,width=35)
my_list.pack()


root.mainloop()
