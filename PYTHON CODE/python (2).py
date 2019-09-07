from tkinter import *
root=Tk()
root.geometry ('1080x920')


Label(root,text="NAME :").grid(row=0)
Entry(root).grid(row=0, column=1)
Label(root,text="PASSWORD :").grid(row=1)
Entry(root).grid(row=1, column=1)
Checkbutton(root,text="Keep me logged In").grid(columnspan=2)
root.mainloop()
