from tkinter  import *

def displaytask():
    lists.delete(0,'end')
    file=open("lists.txt","r")
    reading=file.read()
    reading=reading.split("\n")
    reading=list(reading)
    file.close()
    #ab=reading.get()
    #ab=inputtext.get()
    i=0
    while(i<len(reading)):
        lists.insert(END,reading[i])
        i+=1
    #lists.delete(0,Tkinter.END)
    """file=open("lists.txt","r")
    reading=file.read()
    reading=list(reading)
    i=0
    while(i<len(reading)):
        lists.insert(lists.size()+1,reading[i])
    #print(reading)
    file.close()"""
def addtask():
    file=open("lists.txt","a")
    text=inputtext.get()
    appending=file.write(text+"\n")
    file.close()
    inputtext.delete(0,'end')
def deletetask():
    text=inputtext.get()
    file=open("lists.txt","r")
    reading=file.read()
    file.close()
    file=open("lists.txt","w")
    reading=reading.split("\n")
    reading=list(reading)
    #print(reading)
    newlines=[i for i in reading if text!=i]
    #print("i=0",newlines[0])
    i=0
    while(i<len(newlines)):
        deleting=(file.write(newlines[i]+"\n"))
        i+=1
    #newlines=[line for line in reading if text not in line]
    file.close()
    inputtext.delete(0,'end')



window=Tk()
window.title("To-Do List")
window.geometry("1000x700")
title=Label(window,text="To-Do list",font=("bold",40))
title.place(x=150,y=30)
tet=Label(window,text="Enter task here ",font=("bold",20))
tet.place(x=150,y=200)
inputtext=Entry(bd=8,bg="pink")
inputtext.place(x=400,y=200)
button=Button(window,text="Add Task",font=("bold",10),bd=8,bg="grey",command=addtask)
button.place(x=150,y=350)
button=Button(window,text="Delete Task",font=("bold",10),bd=8,bg="grey",command=deletetask)
button.place(x=300,y=350)
button=Button(window,text="Display Task",font=("bold",10),bd=8,bg="grey",command=displaytask)
button.place(x=450,y=350)
lists=Listbox(x=400,y=90,bd=8,bg="pink")
lists.place(x=600,y=170)
window.mainloop()
