import ciud
import tkinter
from tkinter import *
from tkinter import messagebox



import sqlite3


def add():
    if (len(addtask.get())==0):
        messagebox.showerror("ERROR","No data Available \n plese enter Some task")
    else:
        ciud.insertdata(addtask.get())
        addtask.delete(0,END)
        populate()


def populate():
    listbox.delete(0,END)

    for rows in ciud.show():
        listbox.insert(END,str(rows[0])+"\t \t \t "+rows[1])
def deletetask(event):
    ciud.deletebytask(listbox.get(ANCHOR))
    populate()


def updatedata():
    updte=Tk()
    updte.title("update data")
    updte.geometry("500x200")

    def change():
        id=e1.get()
        value=e2.get()
        ciud.updatedata1(id,value)
    first_text = StringVar()
    e1 = Entry(updte, text=" SELECT ID",width=10)
    e1.grid(row=0,column=1)
    e2 = Entry(updte,width=10)
    e2.grid(row=1, column=1)
    f=Label(updte,text="SELECT ID")
    f.grid(row=0,column=0)
    f1 = Label(updte, text="Change Value")
    f1.grid(row=1, column=0)

    # save change data
    b3 = Button(updte,text="save",bg='pink', command=change)
    b3.grid(row=3,column=1)
    updte.mainloop()


main=tkinter.Tk()
main.title("TODO APP")
main.geometry("500x600")
main.resizable(False,False)
main.config(bg='blue')



 # graphic function


tkinter.Label(main,text='Task manager',bg='#1d1d1d',fg='#eeeeee',font="Verdana 20").pack(pady=10)
addtframe=tkinter.Frame(main,bg='#1d1d1d')
addtframe.pack()
addtask=tkinter.Entry(addtframe,font='Vardana',bg='#eeeeee')
addtask.pack(ipadx=20,ipady=5,side=LEFT)
addbtn=tkinter.Button(addtframe,text='Add TASK',command=add,bg='#000000',fg='#eeeeee',relief=FLAT,font="Verdana",highlightcolor='#000000',activebackground='#1d1d1d',border=0,activeforeground='#eeeeee')
addbtn.pack(ipadx=20,ipady=5,padx=20)

tkinter.Label(main,text='YOUR TASK',bg='#1d1d1d',fg='#eeeeee',font="Calabri 18").pack(pady=10)

taskframe=tkinter.Frame(main,bg='#1d1d1d')
taskframe.pack(fill=BOTH,expand=300)

scrollbar=Scrollbar(taskframe)
scrollbar.pack(side=RIGHT,fill=Y)
listbox=Listbox(taskframe,font="Verdana 18 bold",selectforeground='#1d1d1d',bg='#1d1d1d',fg='#eeeeee',selectbackground='#eeeeee')
listbox.pack(fill=BOTH,expand=300)
listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)
listbox.bind("<Double-Button-1>",deletetask)
listbox.bind("<Delete>",deletetask)

tkinter.Label(main,text='TIP Double Click on A Task to Delete',bg='#1d1d1d',fg='#eeeeee',font="Calabri 18").pack(pady=10,side=BOTTOM)
# update function

b2=tkinter.Button(text="EDIT PARTICULAR DATA",command=updatedata)
b2.pack(side=tkinter.BOTTOM)

populate()
main.mainloop()




