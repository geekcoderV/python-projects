#Install tkinter on cmd using "pip install tk"

#import files/modules
from tkinter import *
from tkinter import messagebox
#main programming session

windows = Tk()
windows.title("Confession")
#windows.geometry("420x200")
windows.configure(background="dark red")

txt = Label(windows, text="I like you, would you like to be my girlfriend?", bg="dark red", fg="black", font=("Arial Bold", 20))
txt.grid(column=0,row=0)

def Yes_button():
    messagebox.showinfo("Accepted","I am very glad to have your respond")

btn = Button(windows, text="Yes", command=Yes_button, font=("Arial Bold", 20))
btn.grid(column=0,row=1)

def No_button():
    messagebox.showinfo("Rejection","Maybe anytime soon, I wont give up")

btn1 = Button(windows, text="No", command=No_button, font=("Arial Bold",20))
btn1.grid(column=0,row=2)

windows.mainloop()
