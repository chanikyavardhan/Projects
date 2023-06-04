from cProfile import label
from cgitb import text
from lib2to3.pytree import convert
from random import choices
from googletrans import Translator
from gtts import gTTS
from tkinter import *

window = Tk()
window.geometry('600x280')
window.config(bg='white')

#set_bg = PhotoImage(file="lion.png")
#l1 = Label(window,image=set_bg)
#l1.place(x=0,y=-50)

e1 = Entry(window,bg="blue",fg="black",font=("Arial",25,"bold"))
e1.place(x=20,y=20)

def convert_language():
    a1 = e1.get()
    t1=Translator()
    t2=click_option.get()

    if t2 == "English":
        convert = "en"
    elif t2 == "Hindi":
        convert = "hi"

    trans_text = t1.translate(a1, dest = convert)
    trans_text = trans_text.text
    ob1 = gTTS(text = trans_text,slow = False,lang = convert )
    l2.config(text=trans_text)

choices = [
    "English",
    "Hindi"
]
click_option = StringVar()
click_option.set("Select Language")

list_drop = OptionMenu(window,click_option,*choices)
list_drop.configure(background="green",foreground="white")
list_drop.place(x=400,y=20)
l2=Label(window,text="\t\t\t",bg="black",fg="white")
l2.place(x=0,y=120)
l2 = Label(window,text="Translated text",bg="black",fg="white",font=("Arial",40,"bold"))
l2.place(x=180,y=120)
Button1 = Button(window,text="Translate",bg="red",fg="white",font=("Arial",20,"bold"),command=convert_language)
Button1.place(x=220,y=200)




window.mainloop()
