from tkinter import *
import webbrowser

firstpage=Tk()
###########geometry##########
#firstpage.geometry("500x500")
#firstpage.maxsize(500,500)
##############################
def help():
    webbrowser.open_new(r"https://www.instagram.com/uzair_cancerian/")

def logi():
    #####################################LOGIN PAGE################################3
    secondpage=Tk()
    #setting tkinter window size 
    width= secondpage.winfo_screenwidth()  
    height= secondpage.winfo_screenheight() 
    #full screen 
    secondpage.geometry("%dx%d" % (width, height)) 
    secondpage.minsize(width,height)
    #background icon title
    secondpage.configure(background="white")
    secondpage.iconbitmap("D:\BSCS\BSCS 2 SEMESTER\LGU FILES\OOP IN PYTHON\python gui\LoginGUI\log.ico")
    secondpage.title("Login-Uzairs_designers")
    
    secondpage.mainloop()

def signo():
    ###################################SIGN UP PAGE#####################################
    thirdpage=Tk()
    #setting tkinter window size 
    width= thirdpage.winfo_screenwidth()  
    height= thirdpage.winfo_screenheight() 
    #full screen 
    thirdpage.geometry("%dx%d" % (width, height)) 
    thirdpage.minsize(width,height)
    #background icon title
    thirdpage.configure(background="white")
    thirdpage.iconbitmap("D:\BSCS\BSCS 2 SEMESTER\LGU FILES\OOP IN PYTHON\python gui\LoginGUI\log.ico")
    thirdpage.title("Login-Uzairs_designers")

######################main page############################3
#setting tkinter window size 
width= firstpage.winfo_screenwidth()  
height= firstpage.winfo_screenheight() 
#full screen 
firstpage.geometry("%dx%d" % (width, height)) 
firstpage.minsize(width,height)
#background icon title
firstpage.configure(background="black")
firstpage.iconbitmap("D:\BSCS\BSCS 2 SEMESTER\LGU FILES\OOP IN PYTHON\python gui\LoginGUI\log.ico")
firstpage.title("Login-Uzairs_designers")

#######################################################################################################
################################HEADDING############################
l1=Label(firstpage,text="L O G I N",bg="white",fg=("black"),height=2,font=("Helvetica",12,"bold"),borderwidth=5,relief=SOLID)
l1.pack(fill=X)
###########################DATA PROVIDE#####################################
l2=Label(firstpage,bg="black",font=("Helvetica",15),fg="red",justify=CENTER,text="\n \n Hello!\n Welcome to Graphic User Interface In python!")
l2.pack()


l3=Label(firstpage,bg="black",font=("Helvetica",12),fg="white",justify=CENTER,text="In computer security, logging in is the process by which an individual gains access to a computer system by identifying and authenticating themselves.\n The user credentials are typically some form of  and a matching  and these credentials themselves are sometimes referred to as a login.")
l3.pack()

l4=Label(firstpage,bg="black",font=("Helvetica",12),fg="white",justify=CENTER,text="Logging in is usually used to enter a specific page, website or application, which trespassers cannot see. Once the user is logged in, the login token \n may be used to track what actions the user has taken while connected to the site. Logging out may be performed explicitly by the user \ntaking some actions, such as entering the appropriate command or clicking a website link label as such. It can also be done implicitly, such as by the\n user powering off his or her workstation, closing a web browser window, leaving a website, or not refreshing a website within a defined period.")
l4.pack()

l5=Label(firstpage,bg="black",font=("Helvetica",12),fg="white",justify=CENTER,text="In the case of websites that use cookies to track sessions, when the user logs out, session-only cookies from that site will usually be deleted from the \n user's computer. In addition, the server invalidates any associations with the session, thereby making any session-handle in the user's \n cookie store useless. This feature comes in handy if the user is using a public computer or a computer that is using a public wireless connection.\n As a security precaution, one should not rely on implicit means of logging out of a system, especially not on a public computer; instead, one should explicitly log out and wait for the confirmation that this request has taken place.")
l4.pack()

########################sign up Button###############
but1=Button(firstpage,text="Sign Up",bg="white",font=("Helvetica",10,"bold"),fg="black",borderwidth=0,width=10,command=signo)
but1.place(x=585,y=290)
########################login Button###############
but2=Button(firstpage,text="Login",bg="white",font=("Helvetica",10,"bold"),fg="black",borderwidth=0,width=10,command=logi)
but2.place(x=695,y=290)
########################Quite Button###############
but3=Button(firstpage,text="Quite",bg="red",font=("Helvetica",10,"bold"),fg="white",borderwidth=0,width=10,command=quit)
but3.place(x=1270,y=655)
########################help button###########3
but3=Button(firstpage,text="Help",bg="red",font=("Helvetica",10,"bold"),fg="white",borderwidth=0,width=10,command=help)
but3.place(x=2,y=655)
#########################################END OF FIRST PAGE FOR DESIGN##############################################3









firstpage.mainloop()