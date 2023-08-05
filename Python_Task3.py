from tkinter import *
import random
import string

root=Tk()
root.geometry('400x300')
root.title('Password Generator')
root.resizable(False,False)

pass_str=StringVar()
pswd_len=IntVar()

def get_pass():
    pass1=string.ascii_letters + string.digits + string.punctuation
    password=""
    for x in range(pswd_len.get()):
        password=password + random.choice(pass1)
        pass_str.set(password)

Label(root,text='Enter length of the password:').pack(pady=9)
Entry(root,textvariable=pswd_len).pack(pady=2)
Button(root,text='Generate Password',command=get_pass).pack(pady=15)
Entry(root,textvariable=pass_str).pack(pady=2)


root.mainloop()      