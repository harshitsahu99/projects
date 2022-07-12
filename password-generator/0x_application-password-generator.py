#application generator application
import random
import string
from tkinter import *
from tkinter import messagebox

frame=Tk()
frame.title('Password Generator')
frame.geometry('400x180')
frame.config(bg='black')

def clk():
    val=int(ent.get())
    pwd(val)
    #labdem2.config(text=pswd)

def pwd(val):
    uc=string.ascii_uppercase       #here ascii_uc must be constant
    lc=string.ascii_lowercase           #cause method ends with ().
    dc=string.digits
    pc=string.punctuation
    sp=' '
    ac=uc+lc+dc+pc+sp
    value=random.sample(ac,val)
    pswd=''.join(value)
    labdem2.config(text=pswd)
    #return messagebox.showinfo('Output',f'{pswd}')

lab1=Label(text='Enter Desired Length:',bg='black',fg='white',font=('klavika','10','bold'),padx=15,pady=8)
lab1.grid(row=1,column=1)

ent=Entry(width=20,bg='silver')
ent.grid(row=1,column=2)

butt=Button(text='Enter',font='20',bg='grey',fg='white',height=1,width=8,command=clk)
butt.grid(row=2,column=2,padx=4,pady=12)

labdem1=Label(text='Your Password Is : ',bg='black',fg='white',font=('klavika','10','bold'),padx=2,pady=8)
labdem1.grid(row=3,column=1)

labdem2=Label(text='--------',bg='black',fg='white',font=('klavika','10','bold'),padx=2,pady=8)
labdem2.grid(row=3,column=2)
