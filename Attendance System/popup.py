import tkinter
from tkinter import messagebox

root = tkinter.Tk()
root.withdraw()

def showpopup(message):
    messagebox.showinfo("info",message)
    root.mainloop()
    
showpopup("Attendance marked")