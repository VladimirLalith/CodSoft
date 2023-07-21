from tkinter import *

root=Tk()
root.title('To-Do List')
root.geometry('400x650+400+100')
root.resizable(False,False)

tasklist=[]

def openTaskFile():
        
        try:
            with open('taskfile.txt','r') as taskfile:
                tasks=taskfile.readlines()
            for task in tasks:
                if task!='\n':
                    tasklist.append(task)
                    listbox.insert(END,task)
        except:
            file=open('taskfile.txt','w')
            file.close()

def addTask():
    task=task_entry.get()
    task_entry.delete(0,END)
    if task:
         with open('taskfile.txt','a') as taskfile:
            taskfile.write(f'\n{task}')
         tasklist.append(task)
         listbox.insert(END,task)

def deleteTask():
    global tasklist
    task=str(listbox.get(ANCHOR))
    if task in tasklist:
        tasklist.remove(task)
        with open('taskfile.txt','w') as taskfile:
            for task in tasklist:
                taskfile.write(task+'\n')
        listbox.delete(ANCHOR)
         


heading=Label(root,text='All Tasks',font='lucida 30 bold',fg='black')
heading.place(x=100,y=20)

frame=Frame(root,width=400,height=50,bg='white')
frame.place(x=0,y=150)

task=StringVar()
task_entry=Entry(frame,width=18,font='lucida 20 bold',bd=0)
task_entry.place(x=10,y=7)

button=Button(frame,text='Add',font='lucida 20 bold',width=6,fg='white',bg='blue',bd=0,command=addTask)
button.place(x=300,y=0)


frame1=Frame(root,bd=3,width=700,height=280,bg='black')
frame1.pack(pady=(210,0))

listbox=Listbox(frame1,font='lucida 15',width=40,height=16,bg='light blue',fg='white',cursor='hand2')
listbox.pack(side=LEFT,fill=BOTH,padx=2)

openTaskFile()

Button(root,text='Delete',font='lucida 20 bold',bg='red',bd=0,command=deleteTask).pack(side=BOTTOM,padx=2)

root.mainloop()