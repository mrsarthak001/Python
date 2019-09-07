from tkinter import *
root=Tk()
def LC():
    print("LC")
def RC():
    print("RC")
def MC():
    print("MC")
fm=Frame(root , width=200,height=200)
fm.bind ("<Button-1>" ,LC)
fm.bind ("<Button-2>" ,RC)
fm.bind ("<Button-3>" ,MC)
fm.pack()
root.mainloop()
