from tkinter import *
root=Tk()
def left(event):
    print("LC")
def right(event):
    print("RC")
def middle(event):
    print("MC")
fm=Frame(root , width=200,height=200)
fm.bind ("<Button-1>", left)
fm.bind ("<Button-2>" ,middle)
fm.bind ("<Button-3>", right)
fm.pack()
root.mainloop()
