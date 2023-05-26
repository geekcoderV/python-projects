from tkinter import *
from tkinter import messagebox
import time

root = Tk()
root.title("Confession")
root.geometry("550x200")
root.configure(background="dark red")

txt = Label(root, text="I like you, would you be my girlfriend?",bg="dark red",fg="black", font=("Arial Bold",20))
txt.grid(column=0,row=0)

def Yes_button():
    messagebox.showinfo("Accepted","YEHEY!!! <3")

btn = Button(root, text="Yes",command= Yes_button, font=("Arial Bold",20))
btn.grid(column=0,row=1)

def No_button():
    while True:
        messagebox.showinfo("Rejection","PLEASEEEE!!!!")
        time.sleep(0.1)

btn1 = Button(root, text="No", command= No_button, font=("Arial Bold", 20))
btn1.grid(column=0,row=2)

root.mainloop()
