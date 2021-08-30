from tkinter import *
import tkinter
import tkinter.messagebox
import os
import shutil

def proces():
    path=Entry.get(E1)
    path=str(path)
    
    
    list_of_files=os.listdir(path)
    for file in list_of_files:
        name,ext=os.path.splitext(file)
        ext = ext[1:]
        if ext == ' ':
            continue 
        if os.path.exists(path+'/'+ext):
            shutil.move(path+'/'+file,path+'/'+ext+'/'+file)
            print('Your Files Has Been Organised Successfully')
            
            
        else:
            os.makedirs(path+'/'+ext)
            shutil.move(path+'/'+file,path+'/'+ext+'/'+file)
            print('Your Files Has Been Organised Successfully')
    
    tkinter.messagebox.showinfo('Success','Your Files Has Been Organised Successfully')  
            
            
        
    

top = tkinter.Tk()
L1 = Label(top, text="File Organiser",).grid(row=0,column=1)
L2 = Label(top, text="Enter The Folder Path to Organise:-",).grid(row=1,column=0)

E1 = Entry(top, bd =5,width=40)
E1.grid(row=1,column=1)
B=Button(top, text ="Submit",command = proces).grid(row=5,column=1,)

top.mainloop()
  
