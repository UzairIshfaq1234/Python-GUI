from tkinter import *
import webbrowser

root=Tk()
#data for gui screen
root.geometry("1100x400")
root.maxsize(1100,400)
root.minsize(1100,400)
root.iconbitmap("D:\BSCS\BSCS 2 SEMESTER\LGU FILES\OOP IN PYTHON\python gui\skull.ico")
root.title("UZAIR PYTHON GUI")

#label
l1=Label(bg="RED",fg="WHITE",borderwidth=8,font=("Arial",15,"bold"),text="WELCOME TO UZAIR PYTHON GRAPHIC USER INTER FACE",width=1001,height=2,relief=SUNKEN)
l1.pack()
#iamge
#photo=PhotoImage(file="6.png")
#img1=Label(image=photo)
#img1.pack()
l3=Label(fg="BLACK",font=("Arial",20,"bold"),text="--MORAL---",width=1001,height=2,justify=CENTER,relief=RAISED)
l3.pack()

l2=Label(borderwidth=8,fg="BLACK",font=("Arial",10),text=" \n Hello! So here we are Learning basics of graphic user inter face and here we are at our first gui screen so stay tune we will be profesionaly desiging pyhton gui and make it a piece of cake.\nThe graphical user interface is a form of user interface that allows users to interact with electronic devices through graphical icons and audio indicator such as primary notation, \ninstead of text-based user interfaces, typed command labels or text navigation\nDesigning the visual composition and temporal behavior of a GUI is an important part of software application programming in the area of human–computer interaction. \nIts goal is to enhance the efficiency and ease of use for the underlying logical design of a stored program, a design discipline named usability.",width=1000,justify=CENTER)
l2.pack()

#def data():
#    l4=Label(width=154,bg="GREEN",fg="WHITE",text="YOU FINALLY DID GUI!")
#    l4.place(x=0,y=350)

def data():
    webbrowser.open_new(r"https://www.instagram.com/uzair_cancerian/")


#button-----------------------------------------
b1=Button(relief=FLAT,borderwidth=5,width=30,bg="BLACK",fg="WHITE",text="GUI",command=data)
b1.place(x=300,y=280)

b2=Button(relief=FLAT,borderwidth=5,width=30,bg="BLACK",fg="WHITE",text="QUIT",command=quit)
b2.place(x=550,y=280)




root.mainloop()
