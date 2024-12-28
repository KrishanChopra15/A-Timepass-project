import mysql.connector as mysql
db=mysql.connect(user='root',password='Krishan#15806',host='127.0.0.1',database='project')
cur=db.cursor()
import tkinter as tk
#starter function
def start():
    root=tk.Tk()
    root.title("Project")
    root.geometry("770x650")
    root.resizable(width=False,height=False)

    main_frame=tk.Frame(root,bg="#cdfaf5",pady=0) #background of tk
    main_frame.pack(fill=tk.BOTH,expand=True)
    tk.Label(
        main_frame,
        background="#cdfaf5",       #color of back of button
        foreground="black",       #color of text
        text="Which product do you wish to buy?",
        height=2,
        border=1,
        font=("Arial",25,"bold")).place(relx=0.15, rely=0.08)
    tk.Label(
        main_frame,
        background="#cdfaf5",       #color of back of button
        foreground="black",       #color of text
        text="Hi! Welcome to my retail shop",
        height=2,
        border=1,
        font=("Arial",25,"bold")).place(relx=0.2, rely=0.0)
    button1=tk.Button(
        main_frame,
        background="#4169e1",     #color of back of button
        foreground="#cdfaf5",       #color of text
        activebackground="grey",  #color of back of button activated
        activeforeground="black", #color of text activated
        highlightthickness=2,
        width=13,
        height=2,
        border=10,
        cursor="hand1",
        text="Mobile",
        font=("Arial",20,'bold'),   
        command=lambda:[root.destroy(),mobile()]
        ).place(relx=0.15, rely=0.2)

    button2=tk.Button(
        main_frame,
        background="#4169e1",     #color of back of button
        foreground="#cdfaf5",       #color of text
        activebackground="grey",  #color of back of button activated
        activeforeground="black", #color of text activated
        highlightthickness=2,
        width=13,
        height=2,
        border=10,
        cursor="hand1",
        text="Laptop",
        font=("Arial",20,'bold'),
        command=lambda: [root.destroy(),laptop()]
        ).place(relx=0.55, rely=0.2)
   
    button3=tk.Button(
        main_frame,
        background="#4169e1",     #color of back of button
        foreground="#cdfaf5",       #color of text
        activebackground="grey",  #color of back of button activated
        activeforeground="black", #color of text activated
        highlightthickness=2,
        width=13,
        height=2,
        border=10,
        cursor="hand1",
        text="Console",
        font=("Arial",20,'bold'),
        command=lambda: [root.destroy(),Console()]
        ).place(relx=0.15, rely=0.4)
    
    button4=tk.Button(
        main_frame,
        background="#4169e1",     #color of back of button
        foreground="#cdfaf5",       #color of text
        activebackground="grey",  #color of back of button activated
        activeforeground="black", #color of text activated
        highlightthickness=2,
        width=13,
        height=2,
        border=10,
        cursor="hand1",
        text="Televisions",
        font=("Arial",20,'bold'),
        command=lambda: [root.destroy(),Television()]
        ).place(relx=0.55, rely=0.4)

    button5=tk.Button(
        main_frame,
        background="#002366",       #color of back of button
        foreground="#cdfaf5",       #color of text
        activebackground="grey",  #color of back of button activated
        activeforeground="black", #color of text activated
        highlightthickness=2,
        width=13,
        height=2,
        border=10,
        cursor="hand1",
        text="Close",
        font=("Arial",20,'bold'),
        command=lambda: [root.destroy(),close()]
        ).place(relx=0.55, rely=0.6)
    
    button6=tk.Button(
        main_frame,
        background="#002366",       #color of back of button
        foreground="#cdfaf5",       #color of text
        activebackground="grey",  #color of back of button activated
        activeforeground="black", #color of text activated
        highlightthickness=2,
        width=13,
        height=2,
        border=10,
        cursor="hand1",
        text="Cart",
        font=("Arial",20,'bold'),
        command=lambda: [root.destroy(),Cart()]
        ).place(relx=0.15, rely=0.6)
    root.mainloop()

#mobile function
def mobile():
    root=tk.Tk()
    root.geometry("770x500")
    root.title("Mobile")
    root.resizable(width=False,height=False)

    main_frame=tk.Frame(root,bg="#cdfaf5",pady=40) #background of button
    main_frame.pack(fill=tk.BOTH,expand=True)
    tk.Label(
        main_frame,
        background="#cdfaf5",       #color of back of button
        foreground="black",       #color of text
        text="Which OS would you like to select?",
        height=2,
        border=1,
        font=("Arial",25,"bold")).place(relx=0.5, rely=0, anchor=tk.N)
    button1=tk.Button(
        main_frame,
        background="#4169e1",     #color of back of button
        foreground="#cdfaf5",       #color of text
        activebackground="grey",  #color of back of button activated
        activeforeground="black", #color of text activated
        highlightthickness=2,
        width=12,
        height=2,
        border=10,
        cursor="hand1",
        text="Android OS",
        font=("Arial",20,'bold'),   
        command=lambda:[root.destroy(),Android()]
        ).place(relx=0.03, rely=0.25)

    button2=tk.Button(
        main_frame,
        background="#4169e1",     #color of back of button
        foreground="#cdfaf5",       #color of text
        activebackground="grey",  #color of back of button activated
        activeforeground="black", #color of text activated
        highlightthickness=2,
        width=12,
        height=2,
        border=10,
        cursor="hand1",
        text="Apple iOS",
        font=("Arial",20,'bold'),
        command=lambda:[root.destroy(),AppleIOS()]
        ).place(relx=0.35, rely=0.25)       
    
    button3=tk.Button(
        main_frame,
        background="#4169e1",     #color of back of button
        foreground="#cdfaf5",       #color of text
        activebackground="grey",  #color of back of button activated
        activeforeground="black", #color of text activated
        highlightthickness=2,
        width=12,
        height=2,
        border=10,
        cursor="hand1",
        text="BlackBerry OS",
        font=("Arial",20,'bold'),
        command=lambda:[root.destroy(),BlackBerryOS()]
        ).place(relx=0.67, rely=0.25)

    button4=tk.Button(
        main_frame,
        background="#002366",       #color of back of button
        foreground="#cdfaf5",       #color of text
        activebackground="grey",  #color of back of button activated
        activeforeground="black", #color of text activated
        highlightthickness=2,
        width=12,
        height=2,
        border=10,
        cursor="hand1",
        text="To Start",
        font=("Arial",20,'bold'),
        command=lambda: [root.destroy(),start()]
        ).place(relx=0.35, rely=0.55)
    
    button5=tk.Button(
        main_frame,
        background="#002366",       #color of back of button
        foreground="#cdfaf5",       #color of text
        activebackground="grey",  #color of back of button activated
        activeforeground="black", #color of text activated
        highlightthickness=2,
        width=12,
        height=2,
        border=10,
        cursor="hand1",
        text="Close",
        font=("Arial",20,'bold'),
        command=lambda: [root.destroy(),close()]
        ).place(relx=0.67, rely=0.55)
    button6=tk.Button(
        main_frame,
        background="#002366",       #color of back of button
        foreground="#cdfaf5",       #color of text
        activebackground="grey",  #color of back of button activated
        activeforeground="black", #color of text activated
        highlightthickness=2,
        width=12,
        height=2,
        border=10,
        cursor="hand1",
        text="Cart",
        font=("Arial",20,'bold'),
        command=lambda: [root.destroy(),Cart()]
        ).place(relx=0.03, rely=0.55)
    root.mainloop()
    
def Android():
    root=tk.Tk()
    root.title("Android OS")
    root.geometry("729x450")
    root.resizable(width=False,height=False)
    cur.execute("select Number,Name from android")
    main_frame=tk.Frame(root,bg="#cdfaf5",pady=0) #background of button
    main_frame.pack(fill=tk.BOTH,expand=True)
    
    i=1
    c=tk.Label(
        main_frame,
        width=30,
        text="S. No.",
        borderwidth=3,
        relief="ridge",
        anchor="w",
        bg="yellow",
        font=("Ariel",15)).grid(row=0,column=0)
    c=tk.Label(
        main_frame,
        width=30,
        text="Android OS",
        borderwidth=3,
        relief="ridge",
        anchor="w",
        bg="yellow",
        font=("Ariel",15)).grid(row=0,column=1)
    for a in cur:
        for b in range(len(a)):
            c=tk.Entry(main_frame,width=30,fg="blue",bg="white",borderwidth=3,font=("Ariel",15))
            c.grid(row=i,column=b)
            c.insert(tk.END,a[b])
        i=i+1
    tk.Button(
        main_frame,
        background="#002366",       #color of back of button
        foreground="#cdfaf5",       #color of text
        activebackground="grey",  #color of back of button activated
        activeforeground="black", #color of text activated
        highlightthickness=2,
        width=5,
        border=2,
        cursor="hand1",
        text="Select",
        font=("Arial",10,'bold'),
        command=lambda: [root.destroy(),Samsung()]
        ).grid(row=1,column=2)
    tk.Button(
        main_frame,
        background="#002366",       #color of back of button
        foreground="#cdfaf5",       #color of text
        activebackground="grey",  #color of back of button activated
        activeforeground="black", #color of text activated
        highlightthickness=2,
        width=5,
        border=2,
        cursor="hand1",
        text="Select",
        font=("Arial",10,'bold'),
        command=lambda: [root.destroy(),Xiaomi()]
        ).grid(row=2,column=2)
    tk.Button(
        main_frame,
        background="#002366",       #color of back of button
        foreground="#cdfaf5",       #color of text
        activebackground="grey",  #color of back of button activated
        activeforeground="black", #color of text activated
        highlightthickness=2,
        width=5,
        border=2,
        cursor="hand1",
        text="Select",
        font=("Arial",10,'bold'),
        command=lambda: [root.destroy(),Realme()]
        ).grid(row=3,column=2)
    tk.Button(
        main_frame,
        background="#002366",       #color of back of button
        foreground="#cdfaf5",       #color of text
        activebackground="grey",  #color of back of button activated
        activeforeground="black", #color of text activated
        highlightthickness=2,
        width=5,
        border=2,
        cursor="hand1",
        text="Select",
        font=("Arial",10,'bold'),
        command=lambda: [root.destroy(),OPPO()]
        ).grid(row=4,column=2)
    tk.Button(
        main_frame,
        background="#002366",       #color of back of button
        foreground="#cdfaf5",       #color of text
        activebackground="grey",  #color of back of button activated
        activeforeground="black", #color of text activated
        highlightthickness=2,
        width=5,
        border=2,
        cursor="hand1",
        text="Select",
        font=("Arial",10,'bold'),
        command=lambda: [root.destroy(),VIVO()]
        ).grid(row=5,column=2)
    tk.Button(
        main_frame,
        background="#002366",       #color of back of button
        foreground="#cdfaf5",       #color of text
        activebackground="grey",  #color of back of button activated
        activeforeground="black", #color of text activated
        highlightthickness=2,
        width=5,
        border=2,
        cursor="hand1",
        text="Select",
        font=("Arial",10,'bold'),
        command=lambda: [root.destroy(),Pixel()]
        ).grid(row=6,column=2)
        
    tk.Button(
        main_frame,
        background="#002366",       #color of back of button
        foreground="#cdfaf5",       #color of text
        activebackground="grey",  #color of back of button activated
        activeforeground="black", #color of text activated
        highlightthickness=2,
        width=13,
        border=6,
        cursor="hand1",
        text="To Start",
        font=("Arial",20,'bold'),
        command=lambda: [root.destroy(),start()]
        ).place(relx=0.19, rely=0.55)
    
    tk.Button(
        main_frame,
        background="#002366",       #color of back of button
        foreground="#cdfaf5",       #color of text
        activebackground="grey",  #color of back of button activated
        activeforeground="black", #color of text activated
        highlightthickness=2,
        width=13,
        border=6,
        cursor="hand1",
        text="Close",
        font=("Arial",20,'bold'),
        command=lambda: [root.destroy(),close()]
        ).place(relx=0.53, rely=0.55)
    
    tk.Button(
        main_frame,
        background="#002366",       #color of back of button
        foreground="#cdfaf5",       #color of text
        activebackground="grey",  #color of back of button activated
        activeforeground="black", #color of text activated
        highlightthickness=2,
        width=13,
        border=6,
        cursor="hand1",
        text="Cart",
        font=("Arial",20,'bold'),
        command=lambda: [root.destroy(),Cart()]
        ).place(relx=0.19, rely=0.75)
    
    tk.Button(
        main_frame,
        background="#002366",       #color of back of button
        foreground="#cdfaf5",       #color of text
        activebackground="grey",  #color of back of button activated
        activeforeground="black", #color of text activated
        highlightthickness=2,
        width=13,
        border=6,
        cursor="hand1",
        text="Go Back",
        font=("Arial",20,'bold'),
        command=lambda: [root.destroy(),mobile()]
        ).place(relx=0.53, rely=0.75)
    root.mainloop()
    
def Samsung():
    root=tk.Tk()
    root.title("Samsung")
    root.geometry("740x450")
    root.resizable(width=False,height=False)
    cur.execute("select * from samsung")
    main_frame=tk.Frame(root,bg="#cdfaf5",pady=0) #background of button
    main_frame.pack(fill=tk.BOTH,expand=True)
    
    i=1
    c=tk.Label(
        main_frame,
        width=20,
        text="S. No.",
        borderwidth=3,
        relief="ridge",
        anchor="w",
        bg="yellow",
        font=("Ariel",15)).grid(row=0,column=0)
    c=tk.Label(
        main_frame,
        width=20,
        text="Samsung",
        borderwidth=3,
        relief="ridge",
        anchor="w",
        bg="yellow",
        font=("Ariel",15)).grid(row=0,column=1)
    c=tk.Label(
        main_frame,
        width=20,
        text="Price in Rs.",
        borderwidth=3,
        relief="ridge",
        anchor="w",
        bg="yellow",
        font=("Ariel",15)).grid(row=0,column=2)
    for a in cur:
        for b in range(len(a)):
            c=tk.Entry(main_frame,width=20,fg="blue",bg="white",borderwidth=3,font=("Ariel",15))
            c.grid(row=i,column=b)
            c.insert(tk.END,a[b])
        i=i+1
    tk.Button(
        main_frame,
        background="#002366",       #color of back of button
        foreground="#cdfaf5",       #color of text
        activebackground="grey",  #color of back of button activated
        activeforeground="black", #color of text activated
        highlightthickness=2,
        width=5,
        border=2,
        cursor="hand1",
        text="Add",
        font=("Arial",10,'bold'),
        command=lambda: [GalaxyZFold6()]
        ).grid(row=1,column=3)
    tk.Button(
        main_frame,
        background="#002366",       #color of back of button
        foreground="#cdfaf5",       #color of text
        activebackground="grey",  #color of back of button activated
        activeforeground="black", #color of text activated
        highlightthickness=2,
        width=5,
        border=2,
        cursor="hand1",
        text="Add",
        font=("Arial",10,'bold'),
        command=lambda: [GalaxyZFlip6()]
        ).grid(row=2,column=3)
    tk.Button(
        main_frame,
        background="#002366",       #color of back of button
        foreground="#cdfaf5",       #color of text
        activebackground="grey",  #color of back of button activated
        activeforeground="black", #color of text activated
        highlightthickness=2,
        width=5,
        border=2,
        cursor="hand1",
        text="Add",
        font=("Arial",10,'bold'),
        command=lambda: [GalaxyS24()]
        ).grid(row=3,column=3)
    tk.Button(
        main_frame,
        background="#002366",       #color of back of button
        foreground="#cdfaf5",       #color of text
        activebackground="grey",  #color of back of button activated
        activeforeground="black", #color of text activated
        highlightthickness=2,
        width=5,
        border=2,
        cursor="hand1",
        text="Add",
        font=("Arial",10,'bold'),
        command=lambda: [GalaxyA54()]
        ).grid(row=4,column=3)
    tk.Button(
        main_frame,
        background="#002366",       #color of back of button
        foreground="#cdfaf5",       #color of text
        activebackground="grey",  #color of back of button activated
        activeforeground="black", #color of text activated
        highlightthickness=2,
        width=5,
        border=2,
        cursor="hand1",
        text="Add",
        font=("Arial",10,'bold'),
        command=lambda: [GalaxyA34()]
        ).grid(row=5,column=3)
    tk.Button(
        main_frame,
        background="#002366",       #color of back of button
        foreground="#cdfaf5",       #color of text
        activebackground="grey",  #color of back of button activated
        activeforeground="black", #color of text activated
        highlightthickness=2,
        width=5,
        border=2,
        cursor="hand1",
        text="Add",
        font=("Arial",10,'bold'),
        command=lambda: [GalaxyM24()]
        ).grid(row=6,column=3)
        
    tk.Button(
        main_frame,
        background="#002366",       #color of back of button
        foreground="#cdfaf5",       #color of text
        activebackground="grey",  #color of back of button activated
        activeforeground="black", #color of text activated
        highlightthickness=2,
        width=13,
        border=6,
        cursor="hand1",
        text="To Start",
        font=("Arial",20,'bold'),
        command=lambda: [root.destroy(),start()]
        ).place(relx=0.19, rely=0.55)
    
    tk.Button(
        main_frame,
        background="#002366",       #color of back of button
        foreground="#cdfaf5",       #color of text
        activebackground="grey",  #color of back of button activated
        activeforeground="black", #color of text activated
        highlightthickness=2,
        width=13,
        border=6,
        cursor="hand1",
        text="Close",
        font=("Arial",20,'bold'),
        command=lambda: [root.destroy(),close()]
        ).place(relx=0.53, rely=0.55)
    
    tk.Button(
        main_frame,
        background="#002366",       #color of back of button
        foreground="#cdfaf5",       #color of text
        activebackground="grey",  #color of back of button activated
        activeforeground="black", #color of text activated
        highlightthickness=2,
        width=13,
        border=6,
        cursor="hand1",
        text="Cart",
        font=("Arial",20,'bold'),
        command=lambda: [root.destroy(),Cart()]
        ).place(relx=0.19, rely=0.75)
    
    tk.Button(
        main_frame,
        background="#002366",       #color of back of button
        foreground="#cdfaf5",       #color of text
        activebackground="grey",  #color of back of button activated
        activeforeground="black", #color of text activated
        highlightthickness=2,
        width=13,
        border=6,
        cursor="hand1",
        text="Go Back",
        font=("Arial",20,'bold'),
        command=lambda: [root.destroy(),Android()]
        ).place(relx=0.53, rely=0.75)
    root.mainloop()
def GalaxyZFold6():
    cur.execute("Select qty from cart where productname= 'Samsung Galaxy Z Fold 6';")
    for a in cur:
        for c in range(len(a)):
            cur.execute("update cart set qty=qty+1 where productname='Samsung Galaxy Z Fold 6';")
            db.commit()
def GalaxyZFlip6():
    cur.execute("Select qty from cart where productname= 'Samsung Galaxy Z Flip 6';")
    for a in cur:
        for c in range(len(a)):
            cur.execute("update cart set qty=qty+1 where productname='Samsung Galaxy Z Flip 6';")
            db.commit()
def GalaxyS24():
    cur.execute("Select qty from cart where productname= 'Samsung Galaxy S24';")
    for a in cur:
        for c in range(len(a)):
            cur.execute("update cart set qty=qty+1 where productname='Samsung Galaxy S24';")
            db.commit()
def GalaxyA54():
    cur.execute("Select qty from cart where productname= 'Samsung Galaxy A54';")
    for a in cur:
        for c in range(len(a)):
            cur.execute("update cart set qty=qty+1 where productname='Samsung Galaxy A54';")
            db.commit()
def GalaxyA34():
    cur.execute("Select qty from cart where productname= 'Samsung Galaxy A34';")
    for a in cur:
        for c in range(len(a)):
            cur.execute("update cart set qty=qty+1 where productname='Samsung Galaxy A34';")
            db.commit()
def GalaxyM24():
    cur.execute("Select qty from cart where productname= 'Samsung Galaxy M24';")
    for a in cur:
        for c in range(len(a)):
            cur.execute("update cart set qty=qty+1 where productname='Samsung Galaxy M24';")
            db.commit()

def Xiaomi():
    root=tk.Tk()
    root.title("Xiaomi")
    root.geometry("740x450")
    root.resizable(width=False,height=False)
    cur.execute("select * from xiaomi")
    main_frame=tk.Frame(root,bg="#cdfaf5",pady=0) #background of button
    main_frame.pack(fill=tk.BOTH,expand=True)
    
    i=1
    c=tk.Label(
        main_frame,
        width=20,
        text="S. No.",
        borderwidth=3,
        relief="ridge",
        anchor="w",
        bg="yellow",
        font=("Ariel",15)).grid(row=0,column=0)
    c=tk.Label(
        main_frame,
        width=20,
        text="Xiaomi",
        borderwidth=3,
        relief="ridge",
        anchor="w",
        bg="yellow",
        font=("Ariel",15)).grid(row=0,column=1)
    c=tk.Label(
        main_frame,
        width=20,
        text="Price in Rs.",
        borderwidth=3,
        relief="ridge",
        anchor="w",
        bg="yellow",
        font=("Ariel",15)).grid(row=0,column=2)
    for a in cur:
        for b in range(len(a)):
            c=tk.Entry(main_frame,width=20,fg="blue",bg="white",borderwidth=3,font=("Ariel",15))
            c.grid(row=i,column=b)
            c.insert(tk.END,a[b])
        i=i+1
    tk.Button(
        main_frame,
        background="#002366",       #color of back of button
        foreground="#cdfaf5",       #color of text
        activebackground="grey",  #color of back of button activated
        activeforeground="black", #color of text activated
        highlightthickness=2,
        width=5,
        border=2,
        cursor="hand1",
        text="Add",
        font=("Arial",10,'bold'),
        command=lambda: [RedmiNote14()]
        ).grid(row=1,column=3)
    tk.Button(
        main_frame,
        background="#002366",       #color of back of button
        foreground="#cdfaf5",       #color of text
        activebackground="grey",  #color of back of button activated
        activeforeground="black", #color of text activated
        highlightthickness=2,
        width=5,
        border=2,
        cursor="hand1",
        text="Add",
        font=("Arial",10,'bold'),
        command=lambda: [RedmiK80()]
        ).grid(row=2,column=3)
    tk.Button(
        main_frame,
        background="#002366",       #color of back of button
        foreground="#cdfaf5",       #color of text
        activebackground="grey",  #color of back of button activated
        activeforeground="black", #color of text activated
        highlightthickness=2,
        width=5,
        border=2,
        cursor="hand1",
        text="Add",
        font=("Arial",10,'bold'),
        command=lambda: [RedmiA4()]
        ).grid(row=3,column=3)
    tk.Button(
        main_frame,
        background="#002366",       #color of back of button
        foreground="#cdfaf5",       #color of text
        activebackground="grey",  #color of back of button activated
        activeforeground="black", #color of text activated
        highlightthickness=2,
        width=5,
        border=2,
        cursor="hand1",
        text="Add",
        font=("Arial",10,'bold'),
        command=lambda: [RedmiNote13()]
        ).grid(row=4,column=3)
    tk.Button(
        main_frame,
        background="#002366",       #color of back of button
        foreground="#cdfaf5",       #color of text
        activebackground="grey",  #color of back of button activated
        activeforeground="black", #color of text activated
        highlightthickness=2,
        width=5,
        border=2,
        cursor="hand1",
        text="Add",
        font=("Arial",10,'bold'),
        command=lambda: [POCOC75()]
        ).grid(row=5,column=3)
        
    tk.Button(
        main_frame,
        background="#002366",       #color of back of button
        foreground="#cdfaf5",       #color of text
        activebackground="grey",  #color of back of button activated
        activeforeground="black", #color of text activated
        highlightthickness=2,
        width=13,
        border=6,
        cursor="hand1",
        text="To Start",
        font=("Arial",20,'bold'),
        command=lambda: [root.destroy(),start()]
        ).place(relx=0.19, rely=0.55)
    
    tk.Button(
        main_frame,
        background="#002366",       #color of back of button
        foreground="#cdfaf5",       #color of text
        activebackground="grey",  #color of back of button activated
        activeforeground="black", #color of text activated
        highlightthickness=2,
        width=13,
        border=6,
        cursor="hand1",
        text="Close",
        font=("Arial",20,'bold'),
        command=lambda: [root.destroy(),close()]
        ).place(relx=0.53, rely=0.55)
    
    tk.Button(
        main_frame,
        background="#002366",       #color of back of button
        foreground="#cdfaf5",       #color of text
        activebackground="grey",  #color of back of button activated
        activeforeground="black", #color of text activated
        highlightthickness=2,
        width=13,
        border=6,
        cursor="hand1",
        text="Cart",
        font=("Arial",20,'bold'),
        command=lambda: [root.destroy(),Cart()]
        ).place(relx=0.19, rely=0.75)
    
    tk.Button(
        main_frame,
        background="#002366",       #color of back of button
        foreground="#cdfaf5",       #color of text
        activebackground="grey",  #color of back of button activated
        activeforeground="black", #color of text activated
        highlightthickness=2,
        width=13,
        border=6,
        cursor="hand1",
        text="Go Back",
        font=("Arial",20,'bold'),
        command=lambda: [root.destroy(),Android()]
        ).place(relx=0.53, rely=0.75)
    root.mainloop()
def RedmiNote14():
    cur.execute("Select qty from cart where productname= 'Xiaomi Redmi Note 14';")
    for a in cur:
        for c in range(len(a)):
            cur.execute("update cart set qty=qty+1 where productname='Xiaomi Redmi Note 14';")
            db.commit()
def RedmiK80():
    cur.execute("Select qty from cart where productname= 'Xiaomi Redmi K80';")
    for a in cur:
        for c in range(len(a)):
            cur.execute("update cart set qty=qty+1 where productname='Xiaomi Redmi K80';")
            db.commit()
def RedmiA4():
    cur.execute("Select qty from cart where productname= 'Xiaomi Redmi A4';")
    for a in cur:
        for c in range(len(a)):
            cur.execute("update cart set qty=qty+1 where productname='Xiaomi Redmi A4';")
            db.commit()
def RedmiNote13():
    cur.execute("Select qty from cart where productname= 'Xiaomi Redmi Note 13';")
    for a in cur:
        for c in range(len(a)):
            cur.execute("update cart set qty=qty+1 where productname='Xiaomi Redmi Note 13';")
            db.commit()
def POCOC75():
    cur.execute("Select qty from cart where productname= 'Xiaomi POCO C75';")
    for a in cur:
        for c in range(len(a)):
            cur.execute("update cart set qty=qty+1 where productname='Xiaomi POCO C75';")
            db.commit()
def Realme():
    root=tk.Tk()
    root.title("Realme")
    root.geometry("740x450")
    root.resizable(width=False,height=False)
    cur.execute("select * from realme")
    main_frame=tk.Frame(root,bg="#cdfaf5",pady=0) #background of button
    main_frame.pack(fill=tk.BOTH,expand=True)
    
    i=1
    c=tk.Label(
        main_frame,
        width=20,
        text="S. No.",
        borderwidth=3,
        relief="ridge",
        anchor="w",
        bg="yellow",
        font=("Ariel",15)).grid(row=0,column=0)
    c=tk.Label(
        main_frame,
        width=20,
        text="Realme",
        borderwidth=3,
        relief="ridge",
        anchor="w",
        bg="yellow",
        font=("Ariel",15)).grid(row=0,column=1)
    c=tk.Label(
        main_frame,
        width=20,
        text="Price in Rs.",
        borderwidth=3,
        relief="ridge",
        anchor="w",
        bg="yellow",
        font=("Ariel",15)).grid(row=0,column=2)
    for a in cur:
        for b in range(len(a)):
            c=tk.Entry(main_frame,width=20,fg="blue",bg="white",borderwidth=3,font=("Ariel",15))
            c.grid(row=i,column=b)
            c.insert(tk.END,a[b])
        i=i+1
    tk.Button(
        main_frame,
        background="#002366",       #color of back of button
        foreground="#cdfaf5",       #color of text
        activebackground="grey",  #color of back of button activated
        activeforeground="black", #color of text activated
        highlightthickness=2,
        width=5,
        border=2,
        cursor="hand1",
        text="Add",
        font=("Arial",10,'bold'),
        command=lambda: [V60()]
        ).grid(row=1,column=3)
    tk.Button(
        main_frame,
        background="#002366",       #color of back of button
        foreground="#cdfaf5",       #color of text
        activebackground="grey",  #color of back of button activated
        activeforeground="black", #color of text activated
        highlightthickness=2,
        width=5,
        border=2,
        cursor="hand1",
        text="Add",
        font=("Arial",10,'bold'),
        command=lambda: [Neo7()]
        ).grid(row=2,column=3)
    tk.Button(
        main_frame,
        background="#002366",       #color of back of button
        foreground="#cdfaf5",       #color of text
        activebackground="grey",  #color of back of button activated
        activeforeground="black", #color of text activated
        highlightthickness=2,
        width=5,
        border=2,
        cursor="hand1",
        text="Add",
        font=("Arial",10,'bold'),
        command=lambda: [Note60x()]
        ).grid(row=3,column=3)
    tk.Button(
        main_frame,
        background="#002366",       #color of back of button
        foreground="#cdfaf5",       #color of text
        activebackground="grey",  #color of back of button activated
        activeforeground="black", #color of text activated
        highlightthickness=2,
        width=5,
        border=2,
        cursor="hand1",
        text="Add",
        font=("Arial",10,'bold'),
        command=lambda: [GT7Pro()]
        ).grid(row=4,column=3)
    tk.Button(
        main_frame,
        background="#002366",       #color of back of button
        foreground="#cdfaf5",       #color of text
        activebackground="grey",  #color of back of button activated
        activeforeground="black", #color of text activated
        highlightthickness=2,
        width=5,
        border=2,
        cursor="hand1",
        text="Add",
        font=("Arial",10,'bold'),
        command=lambda: [P2Pro()]
        ).grid(row=5,column=3)

    tk.Button(
        main_frame,
        background="#002366",       #color of back of button
        foreground="#cdfaf5",       #color of text
        activebackground="grey",  #color of back of button activated
        activeforeground="black", #color of text activated
        highlightthickness=2,
        width=13,
        border=6,
        cursor="hand1",
        text="To Start",
        font=("Arial",20,'bold'),
        command=lambda: [root.destroy(),start()]
        ).place(relx=0.19, rely=0.55)
    
    tk.Button(
        main_frame,
        background="#002366",       #color of back of button
        foreground="#cdfaf5",       #color of text
        activebackground="grey",  #color of back of button activated
        activeforeground="black", #color of text activated
        highlightthickness=2,
        width=13,
        border=6,
        cursor="hand1",
        text="Close",
        font=("Arial",20,'bold'),
        command=lambda: [root.destroy(),close()]
        ).place(relx=0.53, rely=0.55)
    
    tk.Button(
        main_frame,
        background="#002366",       #color of back of button
        foreground="#cdfaf5",       #color of text
        activebackground="grey",  #color of back of button activated
        activeforeground="black", #color of text activated
        highlightthickness=2,
        width=13,
        border=6,
        cursor="hand1",
        text="Cart",
        font=("Arial",20,'bold'),
        command=lambda: [root.destroy(),Cart()]
        ).place(relx=0.19, rely=0.75)
    
    tk.Button(
        main_frame,
        background="#002366",       #color of back of button
        foreground="#cdfaf5",       #color of text
        activebackground="grey",  #color of back of button activated
        activeforeground="black", #color of text activated
        highlightthickness=2,
        width=13,
        border=6,
        cursor="hand1",
        text="Go Back",
        font=("Arial",20,'bold'),
        command=lambda: [root.destroy(),Android()]
        ).place(relx=0.53, rely=0.75)
    root.mainloop()
def V60():
    cur.execute("Select qty from cart where productname= 'Realme V60';")
    for a in cur:
        for c in range(len(a)):
            cur.execute("update cart set qty=qty+1 where productname='Realme V60';")
            db.commit()
def Neo7():
    cur.execute("Select qty from cart where productname= 'Realme Neo 7';")
    for a in cur:
        for c in range(len(a)):
            cur.execute("update cart set qty=qty+1 where productname='Realme Neo 7';")
            db.commit()
def Note60x():
    cur.execute("Select qty from cart where productname= 'Realme Note 60x';")
    for a in cur:
        for c in range(len(a)):
            cur.execute("update cart set qty=qty+1 where productname='Realme Note 60x';")
            db.commit()
def GT7Pro():
    cur.execute("Select qty from cart where productname= 'Realme GT 7 Pro';")
    for a in cur:
        for c in range(len(a)):
            cur.execute("update cart set qty=qty+1 where productname='Realme GT 7 Pro';")
            db.commit()
def P2Pro():
    cur.execute("Select qty from cart where productname= 'Realme P2 Pro';")
    for a in cur:
        for c in range(len(a)):
            cur.execute("update cart set qty=qty+1 where productname='Realme P2 Pro';")
            db.commit()
def OPPO():
    root=tk.Tk()
    root.title("OPPO")
    root.geometry("740x450")
    root.resizable(width=False,height=False)
    cur.execute("select * from oppo")
    main_frame=tk.Frame(root,bg="#cdfaf5",pady=0) #background of button
    main_frame.pack(fill=tk.BOTH,expand=True)
    
    i=1
    c=tk.Label(
        main_frame,
        width=20,
        text="S. No.",
        borderwidth=3,
        relief="ridge",
        anchor="w",
        bg="yellow",
        font=("Ariel",15)).grid(row=0,column=0)
    c=tk.Label(
        main_frame,
        width=20,
        text="OPPO",
        borderwidth=3,
        relief="ridge",
        anchor="w",
        bg="yellow",
        font=("Ariel",15)).grid(row=0,column=1)
    c=tk.Label(
        main_frame,
        width=20,
        text="Price in Rs.",
        borderwidth=3,
        relief="ridge",
        anchor="w",
        bg="yellow",
        font=("Ariel",15)).grid(row=0,column=2)
    for a in cur:
        for b in range(len(a)):
            c=tk.Entry(main_frame,width=20,fg="blue",bg="white",borderwidth=3,font=("Ariel",15))
            c.grid(row=i,column=b)
            c.insert(tk.END,a[b])
        i=i+1
    tk.Button(
        main_frame,
        background="#002366",       #color of back of button
        foreground="#cdfaf5",       #color of text
        activebackground="grey",  #color of back of button activated
        activeforeground="black", #color of text activated
        highlightthickness=2,
        width=5,
        border=2,
        cursor="hand1",
        text="Add",
        font=("Arial",10,'bold'),
        command=lambda: [FindX8()]
        ).grid(row=1,column=3)
    tk.Button(
        main_frame,
        background="#002366",       #color of back of button
        foreground="#cdfaf5",       #color of text
        activebackground="grey",  #color of back of button activated
        activeforeground="black", #color of text activated
        highlightthickness=2,
        width=5,
        border=2,
        cursor="hand1",
        text="Add",
        font=("Arial",10,'bold'),
        command=lambda: [K12()]
        ).grid(row=2,column=3)
    tk.Button(
        main_frame,
        background="#002366",       #color of back of button
        foreground="#cdfaf5",       #color of text
        activebackground="grey",  #color of back of button activated
        activeforeground="black", #color of text activated
        highlightthickness=2,
        width=5,
        border=2,
        cursor="hand1",
        text="Add",
        font=("Arial",10,'bold'),
        command=lambda: [A80()]
        ).grid(row=3,column=3)
    tk.Button(
        main_frame,
        background="#002366",       #color of back of button
        foreground="#cdfaf5",       #color of text
        activebackground="grey",  #color of back of button activated
        activeforeground="black", #color of text activated
        highlightthickness=2,
        width=5,
        border=2,
        cursor="hand1",
        text="Add",
        font=("Arial",10,'bold'),
        command=lambda: [F27()]
        ).grid(row=4,column=3)
    tk.Button(
        main_frame,
        background="#002366",       #color of back of button
        foreground="#cdfaf5",       #color of text
        activebackground="grey",  #color of back of button activated
        activeforeground="black", #color of text activated
        highlightthickness=2,
        width=5,
        border=2,
        cursor="hand1",
        text="Add",
        font=("Arial",10,'bold'),
        command=lambda: [A3()]
        ).grid(row=5,column=3)
        
    tk.Button(
        main_frame,
        background="#002366",       #color of back of button
        foreground="#cdfaf5",       #color of text
        activebackground="grey",  #color of back of button activated
        activeforeground="black", #color of text activated
        highlightthickness=2,
        width=13,
        border=6,
        cursor="hand1",
        text="To Start",
        font=("Arial",20,'bold'),
        command=lambda: [root.destroy(),start()]
        ).place(relx=0.19, rely=0.55)
    
    tk.Button(
        main_frame,
        background="#002366",       #color of back of button
        foreground="#cdfaf5",       #color of text
        activebackground="grey",  #color of back of button activated
        activeforeground="black", #color of text activated
        highlightthickness=2,
        width=13,
        border=6,
        cursor="hand1",
        text="Close",
        font=("Arial",20,'bold'),
        command=lambda: [root.destroy(),close()]
        ).place(relx=0.53, rely=0.55)
    
    tk.Button(
        main_frame,
        background="#002366",       #color of back of button
        foreground="#cdfaf5",       #color of text
        activebackground="grey",  #color of back of button activated
        activeforeground="black", #color of text activated
        highlightthickness=2,
        width=13,
        border=6,
        cursor="hand1",
        text="Cart",
        font=("Arial",20,'bold'),
        command=lambda: [root.destroy(),Cart()]
        ).place(relx=0.19, rely=0.75)
    
    tk.Button(
        main_frame,
        background="#002366",       #color of back of button
        foreground="#cdfaf5",       #color of text
        activebackground="grey",  #color of back of button activated
        activeforeground="black", #color of text activated
        highlightthickness=2,
        width=13,
        border=6,
        cursor="hand1",
        text="Go Back",
        font=("Arial",20,'bold'),
        command=lambda: [root.destroy(),Android()]
        ).place(relx=0.53, rely=0.75)
    root.mainloop()
def FindX8():
    cur.execute("Select qty from cart where productname= 'OPPO Find X8';")
    for a in cur:
        for c in range(len(a)):
            cur.execute("update cart set qty=qty+1 where productname='OPPO Find X8';")
            db.commit()
def K12():
    cur.execute("Select qty from cart where productname= 'OPPO K12';")
    for a in cur:
        for c in range(len(a)):
            cur.execute("update cart set qty=qty+1 where productname='OPPO K12';")
            db.commit()
def A80():
    cur.execute("Select qty from cart where productname= 'OPPO A80';")
    for a in cur:
        for c in range(len(a)):
            cur.execute("update cart set qty=qty+1 where productname='OPPO A80';")
            db.commit()
def F27():
    cur.execute("Select qty from cart where productname= 'OPPO F27';")
    for a in cur:
        for c in range(len(a)):
            cur.execute("update cart set qty=qty+1 where productname='OPPO F27';")
            db.commit()
def A3():
    cur.execute("Select qty from cart where productname= 'OPPO A3';")
    for a in cur:
        for c in range(len(a)):
            cur.execute("update cart set qty=qty+1 where productname='OPPO A3';")
            db.commit()
def VIVO():
    root=tk.Tk()
    root.title("VIVO")
    root.geometry("740x450")
    root.resizable(width=False,height=False)
    cur.execute("select * from vivo")
    main_frame=tk.Frame(root,bg="#cdfaf5",pady=0) #background of button
    main_frame.pack(fill=tk.BOTH,expand=True)
    
    i=1
    c=tk.Label(
        main_frame,
        width=20,
        text="S. No.",
        borderwidth=3,
        relief="ridge",
        anchor="w",
        bg="yellow",
        font=("Ariel",15)).grid(row=0,column=0)
    c=tk.Label(
        main_frame,
        width=20,
        text="VIVO",
        borderwidth=3,
        relief="ridge",
        anchor="w",
        bg="yellow",
        font=("Ariel",15)).grid(row=0,column=1)
    c=tk.Label(
        main_frame,
        width=20,
        text="Price in Rs.",
        borderwidth=3,
        relief="ridge",
        anchor="w",
        bg="yellow",
        font=("Ariel",15)).grid(row=0,column=2)
    for a in cur:
        for b in range(len(a)):
            c=tk.Entry(main_frame,width=20,fg="blue",bg="white",borderwidth=3,font=("Ariel",15))
            c.grid(row=i,column=b)
            c.insert(tk.END,a[b])
        i=i+1
    tk.Button(
        main_frame,
        background="#002366",       #color of back of button
        foreground="#cdfaf5",       #color of text
        activebackground="grey",  #color of back of button activated
        activeforeground="black", #color of text activated
        highlightthickness=2,
        width=5,
        border=2,
        cursor="hand1",
        text="Add",
        font=("Arial",10,'bold'),
        command=lambda: [S20()]
        ).grid(row=1,column=3)
    tk.Button(
        main_frame,
        background="#002366",       #color of back of button
        foreground="#cdfaf5",       #color of text
        activebackground="grey",  #color of back of button activated
        activeforeground="black", #color of text activated
        highlightthickness=2,
        width=5,
        border=2,
        cursor="hand1",
        text="Add",
        font=("Arial",10,'bold'),
        command=lambda: [Y300()]
        ).grid(row=2,column=3)
    tk.Button(
        main_frame,
        background="#002366",       #color of back of button
        foreground="#cdfaf5",       #color of text
        activebackground="grey",  #color of back of button activated
        activeforeground="black", #color of text activated
        highlightthickness=2,
        width=5,
        border=2,
        cursor="hand1",
        text="Add",
        font=("Arial",10,'bold'),
        command=lambda: [X200()]
        ).grid(row=3,column=3)
    tk.Button(
        main_frame,
        background="#002366",       #color of back of button
        foreground="#cdfaf5",       #color of text
        activebackground="grey",  #color of back of button activated
        activeforeground="black", #color of text activated
        highlightthickness=2,
        width=5,
        border=2,
        cursor="hand1",
        text="Add",
        font=("Arial",10,'bold'),
        command=lambda: [T3Pro()]
        ).grid(row=4,column=3)
    tk.Button(
        main_frame,
        background="#002366",       #color of back of button
        foreground="#cdfaf5",       #color of text
        activebackground="grey",  #color of back of button activated
        activeforeground="black", #color of text activated
        highlightthickness=2,
        width=5,
        border=2,
        cursor="hand1",
        text="Add",
        font=("Arial",10,'bold'),
        command=lambda: [IQOOZ9s()]
        ).grid(row=5,column=3)
        
    tk.Button(
        main_frame,
        background="#002366",       #color of back of button
        foreground="#cdfaf5",       #color of text
        activebackground="grey",  #color of back of button activated
        activeforeground="black", #color of text activated
        highlightthickness=2,
        width=13,
        border=6,
        cursor="hand1",
        text="To Start",
        font=("Arial",20,'bold'),
        command=lambda: [root.destroy(),start()]
        ).place(relx=0.19, rely=0.55)
    
    tk.Button(
        main_frame,
        background="#002366",       #color of back of button
        foreground="#cdfaf5",       #color of text
        activebackground="grey",  #color of back of button activated
        activeforeground="black", #color of text activated
        highlightthickness=2,
        width=13,
        border=6,
        cursor="hand1",
        text="Close",
        font=("Arial",20,'bold'),
        command=lambda: [root.destroy(),close()]
        ).place(relx=0.53, rely=0.55)
    
    tk.Button(
        main_frame,
        background="#002366",       #color of back of button
        foreground="#cdfaf5",       #color of text
        activebackground="grey",  #color of back of button activated
        activeforeground="black", #color of text activated
        highlightthickness=2,
        width=13,
        border=6,
        cursor="hand1",
        text="Cart",
        font=("Arial",20,'bold'),
        command=lambda: [root.destroy(),Cart()]
        ).place(relx=0.19, rely=0.75)
    
    tk.Button(
        main_frame,
        background="#002366",       #color of back of button
        foreground="#cdfaf5",       #color of text
        activebackground="grey",  #color of back of button activated
        activeforeground="black", #color of text activated
        highlightthickness=2,
        width=13,
        border=6,
        cursor="hand1",
        text="Go Back",
        font=("Arial",20,'bold'),
        command=lambda: [root.destroy(),Android()]
        ).place(relx=0.53, rely=0.75)
    root.mainloop()
def S20():
    cur.execute("Select qty from cart where productname= 'VIVO S20';")
    for a in cur:
        for c in range(len(a)):
            cur.execute("update cart set qty=qty+1 where productname='VIVO S20';")
            db.commit()
def Y300():
    cur.execute("Select qty from cart where productname= 'VIVO Y300';")
    for a in cur:
        for c in range(len(a)):
            cur.execute("update cart set qty=qty+1 where productname='VIVO Y300';")
            db.commit()
def X200():
    cur.execute("Select qty from cart where productname= 'VIVO X200';")
    for a in cur:
        for c in range(len(a)):
            cur.execute("update cart set qty=qty+1 where productname='VIVO X200';")
            db.commit()
def T3Pro():
    cur.execute("Select qty from cart where productname= 'VIVO T3 Pro';")
    for a in cur:
        for c in range(len(a)):
            cur.execute("update cart set qty=qty+1 where productname='VIVO T3 Pro';")
            db.commit()
def IQOOZ9s():
    cur.execute("Select qty from cart where productname= 'VIVO IQOO Z9s';")
    for a in cur:
        for c in range(len(a)):
            cur.execute("update cart set qty=qty+1 where productname='VIVO IQOO Z9s';")
            db.commit()
def Pixel():
    root=tk.Tk()
    root.title("Google-Pixel")
    root.geometry("740x450")
    root.resizable(width=False,height=False)
    cur.execute("select * from pixel")
    main_frame=tk.Frame(root,bg="#cdfaf5",pady=0) #background of button
    main_frame.pack(fill=tk.BOTH,expand=True)
    
    i=1
    c=tk.Label(
        main_frame,
        width=20,
        text="S. No.",
        borderwidth=3,
        relief="ridge",
        anchor="w",
        bg="yellow",
        font=("Ariel",15)).grid(row=0,column=0)
    c=tk.Label(
        main_frame,
        width=20,
        text="Google-Pixel",
        borderwidth=3,
        relief="ridge",
        anchor="w",
        bg="yellow",
        font=("Ariel",15)).grid(row=0,column=1)
    c=tk.Label(
        main_frame,
        width=20,
        text="Price in Rs.",
        borderwidth=3,
        relief="ridge",
        anchor="w",
        bg="yellow",
        font=("Ariel",15)).grid(row=0,column=2)
    for a in cur:
        for b in range(len(a)):
            c=tk.Entry(main_frame,width=20,fg="blue",bg="white",borderwidth=3,font=("Ariel",15))
            c.grid(row=i,column=b)
            c.insert(tk.END,a[b])
        i=i+1
    tk.Button(
        main_frame,
        background="#002366",       #color of back of button
        foreground="#cdfaf5",       #color of text
        activebackground="grey",  #color of back of button activated
        activeforeground="black", #color of text activated
        highlightthickness=2,
        width=5,
        border=2,
        cursor="hand1",
        text="Add",
        font=("Arial",10,'bold'),
        command=lambda: [Pixel9Pro()]
        ).grid(row=1,column=3)
    tk.Button(
        main_frame,
        background="#002366",       #color of back of button
        foreground="#cdfaf5",       #color of text
        activebackground="grey",  #color of back of button activated
        activeforeground="black", #color of text activated
        highlightthickness=2,
        width=5,
        border=2,
        cursor="hand1",
        text="Add",
        font=("Arial",10,'bold'),
        command=lambda: [Pixel9ProFold()]
        ).grid(row=2,column=3)
    tk.Button(
        main_frame,
        background="#002366",       #color of back of button
        foreground="#cdfaf5",       #color of text
        activebackground="grey",  #color of back of button activated
        activeforeground="black", #color of text activated
        highlightthickness=2,
        width=5,
        border=2,
        cursor="hand1",
        text="Add",
        font=("Arial",10,'bold'),
        command=lambda: [Pixel8Pro()]
        ).grid(row=3,column=3)
    tk.Button(
        main_frame,
        background="#002366",       #color of back of button
        foreground="#cdfaf5",       #color of text
        activebackground="grey",  #color of back of button activated
        activeforeground="black", #color of text activated
        highlightthickness=2,
        width=5,
        border=2,
        cursor="hand1",
        text="Add",
        font=("Arial",10,'bold'),
        command=lambda: [Pixel8()]
        ).grid(row=4,column=3)
    tk.Button(
        main_frame,
        background="#002366",       #color of back of button
        foreground="#cdfaf5",       #color of text
        activebackground="grey",  #color of back of button activated
        activeforeground="black", #color of text activated
        highlightthickness=2,
        width=5,
        border=2,
        cursor="hand1",
        text="Add",
        font=("Arial",10,'bold'),
        command=lambda: [Pixel7()]
        ).grid(row=5,column=3)
        
    tk.Button(
        main_frame,
        background="#002366",       #color of back of button
        foreground="#cdfaf5",       #color of text
        activebackground="grey",  #color of back of button activated
        activeforeground="black", #color of text activated
        highlightthickness=2,
        width=13,
        border=6,
        cursor="hand1",
        text="To Start",
        font=("Arial",20,'bold'),
        command=lambda: [root.destroy(),start()]
        ).place(relx=0.19, rely=0.55)
    
    tk.Button(
        main_frame,
        background="#002366",       #color of back of button
        foreground="#cdfaf5",       #color of text
        activebackground="grey",  #color of back of button activated
        activeforeground="black", #color of text activated
        highlightthickness=2,
        width=13,
        border=6,
        cursor="hand1",
        text="Close",
        font=("Arial",20,'bold'),
        command=lambda: [root.destroy(),close()]
        ).place(relx=0.53, rely=0.55)
    
    tk.Button(
        main_frame,
        background="#002366",       #color of back of button
        foreground="#cdfaf5",       #color of text
        activebackground="grey",  #color of back of button activated
        activeforeground="black", #color of text activated
        highlightthickness=2,
        width=13,
        border=6,
        cursor="hand1",
        text="Cart",
        font=("Arial",20,'bold'),
        command=lambda: [root.destroy(),Cart()]
        ).place(relx=0.19, rely=0.75)
    
    tk.Button(
        main_frame,
        background="#002366",       #color of back of button
        foreground="#cdfaf5",       #color of text
        activebackground="grey",  #color of back of button activated
        activeforeground="black", #color of text activated
        highlightthickness=2,
        width=13,
        border=6,
        cursor="hand1",
        text="Go Back",
        font=("Arial",20,'bold'),
        command=lambda: [root.destroy(),Android()]
        ).place(relx=0.53, rely=0.75)
    root.mainloop()
def Pixel9Pro():
    cur.execute("Select qty from cart where productname= 'Google Pixel 9 Pro';")
    for a in cur:
        for c in range(len(a)):
            cur.execute("update cart set qty=qty+1 where productname='Google Pixel 9 Pro';")
            db.commit()
def Pixel9ProFold():
    cur.execute("Select qty from cart where productname= 'Google Pixel 9 Pro Fold';")
    for a in cur:
        for c in range(len(a)):
            cur.execute("update cart set qty=qty+1 where productname='Google Pixel 9 Pro Fold';")
            db.commit()
def Pixel8Pro():
    cur.execute("Select qty from cart where productname= 'Google Pixel 8 Pro';")
    for a in cur:
        for c in range(len(a)):
            cur.execute("update cart set qty=qty+1 where productname='Google Pixel 8 Pro';")
            db.commit()
def Pixel8():
    cur.execute("Select qty from cart where productname= 'Google Pixel 8';")
    for a in cur:
        for c in range(len(a)):
            cur.execute("update cart set qty=qty+1 where productname='Google Pixel 8';")
            db.commit()
def Pixel7():
    cur.execute("Select qty from cart where productname= 'Google Pixel 7';")
    for a in cur:
        for c in range(len(a)):
            cur.execute("update cart set qty=qty+1 where productname='Google Pixel 7';")
            db.commit()
def AppleIOS():
    root=tk.Tk()
    root.title("Apple IOS")
    root.geometry("740x450")
    root.resizable(width=False,height=False)
    cur.execute("select * from appleios")
    main_frame=tk.Frame(root,bg="#cdfaf5",pady=0) #background of button
    main_frame.pack(fill=tk.BOTH,expand=True)
    
    i=1
    c=tk.Label(
        main_frame,
        width=20,
        text="S. No.",
        borderwidth=3,
        relief="ridge",
        anchor="w",
        bg="yellow",
        font=("Ariel",15)).grid(row=0,column=0)
    c=tk.Label(
        main_frame,
        width=20,
        text="Apple iOS",
        borderwidth=3,
        relief="ridge",
        anchor="w",
        bg="yellow",
        font=("Ariel",15)).grid(row=0,column=1)
    c=tk.Label(
        main_frame,
        width=20,
        text="Price in Rs.",
        borderwidth=3,
        relief="ridge",
        anchor="w",
        bg="yellow",
        font=("Ariel",15)).grid(row=0,column=2)
    for a in cur:
        for b in range(len(a)):
            c=tk.Entry(main_frame,width=20,fg="blue",bg="white",borderwidth=3,font=("Ariel",15))
            c.grid(row=i,column=b)
            c.insert(tk.END,a[b])
        i=i+1
    tk.Button(
        main_frame,
        background="#002366",       #color of back of button
        foreground="#cdfaf5",       #color of text
        activebackground="grey",  #color of back of button activated
        activeforeground="black", #color of text activated
        highlightthickness=2,
        width=5,
        border=2,
        cursor="hand1",
        text="Add",
        font=("Arial",10,'bold'),
        command=lambda: [iPhone16()]
        ).grid(row=1,column=3)
    tk.Button(
        main_frame,
        background="#002366",       #color of back of button
        foreground="#cdfaf5",       #color of text
        activebackground="grey",  #color of back of button activated
        activeforeground="black", #color of text activated
        highlightthickness=2,
        width=5,
        border=2,
        cursor="hand1",
        text="Add",
        font=("Arial",10,'bold'),
        command=lambda: [iPhone15()]
        ).grid(row=2,column=3)
    tk.Button(
        main_frame,
        background="#002366",       #color of back of button
        foreground="#cdfaf5",       #color of text
        activebackground="grey",  #color of back of button activated
        activeforeground="black", #color of text activated
        highlightthickness=2,
        width=5,
        border=2,
        cursor="hand1",
        text="Add",
        font=("Arial",10,'bold'),
        command=lambda: [iPhone14()]
        ).grid(row=3,column=3)
    tk.Button(
        main_frame,
        background="#002366",       #color of back of button
        foreground="#cdfaf5",       #color of text
        activebackground="grey",  #color of back of button activated
        activeforeground="black", #color of text activated
        highlightthickness=2,
        width=5,
        border=2,
        cursor="hand1",
        text="Add",
        font=("Arial",10,'bold'),
        command=lambda: [iPhone13()]
        ).grid(row=4,column=3)
    tk.Button(
        main_frame,
        background="#002366",       #color of back of button
        foreground="#cdfaf5",       #color of text
        activebackground="grey",  #color of back of button activated
        activeforeground="black", #color of text activated
        highlightthickness=2,
        width=5,
        border=2,
        cursor="hand1",
        text="Add",
        font=("Arial",10,'bold'),
        command=lambda: [iPhone12()]
        ).grid(row=5,column=3)
        
    tk.Button(
        main_frame,
        background="#002366",       #color of back of button
        foreground="#cdfaf5",       #color of text
        activebackground="grey",  #color of back of button activated
        activeforeground="black", #color of text activated
        highlightthickness=2,
        width=13,
        border=6,
        cursor="hand1",
        text="To Start",
        font=("Arial",20,'bold'),
        command=lambda: [root.destroy(),start()]
        ).place(relx=0.19, rely=0.55)
    
    tk.Button(
        main_frame,
        background="#002366",       #color of back of button
        foreground="#cdfaf5",       #color of text
        activebackground="grey",  #color of back of button activated
        activeforeground="black", #color of text activated
        highlightthickness=2,
        width=13,
        border=6,
        cursor="hand1",
        text="Close",
        font=("Arial",20,'bold'),
        command=lambda: [root.destroy(),close()]
        ).place(relx=0.53, rely=0.55)
    
    tk.Button(
        main_frame,
        background="#002366",       #color of back of button
        foreground="#cdfaf5",       #color of text
        activebackground="grey",  #color of back of button activated
        activeforeground="black", #color of text activated
        highlightthickness=2,
        width=13,
        border=6,
        cursor="hand1",
        text="Cart",
        font=("Arial",20,'bold'),
        command=lambda: [root.destroy(),Cart()]
        ).place(relx=0.19, rely=0.75)
    
    tk.Button(
        main_frame,
        background="#002366",       #color of back of button
        foreground="#cdfaf5",       #color of text
        activebackground="grey",  #color of back of button activated
        activeforeground="black", #color of text activated
        highlightthickness=2,
        width=13,
        border=6,
        cursor="hand1",
        text="Go Back",
        font=("Arial",20,'bold'),
        command=lambda: [root.destroy(),mobile()]
        ).place(relx=0.53, rely=0.75)
    root.mainloop()
def iPhone16():
    cur.execute("Select qty from cart where productname= 'iPhone 16';")
    for a in cur:
        for c in range(len(a)):
            cur.execute("update cart set qty=qty+1 where productname='iPhone 16';")
            db.commit()
def iPhone15():
    cur.execute("Select qty from cart where productname= 'iPhone 15';")
    for a in cur:
        for c in range(len(a)):
            cur.execute("update cart set qty=qty+1 where productname='iPhone 15';")
            db.commit()
def iPhone14():
    cur.execute("Select qty from cart where productname= 'iPhone 14';")
    for a in cur:
        for c in range(len(a)):
            cur.execute("update cart set qty=qty+1 where productname='iPhone 14';")
            db.commit()
def iPhone13():
    cur.execute("Select qty from cart where productname= 'iPhone 13';")
    for a in cur:
        for c in range(len(a)):
            cur.execute("update cart set qty=qty+1 where productname='iPhone 13';")
            db.commit()
def iPhone12():
    cur.execute("Select qty from cart where productname= 'iPhone 12';")
    for a in cur:
        for c in range(len(a)):
            cur.execute("update cart set qty=qty+1 where productname='iPhone 12';")
            db.commit()
def BlackBerryOS():
    root=tk.Tk()
    root.title("BlackBerry OS")
    root.geometry("740x450")
    root.resizable(width=False,height=False)
    cur.execute("select * from blackberryos")
    main_frame=tk.Frame(root,bg="#cdfaf5",pady=0) #background of button
    main_frame.pack(fill=tk.BOTH,expand=True)
    
    i=1
    c=tk.Label(
        main_frame,
        width=20,
        text="S. No.",
        borderwidth=3,
        relief="ridge",
        anchor="w",
        bg="yellow",
        font=("Ariel",15)).grid(row=0,column=0)
    c=tk.Label(
        main_frame,
        width=20,
        text="BlackBerry OS",
        borderwidth=3,
        relief="ridge",
        anchor="w",
        bg="yellow",
        font=("Ariel",15)).grid(row=0,column=1)
    c=tk.Label(
        main_frame,
        width=20,
        text="Price in Rs.",
        borderwidth=3,
        relief="ridge",
        anchor="w",
        bg="yellow",
        font=("Ariel",15)).grid(row=0,column=2)
    for a in cur:
        for b in range(len(a)):
            c=tk.Entry(main_frame,width=20,fg="blue",bg="white",borderwidth=3,font=("Ariel",15))
            c.grid(row=i,column=b)
            c.insert(tk.END,a[b])
        i=i+1
    tk.Button(
        main_frame,
        background="#002366",       #color of back of button
        foreground="#cdfaf5",       #color of text
        activebackground="grey",  #color of back of button activated
        activeforeground="black", #color of text activated
        highlightthickness=2,
        width=5,
        border=2,
        cursor="hand1",
        text="Add",
        font=("Arial",10,'bold'),
        command=lambda: [Evolve()]
        ).grid(row=1,column=3)
    tk.Button(
        main_frame,
        background="#002366",       #color of back of button
        foreground="#cdfaf5",       #color of text
        activebackground="grey",  #color of back of button activated
        activeforeground="black", #color of text activated
        highlightthickness=2,
        width=5,
        border=2,
        cursor="hand1",
        text="Add",
        font=("Arial",10,'bold'),
        command=lambda: [Key2()]
        ).grid(row=2,column=3)
    tk.Button(
        main_frame,
        background="#002366",       #color of back of button
        foreground="#cdfaf5",       #color of text
        activebackground="grey",  #color of back of button activated
        activeforeground="black", #color of text activated
        highlightthickness=2,
        width=5,
        border=2,
        cursor="hand1",
        text="Add",
        font=("Arial",10,'bold'),
        command=lambda: [Motion()]
        ).grid(row=3,column=3)
    tk.Button(
        main_frame,
        background="#002366",       #color of back of button
        foreground="#cdfaf5",       #color of text
        activebackground="grey",  #color of back of button activated
        activeforeground="black", #color of text activated
        highlightthickness=2,
        width=5,
        border=2,
        cursor="hand1",
        text="Add",
        font=("Arial",10,'bold'),
        command=lambda: [Aurora()]
        ).grid(row=4,column=3)
    tk.Button(
        main_frame,
        background="#002366",       #color of back of button
        foreground="#cdfaf5",       #color of text
        activebackground="grey",  #color of back of button activated
        activeforeground="black", #color of text activated
        highlightthickness=2,
        width=5,
        border=2,
        cursor="hand1",
        text="Add",
        font=("Arial",10,'bold'),
        command=lambda: [KeyOne()]
        ).grid(row=5,column=3)
        
    tk.Button(
        main_frame,
        background="#002366",       #color of back of button
        foreground="#cdfaf5",       #color of text
        activebackground="grey",  #color of back of button activated
        activeforeground="black", #color of text activated
        highlightthickness=2,
        width=13,
        border=6,
        cursor="hand1",
        text="To Start",
        font=("Arial",20,'bold'),
        command=lambda: [root.destroy(),start()]
        ).place(relx=0.19, rely=0.55)
    
    tk.Button(
        main_frame,
        background="#002366",       #color of back of button
        foreground="#cdfaf5",       #color of text
        activebackground="grey",  #color of back of button activated
        activeforeground="black", #color of text activated
        highlightthickness=2,
        width=13,
        border=6,
        cursor="hand1",
        text="Close",
        font=("Arial",20,'bold'),
        command=lambda: [root.destroy(),close()]
        ).place(relx=0.53, rely=0.55)
    
    tk.Button(
        main_frame,
        background="#002366",       #color of back of button
        foreground="#cdfaf5",       #color of text
        activebackground="grey",  #color of back of button activated
        activeforeground="black", #color of text activated
        highlightthickness=2,
        width=13,
        border=6,
        cursor="hand1",
        text="Cart",
        font=("Arial",20,'bold'),
        command=lambda: [root.destroy(),Cart()]
        ).place(relx=0.19, rely=0.75)
    
    tk.Button(
        main_frame,
        background="#002366",       #color of back of button
        foreground="#cdfaf5",       #color of text
        activebackground="grey",  #color of back of button activated
        activeforeground="black", #color of text activated
        highlightthickness=2,
        width=13,
        border=6,
        cursor="hand1",
        text="Go Back",
        font=("Arial",20,'bold'),
        command=lambda: [root.destroy(),mobile()]
        ).place(relx=0.53, rely=0.75)
    root.mainloop()
def Evolve():
    cur.execute("Select qty from cart where productname= 'BlackBerry Evolve';")
    for a in cur:
        for c in range(len(a)):
            cur.execute("update cart set qty=qty+1 where productname='BlackBerry Evolve';")
            db.commit()
def Key2():
    cur.execute("Select qty from cart where productname= 'BlackBerry Key2';")
    for a in cur:
        for c in range(len(a)):
            cur.execute("update cart set qty=qty+1 where productname='BlackBerry Key2';")
            db.commit()
def Motion():
    cur.execute("Select qty from cart where productname= 'BlackBerry Motion';")
    for a in cur:
        for c in range(len(a)):
            cur.execute("update cart set qty=qty+1 where productname='BlackBerry Motion';")
            db.commit()
def Aurora():
    cur.execute("Select qty from cart where productname= 'BlackBerry Aurora';")
    for a in cur:
        for c in range(len(a)):
            cur.execute("update cart set qty=qty+1 where productname='BlackBerry Aurora';")
            db.commit()
def KeyOne():
    cur.execute("Select qty from cart where productname= 'BlackBerry KeyOne';")
    for a in cur:
        for c in range(len(a)):
            cur.execute("update cart set qty=qty+1 where productname='BlackBerry KeyOne';")
            db.commit()

#laptop function    
def laptop():
    root=tk.Tk()
    root.geometry("770x500")
    root.title("Laptop")
    root.resizable(width=False,height=False)

    main_frame=tk.Frame(root,bg="#cdfaf5",pady=40) #background of button
    main_frame.pack(fill=tk.BOTH,expand=True)
    tk.Label(
        main_frame,
        background="#cdfaf5",       #color of back of button
        foreground="black",       #color of text
        text="Which company would you like to select?",
        height=2,
        border=1,
        font=("Arial",25,"bold")).place(relx=0.5, rely=0, anchor=tk.N)
    button1=tk.Button(
        main_frame,
        background="#4169e1",     #color of back of button
        foreground="#cdfaf5",       #color of text
        activebackground="grey",  #color of back of button activated
        activeforeground="black", #color of text activated
        highlightthickness=2,
        width=12,
        height=2,
        border=10,
        cursor="hand1",
        text="Windows",
        font=("Arial",20,'bold'),   
        command=lambda: [root.destroy(),Windows()]
        ).place(relx=0.03, rely=0.25)

    button2=tk.Button(
        main_frame,
        background="#4169e1",     #color of back of button
        foreground="#cdfaf5",       #color of text
        activebackground="grey",  #color of back of button activated
        activeforeground="black", #color of text activated
        highlightthickness=2,
        width=12,
        height=2,
        border=10,
        cursor="hand1",
        text="Mac",
        font=("Arial",20,'bold'),
        command=lambda: [root.destroy(),Mac()]
        ).place(relx=0.35, rely=0.25)

    button3=tk.Button(
        main_frame,
        background="#4169e1",     #color of back of button
        foreground="#cdfaf5",       #color of text
        activebackground="grey",  #color of back of button activated
        activeforeground="black", #color of text activated
        highlightthickness=2,
        width=12,
        height=2,
        border=10,
        cursor="hand1",
        text="Asus",
        font=("Arial",20,'bold'),
        command=lambda: [root.destroy(),ASUS()]
        ).place(relx=0.67, rely=0.25)
    
    button4=tk.Button(
        main_frame,
        background="#002366",       #color of back of button
        foreground="#cdfaf5",       #color of text
        activebackground="grey",  #color of back of button activated
        activeforeground="black", #color of text activated
        highlightthickness=2,
        width=12,
        height=2,
        border=10,
        cursor="hand1",
        text="To Start",
        font=("Arial",20,'bold'),
        command=lambda: [root.destroy(),start()]
        ).place(relx=0.35, rely=0.55)
    
    button5=tk.Button(
        main_frame,
        background="#002366",       #color of back of button
        foreground="#cdfaf5",       #color of text
        activebackground="grey",  #color of back of button activated
        activeforeground="black", #color of text activated
        highlightthickness=2,
        width=12,
        height=2,
        border=10,
        cursor="hand1",
        text="Close",
        font=("Arial",20,'bold'),
        command=lambda: [root.destroy(),close()]
        ).place(relx=0.67, rely=0.55)
    button6=tk.Button(
        main_frame,
        background="#002366",       #color of back of button
        foreground="#cdfaf5",       #color of text
        activebackground="grey",  #color of back of button activated
        activeforeground="black", #color of text activated
        highlightthickness=2,
        width=12,
        height=2,
        border=10,
        cursor="hand1",
        text="Cart",
        font=("Arial",20,'bold'),
        command=lambda: [root.destroy(),Cart()]
        ).place(relx=0.03, rely=0.55)
    root.mainloop()
    
    root.mainloop()

def Windows():
    root=tk.Tk()
    root.title("Windows")
    root.geometry("740x450")
    root.resizable(width=False,height=False)
    cur.execute("select * from windows")
    main_frame=tk.Frame(root,bg="#cdfaf5",pady=0) #background of button
    main_frame.pack(fill=tk.BOTH,expand=True)
    
    i=1
    c=tk.Label(
        main_frame,
        width=26,
        text="S. No.",
        borderwidth=3,
        relief="ridge",
        anchor="w",
        bg="yellow",
        font=("Ariel",10)).grid(row=0,column=0)
    c=tk.Label(
        main_frame,
        width=26,
        text="Windows",
        borderwidth=3,
        relief="ridge",
        anchor="w",
        bg="yellow",
        font=("Ariel",10)).grid(row=0,column=1)
    c=tk.Label(
        main_frame,
        width=26,
        text="Price in Rs.",
        borderwidth=3,
        relief="ridge",
        anchor="w",
        bg="yellow",
        font=("Ariel",10)).grid(row=0,column=2)
    for a in cur:
        for b in range(len(a)):
            c=tk.Entry(main_frame,width=26,fg="blue",bg="white",borderwidth=3,font=("Ariel",11))
            c.grid(row=i,column=b)
            c.insert(tk.END,a[b])
        i=i+1
    tk.Button(
        main_frame,
        background="#002366",       #color of back of button
        foreground="#cdfaf5",       #color of text
        activebackground="grey",  #color of back of button activated
        activeforeground="black", #color of text activated
        highlightthickness=2,
        width=5,
        border=1,
        cursor="hand1",
        text="Add",
        font=("Arial",9,'bold'),
        command=lambda: [LenovoIdeaPad312thGen()]
        ).grid(row=1,column=3)
    tk.Button(
        main_frame,
        background="#002366",       #color of back of button
        foreground="#cdfaf5",       #color of text
        activebackground="grey",  #color of back of button activated
        activeforeground="black", #color of text activated
        highlightthickness=2,
        width=5,
        border=1,
        cursor="hand1",
        text="Add",
        font=("Arial",9,'bold'),
        command=lambda: [Dell1513thGen()]
        ).grid(row=2,column=3)
    tk.Button(
        main_frame,
        background="#002366",       #color of back of button
        foreground="#cdfaf5",       #color of text
        activebackground="grey",  #color of back of button activated
        activeforeground="black", #color of text activated
        highlightthickness=2,
        width=5,
        border=1,
        cursor="hand1",
        text="Add",
        font=("Arial",9,'bold'),
        command=lambda: [HPEliteBook820G47thGen()]
        ).grid(row=3,column=3)
    tk.Button(
        main_frame,
        background="#002366",       #color of back of button
        foreground="#cdfaf5",       #color of text
        activebackground="grey",  #color of back of button activated
        activeforeground="black", #color of text activated
        highlightthickness=2,
        width=5,
        border=1,
        cursor="hand1",
        text="Add",
        font=("Arial",9,'bold'),
        command=lambda: [AcerOne11IntelCeleronN4500()]
        ).grid(row=4,column=3)
    tk.Button(
        main_frame,
        background="#002366",       #color of back of button
        foreground="#cdfaf5",       #color of text
        activebackground="grey",  #color of back of button activated
        activeforeground="black", #color of text activated
        highlightthickness=2,
        width=5,
        border=1,
        cursor="hand1",
        text="Add",
        font=("Arial",9,'bold'),
        command=lambda: [HPLaptop255G9()]
        ).grid(row=5,column=3)
        
    tk.Button(
        main_frame,
        background="#002366",       #color of back of button
        foreground="#cdfaf5",       #color of text
        activebackground="grey",  #color of back of button activated
        activeforeground="black", #color of text activated
        highlightthickness=2,
        width=13,
        border=6,
        cursor="hand1",
        text="To Start",
        font=("Arial",20,'bold'),
        command=lambda: [root.destroy(),start()]
        ).place(relx=0.19, rely=0.55)
    
    tk.Button(
        main_frame,
        background="#002366",       #color of back of button
        foreground="#cdfaf5",       #color of text
        activebackground="grey",  #color of back of button activated
        activeforeground="black", #color of text activated
        highlightthickness=2,
        width=13,
        border=6,
        cursor="hand1",
        text="Close",
        font=("Arial",20,'bold'),
        command=lambda: [root.destroy(),close()]
        ).place(relx=0.53, rely=0.55)
    
    tk.Button(
        main_frame,
        background="#002366",       #color of back of button
        foreground="#cdfaf5",       #color of text
        activebackground="grey",  #color of back of button activated
        activeforeground="black", #color of text activated
        highlightthickness=2,
        width=13,
        border=6,
        cursor="hand1",
        text="Cart",
        font=("Arial",20,'bold'),
        command=lambda: [root.destroy(),Cart()]
        ).place(relx=0.19, rely=0.75)
    
    tk.Button(
        main_frame,
        background="#002366",       #color of back of button
        foreground="#cdfaf5",       #color of text
        activebackground="grey",  #color of back of button activated
        activeforeground="black", #color of text activated
        highlightthickness=2,
        width=13,
        border=6,
        cursor="hand1",
        text="Go Back",
        font=("Arial",20,'bold'),
        command=lambda: [root.destroy(),laptop()]
        ).place(relx=0.53, rely=0.75)
    root.mainloop()
def LenovoIdeaPad312thGen():
    cur.execute("Select qty from cart where productname= 'Windows Lenovo IdeaPad 3 12th Gen';")
    for a in cur:
        for c in range(len(a)):
            cur.execute("update cart set qty=qty+1 where productname='Windows Lenovo IdeaPad 3 12th Gen';")
            db.commit()
def Dell1513thGen():
    cur.execute("Select qty from cart where productname= 'Windows Dell 15 13th Gen';")
    for a in cur:
        for c in range(len(a)):
            cur.execute("update cart set qty=qty+1 where productname='Windows Dell 15 13th Gen';")
            db.commit()
def HPEliteBook820G47thGen():
    cur.execute("Select qty from cart where productname= 'Windows HP EliteBook 820 G4 7th Gen';")
    for a in cur:
        for c in range(len(a)):
            cur.execute("update cart set qty=qty+1 where productname='Windows HP EliteBook 820 G4 7th Gen';")
            db.commit()
def AcerOne11IntelCeleronN4500():
    cur.execute("Select qty from cart where productname= 'Windows Acer One 11 Intel Celeron N4500';")
    for a in cur:
        for c in range(len(a)):
            cur.execute("update cart set qty=qty+1 where productname='Windows Acer One 11 Intel Celeron N4500';")
            db.commit()
def HPLaptop255G9():
    cur.execute("Select qty from cart where productname= 'Windows HP Laptop 255 G9';")
    for a in cur:
        for c in range(len(a)):
            cur.execute("update cart set qty=qty+1 where productname='Windows HP Laptop 255 G9';")
            db.commit()
def Mac():
    root=tk.Tk()
    root.title("Mac")
    root.geometry("740x450")
    root.resizable(width=False,height=False)
    cur.execute("select * from macos")
    main_frame=tk.Frame(root,bg="#cdfaf5",pady=0) #background of button
    main_frame.pack(fill=tk.BOTH,expand=True)
    
    i=1
    c=tk.Label(
        main_frame,
        width=25,
        text="S. No.",
        borderwidth=3,
        relief="ridge",
        anchor="w",
        bg="yellow",
        font=("Ariel",10)).grid(row=0,column=0)
    c=tk.Label(
        main_frame,
        width=25,
        text="Mac",
        borderwidth=3,
        relief="ridge",
        anchor="w",
        bg="yellow",
        font=("Ariel",10)).grid(row=0,column=1)
    c=tk.Label(
        main_frame,
        width=25,
        text="Price in Rs.",
        borderwidth=3,
        relief="ridge",
        anchor="w",
        bg="yellow",
        font=("Ariel",10)).grid(row=0,column=2)
    for a in cur:
        for b in range(len(a)):
            c=tk.Entry(main_frame,width=25,fg="blue",bg="white",borderwidth=3,font=("Ariel",11))
            c.grid(row=i,column=b)
            c.insert(tk.END,a[b])
        i=i+1
    tk.Button(
        main_frame,
        background="#002366",       #color of back of button
        foreground="#cdfaf5",       #color of text
        activebackground="grey",  #color of back of button activated
        activeforeground="black", #color of text activated
        highlightthickness=2,
        width=5,
        border=1,
        cursor="hand1",
        text="Add",
        font=("Arial",9,'bold'),
        command=lambda: [Pro16InchM4Max()]
        ).grid(row=1,column=3)
    tk.Button(
        main_frame,
        background="#002366",       #color of back of button
        foreground="#cdfaf5",       #color of text
        activebackground="grey",  #color of back of button activated
        activeforeground="black", #color of text activated
        highlightthickness=2,
        width=5,
        border=1,
        cursor="hand1",
        text="Add",
        font=("Arial",9,'bold'),
        command=lambda: [Pro16InchM4Pro()]
        ).grid(row=2,column=3)
    tk.Button(
        main_frame,
        background="#002366",       #color of back of button
        foreground="#cdfaf5",       #color of text
        activebackground="grey",  #color of back of button activated
        activeforeground="black", #color of text activated
        highlightthickness=2,
        width=5,
        border=1,
        cursor="hand1",
        text="Add",
        font=("Arial",9,'bold'),
        command=lambda: [Pro14InchM4Max()]
        ).grid(row=3,column=3)
    tk.Button(
        main_frame,
        background="#002366",       #color of back of button
        foreground="#cdfaf5",       #color of text
        activebackground="grey",  #color of back of button activated
        activeforeground="black", #color of text activated
        highlightthickness=2,
        width=5,
        border=1,
        cursor="hand1",
        text="Add",
        font=("Arial",9,'bold'),
        command=lambda: [Pro14InchM4Pro()]
        ).grid(row=4,column=3)
    tk.Button(
        main_frame,
        background="#002366",       #color of back of button
        foreground="#cdfaf5",       #color of text
        activebackground="grey",  #color of back of button activated
        activeforeground="black", #color of text activated
        highlightthickness=2,
        width=5,
        border=1,
        cursor="hand1",
        text="Add",
        font=("Arial",9,'bold'),
        command=lambda: [Pro15InchM3()]
        ).grid(row=5,column=3)
    tk.Button(
        main_frame,
        background="#002366",       #color of back of button
        foreground="#cdfaf5",       #color of text
        activebackground="grey",  #color of back of button activated
        activeforeground="black", #color of text activated
        highlightthickness=2,
        width=5,
        border=1,
        cursor="hand1",
        text="Add",
        font=("Arial",9,'bold'),
        command=lambda: [Pro13InchM3()]
        ).grid(row=6,column=3)
        
    tk.Button(
        main_frame,
        background="#002366",       #color of back of button
        foreground="#cdfaf5",       #color of text
        activebackground="grey",  #color of back of button activated
        activeforeground="black", #color of text activated
        highlightthickness=2,
        width=13,
        border=6,
        cursor="hand1",
        text="To Start",
        font=("Arial",20,'bold'),
        command=lambda: [root.destroy(),start()]
        ).place(relx=0.19, rely=0.55)
    
    tk.Button(
        main_frame,
        background="#002366",       #color of back of button
        foreground="#cdfaf5",       #color of text
        activebackground="grey",  #color of back of button activated
        activeforeground="black", #color of text activated
        highlightthickness=2,
        width=13,
        border=6,
        cursor="hand1",
        text="Close",
        font=("Arial",20,'bold'),
        command=lambda: [root.destroy(),close()]
        ).place(relx=0.53, rely=0.55)
    
    tk.Button(
        main_frame,
        background="#002366",       #color of back of button
        foreground="#cdfaf5",       #color of text
        activebackground="grey",  #color of back of button activated
        activeforeground="black", #color of text activated
        highlightthickness=2,
        width=13,
        border=6,
        cursor="hand1",
        text="Cart",
        font=("Arial",20,'bold'),
        command=lambda: [root.destroy(),Cart()]
        ).place(relx=0.19, rely=0.75)
    
    tk.Button(
        main_frame,
        background="#002366",       #color of back of button
        foreground="#cdfaf5",       #color of text
        activebackground="grey",  #color of back of button activated
        activeforeground="black", #color of text activated
        highlightthickness=2,
        width=13,
        border=6,
        cursor="hand1",
        text="Go Back",
        font=("Arial",20,'bold'),
        command=lambda: [root.destroy(),laptop()]
        ).place(relx=0.53, rely=0.75)
    root.mainloop()
def Pro16InchM4Max():
    cur.execute("Select qty from cart where productname= 'MacBook Pro 16-inch(M4 Max)';")
    for a in cur:
        for c in range(len(a)):
            cur.execute("update cart set qty=qty+1 where productname='MacBook Pro 16-inch(M4 Max)';")
            db.commit()
def Pro16InchM4Pro():
    cur.execute("Select qty from cart where productname= 'MacBook Pro 16-inch(M4 Pro)';")
    for a in cur:
        for c in range(len(a)):
            cur.execute("update cart set qty=qty+1 where productname='MacBook Pro 16-inch(M4 Pro)';")
            db.commit()
def Pro14InchM4Max():
    cur.execute("Select qty from cart where productname= 'MacBook Pro 14-inch(M4 Max)';")
    for a in cur:
        for c in range(len(a)):
            cur.execute("update cart set qty=qty+1 where productname='MacBook Pro 14-inch(M4 Max)';")
            db.commit()
def Pro14InchM4Pro():
    cur.execute("Select qty from cart where productname= 'MacBook Pro 14-inch(M4 Pro)';")
    for a in cur:
        for c in range(len(a)):
            cur.execute("update cart set qty=qty+1 where productname='MacBook Pro 14-inch(M4 Pro)';")
            db.commit()
def Pro15InchM3():
    cur.execute("Select qty from cart where productname= 'MacBook Pro 15-inch(M3)';")
    for a in cur:
        for c in range(len(a)):
            cur.execute("update cart set qty=qty+1 where productname='MacBook Pro 15-inch(M3)';")
            db.commit()
def Pro13InchM3():
    cur.execute("Select qty from cart where productname= 'MacBook Pro 13-inch(M3)';")
    for a in cur:
        for c in range(len(a)):
            cur.execute("update cart set qty=qty+1 where productname='MacBook Pro 13-inch(M3)';")
            db.commit()
def ASUS():
    root=tk.Tk()
    root.title("ASUS")
    root.geometry("740x450")
    root.resizable(width=False,height=False)
    cur.execute("select * from asus")
    main_frame=tk.Frame(root,bg="#cdfaf5",pady=0) #background of button
    main_frame.pack(fill=tk.BOTH,expand=True)
    
    i=1
    c=tk.Label(
        main_frame,
        width=24,
        text="S. No.",
        borderwidth=3,
        relief="ridge",
        anchor="w",
        bg="yellow",
        font=("Ariel",13)).grid(row=0,column=0)
    c=tk.Label(
        main_frame,
        width=24,
        text="ASUS",
        borderwidth=3,
        relief="ridge",
        anchor="w",
        bg="yellow",
        font=("Ariel",13)).grid(row=0,column=1)
    c=tk.Label(
        main_frame,
        width=24,
        text="Price in Rs.",
        borderwidth=3,
        relief="ridge",
        anchor="w",
        bg="yellow",
        font=("Ariel",13)).grid(row=0,column=2)
    for a in cur:
        for b in range(len(a)):
            c=tk.Entry(main_frame,width=24,fg="blue",bg="white",borderwidth=3,font=("Ariel",13))
            c.grid(row=i,column=b)
            c.insert(tk.END,a[b])
        i=i+1
    tk.Button(
        main_frame,
        background="#002366",       #color of back of button
        foreground="#cdfaf5",       #color of text
        activebackground="grey",  #color of back of button activated
        activeforeground="black", #color of text activated
        highlightthickness=2,
        width=5,
        border=1,
        cursor="hand1",
        text="Add",
        font=("Arial",9,'bold'),
        command=lambda: [ZenbookS14()]
        ).grid(row=1,column=3)
    tk.Button(
        main_frame,
        background="#002366",       #color of back of button
        foreground="#cdfaf5",       #color of text
        activebackground="grey",  #color of back of button activated
        activeforeground="black", #color of text activated
        highlightthickness=2,
        width=5,
        border=1,
        cursor="hand1",
        text="Add",
        font=("Arial",9,'bold'),
        command=lambda: [ROGZephyrusG16()]
        ).grid(row=2,column=3)
    tk.Button(
        main_frame,
        background="#002366",       #color of back of button
        foreground="#cdfaf5",       #color of text
        activebackground="grey",  #color of back of button activated
        activeforeground="black", #color of text activated
        highlightthickness=2,
        width=5,
        border=1,
        cursor="hand1",
        text="Add",
        font=("Arial",9,'bold'),
        command=lambda: [ROGZephyrusG14()]
        ).grid(row=3,column=3)
    tk.Button(
        main_frame,
        background="#002366",       #color of back of button
        foreground="#cdfaf5",       #color of text
        activebackground="grey",  #color of back of button activated
        activeforeground="black", #color of text activated
        highlightthickness=2,
        width=5,
        border=1,
        cursor="hand1",
        text="Add",
        font=("Arial",9,'bold'),
        command=lambda: [ProArtPX13()]
        ).grid(row=4,column=3)
    tk.Button(
        main_frame,
        background="#002366",       #color of back of button
        foreground="#cdfaf5",       #color of text
        activebackground="grey",  #color of back of button activated
        activeforeground="black", #color of text activated
        highlightthickness=2,
        width=5,
        border=1,
        cursor="hand1",
        text="Add",
        font=("Arial",9,'bold'),
        command=lambda: [TUFGaminA14()]
        ).grid(row=5,column=3)
        
    tk.Button(
        main_frame,
        background="#002366",       #color of back of button
        foreground="#cdfaf5",       #color of text
        activebackground="grey",  #color of back of button activated
        activeforeground="black", #color of text activated
        highlightthickness=2,
        width=13,
        border=6,
        cursor="hand1",
        text="To Start",
        font=("Arial",20,'bold'),
        command=lambda: [root.destroy(),start()]
        ).place(relx=0.19, rely=0.55)
    
    tk.Button(
        main_frame,
        background="#002366",       #color of back of button
        foreground="#cdfaf5",       #color of text
        activebackground="grey",  #color of back of button activated
        activeforeground="black", #color of text activated
        highlightthickness=2,
        width=13,
        border=6,
        cursor="hand1",
        text="Close",
        font=("Arial",20,'bold'),
        command=lambda: [root.destroy(),close()]
        ).place(relx=0.53, rely=0.55)
    
    tk.Button(
        main_frame,
        background="#002366",       #color of back of button
        foreground="#cdfaf5",       #color of text
        activebackground="grey",  #color of back of button activated
        activeforeground="black", #color of text activated
        highlightthickness=2,
        width=13,
        border=6,
        cursor="hand1",
        text="Cart",
        font=("Arial",20,'bold'),
        command=lambda: [root.destroy(),Cart()]
        ).place(relx=0.19, rely=0.75)
    
    tk.Button(
        main_frame,
        background="#002366",       #color of back of button
        foreground="#cdfaf5",       #color of text
        activebackground="grey",  #color of back of button activated
        activeforeground="black", #color of text activated
        highlightthickness=2,
        width=13,
        border=6,
        cursor="hand1",
        text="Go Back",
        font=("Arial",20,'bold'),
        command=lambda: [root.destroy(),laptop()]
        ).place(relx=0.53, rely=0.75)
    root.mainloop()
def ZenbookS14():
    cur.execute("Select qty from cart where productname= 'ASUS Zenbook S 14';")
    for a in cur:
        for c in range(len(a)):
            cur.execute("update cart set qty=qty+1 where productname='ASUS Zenbook S 14';")
            db.commit()
def ROGZephyrusG16():
    cur.execute("Select qty from cart where productname= 'ASUS ROG Zephyrus G16';")
    for a in cur:
        for c in range(len(a)):
            cur.execute("update cart set qty=qty+1 where productname='ASUS ROG Zephyrus G16';")
            db.commit()
def ROGZephyrusG14():
    cur.execute("Select qty from cart where productname= 'ASUS ROG Zephyrus G14';")
    for a in cur:
        for c in range(len(a)):
            cur.execute("update cart set qty=qty+1 where productname='ASUS ROG Zephyrus G14';")
            db.commit()
def ProArtPX13():
    cur.execute("Select qty from cart where productname= 'ASUS ProArt PX13';")
    for a in cur:
        for c in range(len(a)):
            cur.execute("update cart set qty=qty+1 where productname='ASUS ProArt PX13';")
            db.commit()
def TUFGaminA14():
    cur.execute("Select qty from cart where productname= 'ASUS TUF Gaming A14';")
    for a in cur:
        for c in range(len(a)):
            cur.execute("update cart set qty=qty+1 where productname='ASUS TUF Gaming A14';")
            db.commit()
#Console function    
def Console():
    root=tk.Tk()
    root.geometry("770x500")
    root.title("Console")
    root.resizable(width=False,height=False)

    main_frame=tk.Frame(root,bg="#cdfaf5",pady=40) #background of button
    main_frame.pack(fill=tk.BOTH,expand=True)
    tk.Label(
        main_frame,
        background="#cdfaf5",       #color of back of button
        foreground="black",       #color of text
        text="Which company would you like to select?",
        height=2,
        border=1,
        font=("Arial",25,"bold")).place(relx=0.5, rely=0, anchor=tk.N)
    button1=tk.Button(
        main_frame,
        background="#4169e1",     #color of back of button
        foreground="#cdfaf5",       #color of text
        activebackground="grey",  #color of back of button activated
        activeforeground="black", #color of text activated
        highlightthickness=2,
        width=12,
        height=2,
        border=10,
        cursor="hand1",
        text="PlayStation",
        font=("Arial",20,'bold'),   
        command=lambda: [root.destroy(),Playstation()]
        ).place(relx=0.03, rely=0.25)

    button2=tk.Button(
        main_frame,
        background="#4169e1",     #color of back of button
        foreground="#cdfaf5",       #color of text
        activebackground="grey",  #color of back of button activated
        activeforeground="black", #color of text activated
        highlightthickness=2,
        width=12,
        height=2,
        border=10,
        cursor="hand1",
        text="Xbox",
        font=("Arial",20,'bold'),
        command=lambda: [root.destroy(),Xbox()]
        ).place(relx=0.35, rely=0.25)

    button3=tk.Button(
        main_frame,
        background="#4169e1",     #color of back of button
        foreground="#cdfaf5",       #color of text
        activebackground="grey",  #color of back of button activated
        activeforeground="black", #color of text activated
        highlightthickness=2,
        width=12,
        height=2,
        border=10,
        cursor="hand1",
        text="Nintendo",
        font=("Arial",20,'bold'),
        command=lambda: [root.destroy(),Nintendo()]
        ).place(relx=0.67, rely=0.25)
    
    button4=tk.Button(
        main_frame,
        background="#002366",       #color of back of button
        foreground="#cdfaf5",       #color of text
        activebackground="grey",  #color of back of button activated
        activeforeground="black", #color of text activated
        highlightthickness=2,
        width=12,
        height=2,
        border=10,
        cursor="hand1",
        text="To Start",
        font=("Arial",20,'bold'),
        command=lambda: [root.destroy(),start()]
        ).place(relx=0.35, rely=0.55)
    
    button5=tk.Button(
        main_frame,
        background="#002366",       #color of back of button
        foreground="#cdfaf5",       #color of text
        activebackground="grey",  #color of back of button activated
        activeforeground="black", #color of text activated
        highlightthickness=2,
        width=12,
        height=2,
        border=10,
        cursor="hand1",
        text="Close",
        font=("Arial",20,'bold'),
        command=lambda: [root.destroy(),close()]
        ).place(relx=0.67, rely=0.55)
    button6=tk.Button(
        main_frame,
        background="#002366",       #color of back of button
        foreground="#cdfaf5",       #color of text
        activebackground="grey",  #color of back of button activated
        activeforeground="black", #color of text activated
        highlightthickness=2,
        width=12,
        height=2,
        border=10,
        cursor="hand1",
        text="Cart",
        font=("Arial",20,'bold'),
        command=lambda: [root.destroy(),Cart()]
        ).place(relx=0.03, rely=0.55)
    root.mainloop()

def Playstation():
    root=tk.Tk()
    root.title("PlayStation")
    root.geometry("740x450")
    root.resizable(width=False,height=False)
    cur.execute("select * from playstation")
    main_frame=tk.Frame(root,bg="#cdfaf5",pady=0) #background of button
    main_frame.pack(fill=tk.BOTH,expand=True)
    
    i=1
    c=tk.Label(
        main_frame,
        width=24,
        text="S. No.",
        borderwidth=3,
        relief="ridge",
        anchor="w",
        bg="yellow",
        font=("Ariel",13)).grid(row=0,column=0)
    c=tk.Label(
        main_frame,
        width=24,
        text="PlayStation",
        borderwidth=3,
        relief="ridge",
        anchor="w",
        bg="yellow",
        font=("Ariel",13)).grid(row=0,column=1)
    c=tk.Label(
        main_frame,
        width=24,
        text="Price in Rs.",
        borderwidth=3,
        relief="ridge",
        anchor="w",
        bg="yellow",
        font=("Ariel",13)).grid(row=0,column=2)
    for a in cur:
        for b in range(len(a)):
            c=tk.Entry(main_frame,width=24,fg="blue",bg="white",borderwidth=3,font=("Ariel",13))
            c.grid(row=i,column=b)
            c.insert(tk.END,a[b])
        i=i+1
    tk.Button(
        main_frame,
        background="#002366",       #color of back of button
        foreground="#cdfaf5",       #color of text
        activebackground="grey",  #color of back of button activated
        activeforeground="black", #color of text activated
        highlightthickness=2,
        width=5,
        border=1,
        cursor="hand1",
        text="Add",
        font=("Arial",9,'bold'),
        command=lambda: [PlayStation5Console()]
        ).grid(row=1,column=3)
    tk.Button(
        main_frame,
        background="#002366",       #color of back of button
        foreground="#cdfaf5",       #color of text
        activebackground="grey",  #color of back of button activated
        activeforeground="black", #color of text activated
        highlightthickness=2,
        width=5,
        border=1,
        cursor="hand1",
        text="Add",
        font=("Arial",9,'bold'),
        command=lambda: [PlayStation5DigitalEdition()]
        ).grid(row=2,column=3)
    tk.Button(
        main_frame,
        background="#002366",       #color of back of button
        foreground="#cdfaf5",       #color of text
        activebackground="grey",  #color of back of button activated
        activeforeground="black", #color of text activated
        highlightthickness=2,
        width=5,
        border=1,
        cursor="hand1",
        text="Add",
        font=("Arial",9,'bold'),
        command=lambda: [PlayStation4Slim()]
        ).grid(row=3,column=3)
    tk.Button(
        main_frame,
        background="#002366",       #color of back of button
        foreground="#cdfaf5",       #color of text
        activebackground="grey",  #color of back of button activated
        activeforeground="black", #color of text activated
        highlightthickness=2,
        width=5,
        border=1,
        cursor="hand1",
        text="Add",
        font=("Arial",9,'bold'),
        command=lambda: [PlayStation4Pro()]
        ).grid(row=4,column=3)
    tk.Button(
        main_frame,
        background="#002366",       #color of back of button
        foreground="#cdfaf5",       #color of text
        activebackground="grey",  #color of back of button activated
        activeforeground="black", #color of text activated
        highlightthickness=2,
        width=5,
        border=1,
        cursor="hand1",
        text="Add",
        font=("Arial",9,'bold'),
        command=lambda: [PlayStation3()]
        ).grid(row=5,column=3)
        
    tk.Button(
        main_frame,
        background="#002366",       #color of back of button
        foreground="#cdfaf5",       #color of text
        activebackground="grey",  #color of back of button activated
        activeforeground="black", #color of text activated
        highlightthickness=2,
        width=13,
        border=6,
        cursor="hand1",
        text="To Start",
        font=("Arial",20,'bold'),
        command=lambda: [root.destroy(),start()]
        ).place(relx=0.19, rely=0.55)
    
    tk.Button(
        main_frame,
        background="#002366",       #color of back of button
        foreground="#cdfaf5",       #color of text
        activebackground="grey",  #color of back of button activated
        activeforeground="black", #color of text activated
        highlightthickness=2,
        width=13,
        border=6,
        cursor="hand1",
        text="Close",
        font=("Arial",20,'bold'),
        command=lambda: [root.destroy(),close()]
        ).place(relx=0.53, rely=0.55)
    
    tk.Button(
        main_frame,
        background="#002366",       #color of back of button
        foreground="#cdfaf5",       #color of text
        activebackground="grey",  #color of back of button activated
        activeforeground="black", #color of text activated
        highlightthickness=2,
        width=13,
        border=6,
        cursor="hand1",
        text="Cart",
        font=("Arial",20,'bold'),
        command=lambda: [root.destroy(),Cart()]
        ).place(relx=0.19, rely=0.75)
    
    tk.Button(
        main_frame,
        background="#002366",       #color of back of button
        foreground="#cdfaf5",       #color of text
        activebackground="grey",  #color of back of button activated
        activeforeground="black", #color of text activated
        highlightthickness=2,
        width=13,
        border=6,
        cursor="hand1",
        text="Go Back",
        font=("Arial",20,'bold'),
        command=lambda: [root.destroy(),Console()]
        ).place(relx=0.53, rely=0.75)
    root.mainloop()
def PlayStation5Console():
    cur.execute("Select qty from cart where productname= 'sony playstation 5 console';")
    for a in cur:
        for c in range(len(a)):
            cur.execute("update cart set qty=qty+1 where productname='sony playstation 5 console';")
            db.commit()
def PlayStation5DigitalEdition():
    cur.execute("Select qty from cart where productname= 'SONY PlayStation 5 Digital Edition';")
    for a in cur:
        for c in range(len(a)):
            cur.execute("update cart set qty=qty+1 where productname='SONY PlayStation 5 Digital Edition';")
            db.commit()
def PlayStation4Slim():
    cur.execute("Select qty from cart where productname= 'SONY PlayStation 4 Slim';")
    for a in cur:
        for c in range(len(a)):
            cur.execute("update cart set qty=qty+1 where productname='SONY PlayStation 4 Slim';")
            db.commit()
def PlayStation4Pro():
    cur.execute("Select qty from cart where productname= 'SONY PlayStation 4 Pro';")
    for a in cur:
        for c in range(len(a)):
            cur.execute("update cart set qty=qty+1 where productname='SONY PlayStation 4 Pro';")
            db.commit()
def PlayStation3():
    cur.execute("Select qty from cart where productname= 'sony playstation 3';")
    for a in cur:
        for c in range(len(a)):
            cur.execute("update cart set qty=qty+1 where productname='sony playstation 3';")
            db.commit()
def Xbox():
    root=tk.Tk()
    root.title("Xbox")
    root.geometry("740x450")
    root.resizable(width=False,height=False)
    cur.execute("select * from xbox")
    main_frame=tk.Frame(root,bg="#cdfaf5",pady=0) #background of button
    main_frame.pack(fill=tk.BOTH,expand=True)
    
    i=1
    c=tk.Label(
        main_frame,
        width=20,
        text="S. No.",
        borderwidth=3,
        relief="ridge",
        anchor="w",
        bg="yellow",
        font=("Ariel",15)).grid(row=0,column=0)
    c=tk.Label(
        main_frame,
        width=20,
        text="Xbox",
        borderwidth=3,
        relief="ridge",
        anchor="w",
        bg="yellow",
        font=("Ariel",15)).grid(row=0,column=1)
    c=tk.Label(
        main_frame,
        width=20,
        text="Price in Rs.",
        borderwidth=3,
        relief="ridge",
        anchor="w",
        bg="yellow",
        font=("Ariel",15)).grid(row=0,column=2)
    for a in cur:
        for b in range(len(a)):
            c=tk.Entry(main_frame,width=20,fg="blue",bg="white",borderwidth=3,font=("Ariel",15))
            c.grid(row=i,column=b)
            c.insert(tk.END,a[b])
        i=i+1
    tk.Button(
        main_frame,
        background="#002366",       #color of back of button
        foreground="#cdfaf5",       #color of text
        activebackground="grey",  #color of back of button activated
        activeforeground="black", #color of text activated
        highlightthickness=2,
        width=5,
        border=1,
        cursor="hand1",
        text="Add",
        font=("Arial",11,'bold'),
        command=lambda: [XboxSeriesS()]
        ).grid(row=1,column=3)
    tk.Button(
        main_frame,
        background="#002366",       #color of back of button
        foreground="#cdfaf5",       #color of text
        activebackground="grey",  #color of back of button activated
        activeforeground="black", #color of text activated
        highlightthickness=2,
        width=5,
        border=1,
        cursor="hand1",
        text="Add",
        font=("Arial",11,'bold'),
        command=lambda: [XboxSeriesT()]
        ).grid(row=2,column=3)
    tk.Button(
        main_frame,
        background="#002366",       #color of back of button
        foreground="#cdfaf5",       #color of text
        activebackground="grey",  #color of back of button activated
        activeforeground="black", #color of text activated
        highlightthickness=2,
        width=5,
        border=1,
        cursor="hand1",
        text="Add",
        font=("Arial",11,'bold'),
        command=lambda: [XboxOneS()]
        ).grid(row=3,column=3)
    tk.Button(
        main_frame,
        background="#002366",       #color of back of button
        foreground="#cdfaf5",       #color of text
        activebackground="grey",  #color of back of button activated
        activeforeground="black", #color of text activated
        highlightthickness=2,
        width=5,
        border=1,
        cursor="hand1",
        text="Add",
        font=("Arial",11,'bold'),
        command=lambda: [XboxOneX()]
        ).grid(row=4,column=3)
    tk.Button(
        main_frame,
        background="#002366",       #color of back of button
        foreground="#cdfaf5",       #color of text
        activebackground="grey",  #color of back of button activated
        activeforeground="black", #color of text activated
        highlightthickness=2,
        width=5,
        border=1,
        cursor="hand1",
        text="Add",
        font=("Arial",11,'bold'),
        command=lambda: [Xbox360()]
        ).grid(row=5,column=3)
        
    tk.Button(
        main_frame,
        background="#002366",       #color of back of button
        foreground="#cdfaf5",       #color of text
        activebackground="grey",  #color of back of button activated
        activeforeground="black", #color of text activated
        highlightthickness=2,
        width=13,
        border=6,
        cursor="hand1",
        text="To Start",
        font=("Arial",20,'bold'),
        command=lambda: [root.destroy(),start()]
        ).place(relx=0.19, rely=0.55)
    
    tk.Button(
        main_frame,
        background="#002366",       #color of back of button
        foreground="#cdfaf5",       #color of text
        activebackground="grey",  #color of back of button activated
        activeforeground="black", #color of text activated
        highlightthickness=2,
        width=13,
        border=6,
        cursor="hand1",
        text="Close",
        font=("Arial",20,'bold'),
        command=lambda: [root.destroy(),close()]
        ).place(relx=0.53, rely=0.55)
    
    tk.Button(
        main_frame,
        background="#002366",       #color of back of button
        foreground="#cdfaf5",       #color of text
        activebackground="grey",  #color of back of button activated
        activeforeground="black", #color of text activated
        highlightthickness=2,
        width=13,
        border=6,
        cursor="hand1",
        text="Cart",
        font=("Arial",20,'bold'),
        command=lambda: [root.destroy(),Cart()]
        ).place(relx=0.19, rely=0.75)
    
    tk.Button(
        main_frame,
        background="#002366",       #color of back of button
        foreground="#cdfaf5",       #color of text
        activebackground="grey",  #color of back of button activated
        activeforeground="black", #color of text activated
        highlightthickness=2,
        width=13,
        border=6,
        cursor="hand1",
        text="Go Back",
        font=("Arial",20,'bold'),
        command=lambda: [root.destroy(),Console()]
        ).place(relx=0.53, rely=0.75)
    root.mainloop()
def XboxSeriesS():
    cur.execute("Select qty from cart where productname= 'xbox series s';")
    for a in cur:
        for c in range(len(a)):
            cur.execute("update cart set qty=qty+1 where productname='xbox series s';")
            db.commit()
def XboxSeriesT():
    cur.execute("Select qty from cart where productname= 'xbox series t';")
    for a in cur:
        for c in range(len(a)):
            cur.execute("update cart set qty=qty+1 where productname='xbox series t';")
            db.commit()
def XboxOneS():
    cur.execute("Select qty from cart where productname= 'xbox one s';")
    for a in cur:
        for c in range(len(a)):
            cur.execute("update cart set qty=qty+1 where productname='xbox one s';")
            db.commit()
def XboxOneX():
    cur.execute("Select qty from cart where productname= 'xbox one x';")
    for a in cur:
        for c in range(len(a)):
            cur.execute("update cart set qty=qty+1 where productname='xbox one x';")
            db.commit()
def Xbox360():
    cur.execute("Select qty from cart where productname= 'xbox 360';")
    for a in cur:
        for c in range(len(a)):
            cur.execute("update cart set qty=qty+1 where productname='xbox 360';")
            db.commit()
def Nintendo():
    root=tk.Tk()
    root.title("Nintendo")
    root.geometry("740x450")
    root.resizable(width=False,height=False)
    cur.execute("select * from nintendo")
    main_frame=tk.Frame(root,bg="#cdfaf5",pady=0) #background of button
    main_frame.pack(fill=tk.BOTH,expand=True)
    
    i=1
    c=tk.Label(
        main_frame,
        width=20,
        text="S. No.",
        borderwidth=3,
        relief="ridge",
        anchor="w",
        bg="yellow",
        font=("Ariel",15)).grid(row=0,column=0)
    c=tk.Label(
        main_frame,
        width=20,
        text="Nintendo",
        borderwidth=3,
        relief="ridge",
        anchor="w",
        bg="yellow",
        font=("Ariel",15)).grid(row=0,column=1)
    c=tk.Label(
        main_frame,
        width=20,
        text="Price in Rs.",
        borderwidth=3,
        relief="ridge",
        anchor="w",
        bg="yellow",
        font=("Ariel",15)).grid(row=0,column=2)
    for a in cur:
        for b in range(len(a)):
            c=tk.Entry(main_frame,width=20,fg="blue",bg="white",borderwidth=3,font=("Ariel",15))
            c.grid(row=i,column=b)
            c.insert(tk.END,a[b])
        i=i+1
    tk.Button(
        main_frame,
        background="#002366",       #color of back of button
        foreground="#cdfaf5",       #color of text
        activebackground="grey",  #color of back of button activated
        activeforeground="black", #color of text activated
        highlightthickness=2,
        width=5,
        border=1,
        cursor="hand1",
        text="Add",
        font=("Arial",11,'bold'),
        command=lambda: [NintendoSwitchOLED()]
        ).grid(row=1,column=3)
    tk.Button(
        main_frame,
        background="#002366",       #color of back of button
        foreground="#cdfaf5",       #color of text
        activebackground="grey",  #color of back of button activated
        activeforeground="black", #color of text activated
        highlightthickness=2,
        width=5,
        border=1,
        cursor="hand1",
        text="Add",
        font=("Arial",11,'bold'),
        command=lambda: [Nintendo3DS()]
        ).grid(row=2,column=3)
    tk.Button(
        main_frame,
        background="#002366",       #color of back of button
        foreground="#cdfaf5",       #color of text
        activebackground="grey",  #color of back of button activated
        activeforeground="black", #color of text activated
        highlightthickness=2,
        width=5,
        border=1,
        cursor="hand1",
        text="Add",
        font=("Arial",11,'bold'),
        command=lambda: [NintendoWii()]
        ).grid(row=3,column=3)
    tk.Button(
        main_frame,
        background="#002366",       #color of back of button
        foreground="#cdfaf5",       #color of text
        activebackground="grey",  #color of back of button activated
        activeforeground="black", #color of text activated
        highlightthickness=2,
        width=5,
        border=1,
        cursor="hand1",
        text="Add",
        font=("Arial",11,'bold'),
        command=lambda: [NintendoWiiU()]
        ).grid(row=4,column=3)
    tk.Button(
        main_frame,
        background="#002366",       #color of back of button
        foreground="#cdfaf5",       #color of text
        activebackground="grey",  #color of back of button activated
        activeforeground="black", #color of text activated
        highlightthickness=2,
        width=5,
        border=1,
        cursor="hand1",
        text="Add",
        font=("Arial",11,'bold'),
        command=lambda: [NintendoDS()]
        ).grid(row=5,column=3)
        
    tk.Button(
        main_frame,
        background="#002366",       #color of back of button
        foreground="#cdfaf5",       #color of text
        activebackground="grey",  #color of back of button activated
        activeforeground="black", #color of text activated
        highlightthickness=2,
        width=13,
        border=6,
        cursor="hand1",
        text="To Start",
        font=("Arial",20,'bold'),
        command=lambda: [root.destroy(),start()]
        ).place(relx=0.19, rely=0.55)
    
    tk.Button(
        main_frame,
        background="#002366",       #color of back of button
        foreground="#cdfaf5",       #color of text
        activebackground="grey",  #color of back of button activated
        activeforeground="black", #color of text activated
        highlightthickness=2,
        width=13,
        border=6,
        cursor="hand1",
        text="Close",
        font=("Arial",20,'bold'),
        command=lambda: [root.destroy(),close()]
        ).place(relx=0.53, rely=0.55)
    
    tk.Button(
        main_frame,
        background="#002366",       #color of back of button
        foreground="#cdfaf5",       #color of text
        activebackground="grey",  #color of back of button activated
        activeforeground="black", #color of text activated
        highlightthickness=2,
        width=13,
        border=6,
        cursor="hand1",
        text="Cart",
        font=("Arial",20,'bold'),
        command=lambda: [root.destroy(),Cart()]
        ).place(relx=0.19, rely=0.75)
    
    tk.Button(
        main_frame,
        background="#002366",       #color of back of button
        foreground="#cdfaf5",       #color of text
        activebackground="grey",  #color of back of button activated
        activeforeground="black", #color of text activated
        highlightthickness=2,
        width=13,
        border=6,
        cursor="hand1",
        text="Go Back",
        font=("Arial",20,'bold'),
        command=lambda: [root.destroy(),Console()]
        ).place(relx=0.53, rely=0.75)
    root.mainloop()
def NintendoSwitchOLED():
    cur.execute("Select qty from cart where productname= 'Nintendo Switch OLED';")
    for a in cur:
        for c in range(len(a)):
            cur.execute("update cart set qty=qty+1 where productname='nintendo switch oled';")
            db.commit()
def Nintendo3DS():
    cur.execute("Select qty from cart where productname= 'Nintendo 3DS';")
    for a in cur:
        for c in range(len(a)):
            cur.execute("update cart set qty=qty+1 where productname='nintendo 3ds';")
            db.commit()
def NintendoWii():
    cur.execute("Select qty from cart where productname= 'Nintendo wii';")
    for a in cur:
        for c in range(len(a)):
            cur.execute("update cart set qty=qty+1 where productname='nintendo wii';")
            db.commit()
def NintendoWiiU():
    cur.execute("Select qty from cart where productname= 'Nintendo Wii U';")
    for a in cur:
        for c in range(len(a)):
            cur.execute("update cart set qty=qty+1 where productname='nintendo wii u';")
            db.commit()
def NintendoDS():
    cur.execute("Select qty from cart where productname= 'Nintendo DS';")
    for a in cur:
        for c in range(len(a)):
            cur.execute("update cart set qty=qty+1 where productname='nintendo ds';")
            db.commit()
#Television
def Television():
    root=tk.Tk()
    root.geometry("770x500")
    root.title("Television")
    root.resizable(width=False,height=False)

    main_frame=tk.Frame(root,bg="#cdfaf5",pady=40) #background of button
    main_frame.pack(fill=tk.BOTH,expand=True)
    tk.Label(
        main_frame,
        background="#cdfaf5",       #color of back of button
        foreground="black",       #color of text
        text="Which company would you like to select?",
        height=2,
        border=1,
        font=("Arial",25,"bold")).place(relx=0.5, rely=0, anchor=tk.N)
    button1=tk.Button(
        main_frame,
        background="#4169e1",     #color of back of button
        foreground="#cdfaf5",       #color of text
        activebackground="grey",  #color of back of button activated
        activeforeground="black", #color of text activated
        highlightthickness=2,
        width=12,
        height=2,
        border=10,
        cursor="hand1",
        text="Sony",
        font=("Arial",20,'bold'),   
        command=lambda:[root.destroy(),SonyTV()]
        ).place(relx=0.03, rely=0.25)

    button2=tk.Button(
        main_frame,
        background="#4169e1",     #color of back of button
        foreground="#cdfaf5",       #color of text
        activebackground="grey",  #color of back of button activated
        activeforeground="black", #color of text activated
        highlightthickness=2,
        width=12,
        height=2,
        border=10,
        cursor="hand1",
        text="Samsung",
        font=("Arial",20,'bold'),
        command=lambda:[root.destroy(),SamsungTV()]
        ).place(relx=0.35, rely=0.25)       
    
    button3=tk.Button(
        main_frame,
        background="#4169e1",     #color of back of button
        foreground="#cdfaf5",       #color of text
        activebackground="grey",  #color of back of button activated
        activeforeground="black", #color of text activated
        highlightthickness=2,
        width=12,
        height=2,
        border=10,
        cursor="hand1",
        text="LG",
        font=("Arial",20,'bold'),
        command=lambda:[root.destroy(),LGTV()]
        ).place(relx=0.67, rely=0.25)

    button4=tk.Button(
        main_frame,
        background="#002366",       #color of back of button
        foreground="#cdfaf5",       #color of text
        activebackground="grey",  #color of back of button activated
        activeforeground="black", #color of text activated
        highlightthickness=2,
        width=12,
        height=2,
        border=10,
        cursor="hand1",
        text="To Start",
        font=("Arial",20,'bold'),
        command=lambda: [root.destroy(),start()]
        ).place(relx=0.35, rely=0.55)
    
    button5=tk.Button(
        main_frame,
        background="#002366",       #color of back of button
        foreground="#cdfaf5",       #color of text
        activebackground="grey",  #color of back of button activated
        activeforeground="black", #color of text activated
        highlightthickness=2,
        width=12,
        height=2,
        border=10,
        cursor="hand1",
        text="Close",
        font=("Arial",20,'bold'),
        command=lambda: [root.destroy(),close()]
        ).place(relx=0.67, rely=0.55)
    button6=tk.Button(
        main_frame,
        background="#002366",       #color of back of button
        foreground="#cdfaf5",       #color of text
        activebackground="grey",  #color of back of button activated
        activeforeground="black", #color of text activated
        highlightthickness=2,
        width=12,
        height=2,
        border=10,
        cursor="hand1",
        text="Cart",
        font=("Arial",20,'bold'),
        command=lambda: [root.destroy(),Cart()]
        ).place(relx=0.03, rely=0.55)
    root.mainloop()
    
def SonyTV():
    root=tk.Tk()
    root.title("SonyTV")
    root.geometry("740x450")
    root.resizable(width=False,height=False)
    cur.execute("select * from sonytv")
    main_frame=tk.Frame(root,bg="#cdfaf5",pady=0) #background of button
    main_frame.pack(fill=tk.BOTH,expand=True)
    
    i=1
    c=tk.Label(
        main_frame,
        width=20,
        text="S. No.",
        borderwidth=3,
        relief="ridge",
        anchor="w",
        bg="yellow",
        font=("Ariel",15)).grid(row=0,column=0)
    c=tk.Label(
        main_frame,
        width=20,
        text="SonyTV",
        borderwidth=3,
        relief="ridge",
        anchor="w",
        bg="yellow",
        font=("Ariel",15)).grid(row=0,column=1)
    c=tk.Label(
        main_frame,
        width=20,
        text="Price in Rs.",
        borderwidth=3,
        relief="ridge",
        anchor="w",
        bg="yellow",
        font=("Ariel",15)).grid(row=0,column=2)
    for a in cur:
        for b in range(len(a)):
            c=tk.Entry(main_frame,width=20,fg="blue",bg="white",borderwidth=3,font=("Ariel",15))
            c.grid(row=i,column=b)
            c.insert(tk.END,a[b])
        i=i+1
    tk.Button(
        main_frame,
        background="#002366",       #color of back of button
        foreground="#cdfaf5",       #color of text
        activebackground="grey",  #color of back of button activated
        activeforeground="black", #color of text activated
        highlightthickness=2,
        width=5,
        border=2,
        cursor="hand1",
        text="Add",
        font=("Arial",10,'bold'),
        command=lambda: [Bravia7()]
        ).grid(row=1,column=3)
    tk.Button(
        main_frame,
        background="#002366",       #color of back of button
        foreground="#cdfaf5",       #color of text
        activebackground="grey",  #color of back of button activated
        activeforeground="black", #color of text activated
        highlightthickness=2,
        width=5,
        border=2,
        cursor="hand1",
        text="Add",
        font=("Arial",10,'bold'),
        command=lambda: [Bravia9()]
        ).grid(row=2,column=3)
    tk.Button(
        main_frame,
        background="#002366",       #color of back of button
        foreground="#cdfaf5",       #color of text
        activebackground="grey",  #color of back of button activated
        activeforeground="black", #color of text activated
        highlightthickness=2,
        width=5,
        border=2,
        cursor="hand1",
        text="Add",
        font=("Arial",10,'bold'),
        command=lambda: [Bravia8()]
        ).grid(row=3,column=3)
    tk.Button(
        main_frame,
        background="#002366",       #color of back of button
        foreground="#cdfaf5",       #color of text
        activebackground="grey",  #color of back of button activated
        activeforeground="black", #color of text activated
        highlightthickness=2,
        width=5,
        border=2,
        cursor="hand1",
        text="Add",
        font=("Arial",10,'bold'),
        command=lambda: [Bravia3()]
        ).grid(row=4,column=3)
    tk.Button(
        main_frame,
        background="#002366",       #color of back of button
        foreground="#cdfaf5",       #color of text
        activebackground="grey",  #color of back of button activated
        activeforeground="black", #color of text activated
        highlightthickness=2,
        width=5,
        border=2,
        cursor="hand1",
        text="Add",
        font=("Arial",10,'bold'),
        command=lambda: [Bravia2()]
        ).grid(row=5,column=3)
        
    tk.Button(
        main_frame,
        background="#002366",       #color of back of button
        foreground="#cdfaf5",       #color of text
        activebackground="grey",  #color of back of button activated
        activeforeground="black", #color of text activated
        highlightthickness=2,
        width=13,
        border=6,
        cursor="hand1",
        text="To Start",
        font=("Arial",20,'bold'),
        command=lambda: [root.destroy(),start()]
        ).place(relx=0.19, rely=0.55)
    
    tk.Button(
        main_frame,
        background="#002366",       #color of back of button
        foreground="#cdfaf5",       #color of text
        activebackground="grey",  #color of back of button activated
        activeforeground="black", #color of text activated
        highlightthickness=2,
        width=13,
        border=6,
        cursor="hand1",
        text="Close",
        font=("Arial",20,'bold'),
        command=lambda: [root.destroy(),close()]
        ).place(relx=0.53, rely=0.55)
    
    tk.Button(
        main_frame,
        background="#002366",       #color of back of button
        foreground="#cdfaf5",       #color of text
        activebackground="grey",  #color of back of button activated
        activeforeground="black", #color of text activated
        highlightthickness=2,
        width=13,
        border=6,
        cursor="hand1",
        text="Cart",
        font=("Arial",20,'bold'),
        command=lambda: [root.destroy(),Cart()]
        ).place(relx=0.19, rely=0.75)
    
    tk.Button(
        main_frame,
        background="#002366",       #color of back of button
        foreground="#cdfaf5",       #color of text
        activebackground="grey",  #color of back of button activated
        activeforeground="black", #color of text activated
        highlightthickness=2,
        width=13,
        border=6,
        cursor="hand1",
        text="Go Back",
        font=("Arial",20,'bold'),
        command=lambda: [root.destroy(),Television()]
        ).place(relx=0.53, rely=0.75)
    root.mainloop()
def Bravia7():
    cur.execute("Select qty from cart where productname= 'SONY Bravia 7';")
    for a in cur:
        for c in range(len(a)):
            cur.execute("update cart set qty=qty+1 where productname='SONY Bravia 7';")
            db.commit()
def Bravia9():
    cur.execute("Select qty from cart where productname= 'SONY Bravia 9';")
    for a in cur:
        for c in range(len(a)):
            cur.execute("update cart set qty=qty+1 where productname='SONY Bravia 9';")
            db.commit()
def Bravia8():
    cur.execute("Select qty from cart where productname= 'SONY Bravia 8';")
    for a in cur:
        for c in range(len(a)):
            cur.execute("update cart set qty=qty+1 where productname='SONY Bravia 8';")
            db.commit()
def Bravia3():
    cur.execute("Select qty from cart where productname= 'SONY Bravia 3';")
    for a in cur:
        for c in range(len(a)):
            cur.execute("update cart set qty=qty+1 where productname='SONY Bravia 3';")
            db.commit()
def Bravia2():
    cur.execute("Select qty from cart where productname= 'SONY Bravia 2';")
    for a in cur:
        for c in range(len(a)):
            cur.execute("update cart set qty=qty+1 where productname='SONY Bravia 2';")
            db.commit()
            
def SamsungTV():
    root=tk.Tk()
    root.title("SamsungTV")
    root.geometry("740x450")
    root.resizable(width=False,height=False)
    cur.execute("select * from samsungtv")
    main_frame=tk.Frame(root,bg="#cdfaf5",pady=0) #background of button
    main_frame.pack(fill=tk.BOTH,expand=True)
    
    i=1
    c=tk.Label(
        main_frame,
        width=25,
        text="S. No.",
        borderwidth=3,
        relief="ridge",
        anchor="w",
        bg="yellow",
        font=("Ariel",10)).grid(row=0,column=0)
    c=tk.Label(
        main_frame,
        width=25,
        text="SamsungTV",
        borderwidth=3,
        relief="ridge",
        anchor="w",
        bg="yellow",
        font=("Ariel",10)).grid(row=0,column=1)
    c=tk.Label(
        main_frame,
        width=25,
        text="Price in Rs.",
        borderwidth=3,
        relief="ridge",
        anchor="w",
        bg="yellow",
        font=("Ariel",10)).grid(row=0,column=2)
    for a in cur:
        for b in range(len(a)):
            c=tk.Entry(main_frame,width=25,fg="blue",bg="white",borderwidth=3,font=("Ariel",11))
            c.grid(row=i,column=b)
            c.insert(tk.END,a[b])
        i=i+1
    tk.Button(
        main_frame,
        background="#002366",       #color of back of button
        foreground="#cdfaf5",       #color of text
        activebackground="grey",  #color of back of button activated
        activeforeground="black", #color of text activated
        highlightthickness=2,
        width=5,
        border=1,
        cursor="hand1",
        text="Add",
        font=("Arial",9,'bold'),
        command=lambda: [Q70Series4KQLED()]
        ).grid(row=1,column=3)
    tk.Button(
        main_frame,
        background="#002366",       #color of back of button
        foreground="#cdfaf5",       #color of text
        activebackground="grey",  #color of back of button activated
        activeforeground="black", #color of text activated
        highlightthickness=2,
        width=5,
        border=1,
        cursor="hand1",
        text="Add",
        font=("Arial",9,'bold'),
        command=lambda: [DSeriesBrighterCrystal4K()]
        ).grid(row=2,column=3)
    tk.Button(
        main_frame,
        background="#002366",       #color of back of button
        foreground="#cdfaf5",       #color of text
        activebackground="grey",  #color of back of button activated
        activeforeground="black", #color of text activated
        highlightthickness=2,
        width=5,
        border=1,
        cursor="hand1",
        text="Add",
        font=("Arial",9,'bold'),
        command=lambda: [QLED4K()]
        ).grid(row=3,column=3)
    tk.Button(
        main_frame,
        background="#002366",       #color of back of button
        foreground="#cdfaf5",       #color of text
        activebackground="grey",  #color of back of button activated
        activeforeground="black", #color of text activated
        highlightthickness=2,
        width=5,
        border=1,
        cursor="hand1",
        text="Add",
        font=("Arial",9,'bold'),
        command=lambda: [LED4KHD()]
        ).grid(row=4,column=3)
    tk.Button(
        main_frame,
        background="#002366",       #color of back of button
        foreground="#cdfaf5",       #color of text
        activebackground="grey",  #color of back of button activated
        activeforeground="black", #color of text activated
        highlightthickness=2,
        width=5,
        border=1,
        cursor="hand1",
        text="Add",
        font=("Arial",9,'bold'),
        command=lambda: [LED4KHDUltra()]
        ).grid(row=5,column=3)
        
    tk.Button(
        main_frame,
        background="#002366",       #color of back of button
        foreground="#cdfaf5",       #color of text
        activebackground="grey",  #color of back of button activated
        activeforeground="black", #color of text activated
        highlightthickness=2,
        width=13,
        border=6,
        cursor="hand1",
        text="To Start",
        font=("Arial",20,'bold'),
        command=lambda: [root.destroy(),start()]
        ).place(relx=0.19, rely=0.55)
    
    tk.Button(
        main_frame,
        background="#002366",       #color of back of button
        foreground="#cdfaf5",       #color of text
        activebackground="grey",  #color of back of button activated
        activeforeground="black", #color of text activated
        highlightthickness=2,
        width=13,
        border=6,
        cursor="hand1",
        text="Close",
        font=("Arial",20,'bold'),
        command=lambda: [root.destroy(),close()]
        ).place(relx=0.53, rely=0.55)
    
    tk.Button(
        main_frame,
        background="#002366",       #color of back of button
        foreground="#cdfaf5",       #color of text
        activebackground="grey",  #color of back of button activated
        activeforeground="black", #color of text activated
        highlightthickness=2,
        width=13,
        border=6,
        cursor="hand1",
        text="Cart",
        font=("Arial",20,'bold'),
        command=lambda: [root.destroy(),Cart()]
        ).place(relx=0.19, rely=0.75)
    
    tk.Button(
        main_frame,
        background="#002366",       #color of back of button
        foreground="#cdfaf5",       #color of text
        activebackground="grey",  #color of back of button activated
        activeforeground="black", #color of text activated
        highlightthickness=2,
        width=13,
        border=6,
        cursor="hand1",
        text="Go Back",
        font=("Arial",20,'bold'),
        command=lambda: [root.destroy(),Television()]
        ).place(relx=0.53, rely=0.75)
    root.mainloop()

def Q70Series4KQLED():
    cur.execute("Select qty from cart where productname= 'Samsung Q70 Series 4K QLED';")
    for a in cur:
        for c in range(len(a)):
            cur.execute("update cart set qty=qty+1 where productname='Samsung Q70 Series 4K QLED';")
            db.commit()
def DSeriesBrighterCrystal4K():
    cur.execute("Select qty from cart where productname= 'Samsung D Series Brighter Crystal 4K';")
    for a in cur:
        for c in range(len(a)):
            cur.execute("update cart set qty=qty+1 where productname='Samsung D Series Brighter Crystal 4K';")
            db.commit()
def QLED4K():
    cur.execute("Select qty from cart where productname= 'Samsung 4K QLED';")
    for a in cur:
        for c in range(len(a)):
            cur.execute("update cart set qty=qty+1 where productname='Samsung 4K QLED';")
            db.commit()
def LED4KHD():
    cur.execute("Select qty from cart where productname= 'Samsung 4K HD LED';")
    for a in cur:
        for c in range(len(a)):
            cur.execute("update cart set qty=qty+1 where productname='Samsung 4K HD LED';")
            db.commit()
def LED4KHDUltra():
    cur.execute("Select qty from cart where productname= 'Samsung 4K Ultra HD LED';")
    for a in cur:
        for c in range(len(a)):
            cur.execute("update cart set qty=qty+1 where productname='Samsung 4K Ultra HD LED';")
            db.commit()

def LGTV():
    root=tk.Tk()
    root.title("LGTV")
    root.geometry("740x450")
    root.resizable(width=False,height=False)
    cur.execute("select * from lgtv")
    main_frame=tk.Frame(root,bg="#cdfaf5",pady=0) #background of button
    main_frame.pack(fill=tk.BOTH,expand=True)
    
    i=1
    c=tk.Label(
        main_frame,
        width=25,
        text="S. No.",
        borderwidth=3,
        relief="ridge",
        anchor="w",
        bg="yellow",
        font=("Ariel",10)).grid(row=0,column=0)
    c=tk.Label(
        main_frame,
        width=25,
        text="LGTV",
        borderwidth=3,
        relief="ridge",
        anchor="w",
        bg="yellow",
        font=("Ariel",10)).grid(row=0,column=1)
    c=tk.Label(
        main_frame,
        width=25,
        text="Price in Rs.",
        borderwidth=3,
        relief="ridge",
        anchor="w",
        bg="yellow",
        font=("Ariel",10)).grid(row=0,column=2)
    for a in cur:
        for b in range(len(a)):
            c=tk.Entry(main_frame,width=25,fg="blue",bg="white",borderwidth=3,font=("Ariel",11))
            c.grid(row=i,column=b)
            c.insert(tk.END,a[b])
        i=i+1
    tk.Button(
        main_frame,
        background="#002366",       #color of back of button
        foreground="#cdfaf5",       #color of text
        activebackground="grey",  #color of back of button activated
        activeforeground="black", #color of text activated
        highlightthickness=2,
        width=5,
        border=1,
        cursor="hand1",
        text="Add",
        font=("Arial",9,'bold'),
        command=lambda: [OLEDevoAIC465()]
        ).grid(row=1,column=3)
    tk.Button(
        main_frame,
        background="#002366",       #color of back of button
        foreground="#cdfaf5",       #color of text
        activebackground="grey",  #color of back of button activated
        activeforeground="black", #color of text activated
        highlightthickness=2,
        width=5,
        border=1,
        cursor="hand1",
        text="Add",
        font=("Arial",9,'bold'),
        command=lambda: [UHDTVUR7565()]
        ).grid(row=2,column=3)
    tk.Button(
        main_frame,
        background="#002366",       #color of back of button
        foreground="#cdfaf5",       #color of text
        activebackground="grey",  #color of back of button activated
        activeforeground="black", #color of text activated
        highlightthickness=2,
        width=5,
        border=1,
        cursor="hand1",
        text="Add",
        font=("Arial",9,'bold'),
        command=lambda: [QNEDTVQNED7565()]
        ).grid(row=3,column=3)
    tk.Button(
        main_frame,
        background="#002366",       #color of back of button
        foreground="#cdfaf5",       #color of text
        activebackground="grey",  #color of back of button activated
        activeforeground="black", #color of text activated
        highlightthickness=2,
        width=5,
        border=1,
        cursor="hand1",
        text="Add",
        font=("Arial",9,'bold'),
        command=lambda: [QNEDAI65QNED88()]
        ).grid(row=4,column=3)
    tk.Button(
        main_frame,
        background="#002366",       #color of back of button
        foreground="#cdfaf5",       #color of text
        activebackground="grey",  #color of back of button activated
        activeforeground="black", #color of text activated
        highlightthickness=2,
        width=5,
        border=1,
        cursor="hand1",
        text="Add",
        font=("Arial",9,'bold'),
        command=lambda: [LQ64332AI()]
        ).grid(row=5,column=3)
        
    tk.Button(
        main_frame,
        background="#002366",       #color of back of button
        foreground="#cdfaf5",       #color of text
        activebackground="grey",  #color of back of button activated
        activeforeground="black", #color of text activated
        highlightthickness=2,
        width=13,
        border=6,
        cursor="hand1",
        text="To Start",
        font=("Arial",20,'bold'),
        command=lambda: [root.destroy(),start()]
        ).place(relx=0.19, rely=0.55)
    
    tk.Button(
        main_frame,
        background="#002366",       #color of back of button
        foreground="#cdfaf5",       #color of text
        activebackground="grey",  #color of back of button activated
        activeforeground="black", #color of text activated
        highlightthickness=2,
        width=13,
        border=6,
        cursor="hand1",
        text="Close",
        font=("Arial",20,'bold'),
        command=lambda: [root.destroy(),close()]
        ).place(relx=0.53, rely=0.55)
    
    tk.Button(
        main_frame,
        background="#002366",       #color of back of button
        foreground="#cdfaf5",       #color of text
        activebackground="grey",  #color of back of button activated
        activeforeground="black", #color of text activated
        highlightthickness=2,
        width=13,
        border=6,
        cursor="hand1",
        text="Cart",
        font=("Arial",20,'bold'),
        command=lambda: [root.destroy(),Cart()]
        ).place(relx=0.19, rely=0.75)
    
    tk.Button(
        main_frame,
        background="#002366",       #color of back of button
        foreground="#cdfaf5",       #color of text
        activebackground="grey",  #color of back of button activated
        activeforeground="black", #color of text activated
        highlightthickness=2,
        width=13,
        border=6,
        cursor="hand1",
        text="Go Back",
        font=("Arial",20,'bold'),
        command=lambda: [root.destroy(),Television()]
        ).place(relx=0.53, rely=0.75)
    root.mainloop() 
def OLEDevoAIC465():
    cur.execute("Select qty from cart where productname= 'LG OLED evo AI C4 65';")
    for a in cur:
        for c in range(len(a)):
            cur.execute("update cart set qty=qty+1 where productname='LG OLED evo AI C4 65';")
            db.commit()
def UHDTVUR7565():
    cur.execute("Select qty from cart where productname= 'LG UHD TV UR75 65';")
    for a in cur:
        for c in range(len(a)):
            cur.execute("update cart set qty=qty+1 where productname='LG UHD TV UR75 65';")
            db.commit()
def QNEDTVQNED7565():
    cur.execute("Select qty from cart where productname= 'LG QNED TV QNED75 65';")
    for a in cur:
        for c in range(len(a)):
            cur.execute("update cart set qty=qty+1 where productname='LG QNED TV QNED75 65';")
            db.commit()
def QNEDAI65QNED88():
    cur.execute("Select qty from cart where productname= 'LG 65 QNED AI QNED88T';")
    for a in cur:
        for c in range(len(a)):
            cur.execute("update cart set qty=qty+1 where productname='LG 65 QNED AI QNED88T';")
            db.commit()
def LQ64332AI():
    cur.execute("Select qty from cart where productname= 'LG LQ643 32 AI';")
    for a in cur:
        for c in range(len(a)):
            cur.execute("update cart set qty=qty+1 where productname='LG LQ643 32 AI';")
            db.commit()
def Cart():
    root=tk.Tk()
    root.title("Cart")
    root.state("zoomed")
    root.resizable(width=False,height=False)
    cur.execute("select * from cart where qty>=1;")
    main_frame=tk.Frame(root,bg="#cdfaf5",pady=0) #background of button
    main_frame.pack(fill=tk.BOTH,expand=True)
    tk.Label(
        main_frame,
        width=45,
        text="Product Name",
        borderwidth=3,
        relief="ridge",
        anchor="w",
        bg="yellow",
        font=("Ariel",13)).grid(row=0,column=0)
    tk.Label(
        main_frame,
        width=45,
        text="Price in Rs.",
        borderwidth=3,
        relief="ridge",
        anchor="w",
        bg="yellow",
        font=("Ariel",13)).grid(row=0,column=1)
    tk.Label(
        main_frame,
        width=45,
        text="Quantity",
        borderwidth=3,
        relief="ridge",
        anchor="w",
        bg="yellow",
        font=("Ariel",13)).grid(row=0,column=2)
    i=1
    for a in cur:
        for b in range(len(a)):
            c=tk.Entry(main_frame,width=45,fg="blue",bg="white",borderwidth=3,font=("Ariel",13))
            c.grid(row=i,column=b)
            c.insert(tk.END,a[b])
        i=i+1
    tk.Button(
        main_frame,
        background="#002366",       #color of back of button
        foreground="#cdfaf5",       #color of text
        activebackground="grey",  #color of back of button activated
        activeforeground="black", #color of text activated
        highlightthickness=2,
        width=13,
        border=6,
        cursor="hand1",
        text="To Start",
        font=("Arial",18,'bold'),
        command=lambda: [root.destroy(),start()]
        ).place(relx=0.83, rely=0.25)
    
    tk.Button(
        main_frame,
        background="#002366",       #color of back of button
        foreground="#cdfaf5",       #color of text
        activebackground="grey",  #color of back of button activated
        activeforeground="black", #color of text activated
        highlightthickness=2,
        width=13,
        border=6,
        cursor="hand1",
        text="Close",
        font=("Arial",18,'bold'),
        command=lambda: [root.destroy(),close()]
        ).place(relx=0.83, rely=0.45)
    
    tk.Button(
        main_frame,
        background="#002366",       #color of back of button
        foreground="#cdfaf5",       #color of text
        activebackground="grey",  #color of back of button activated
        activeforeground="black", #color of text activated
        highlightthickness=2,
        width=13,
        border=6,
        cursor="hand1",
        text="Buy Items",
        font=("Arial",18,'bold'),
        command=lambda: [root.destroy(),Buy()]
        ).place(relx=0.83, rely=0.65)
    root.mainloop()
def Buy():
    root=tk.Tk()
    root.title("Buy")
    root.geometry("740x450")
    root.resizable(width=False,height=False)
    cur.execute("Select sum(Qty*Price) from cart;")
    main_frame=tk.Frame(root,bg="#cdfaf5",pady=0) #background of button
    main_frame.pack(fill=tk.BOTH,expand=True)
    tk.Label(
        main_frame,
        background="#cdfaf5",       #color of back of button
        foreground="black",       #color of text
        text="Thank you for purchasing from our store",
        height=2,
        border=1,
        font=("Arial",25,"bold")).grid(row=0,column=0)
    tk.Label(
        main_frame,
        width=20,
        text="Total Price in Rs.",
        borderwidth=3,
        relief="ridge",
        anchor="w",
        bg="yellow",
        font=("Ariel",15)).grid(row=1,column=0)
    i=2
    for a in cur:
        for b in range(len(a)):
            c=tk.Entry(main_frame,width=20,fg="blue",bg="white",borderwidth=3,font=("Ariel",15))
            c.grid(row=i,column=b)
            c.insert(tk.END,a[b])
    tk.Button(
        main_frame,
        background="#002366",       #color of back of button
        foreground="#cdfaf5",       #color of text
        activebackground="grey",  #color of back of button activated
        activeforeground="black", #color of text activated
        highlightthickness=2,
        width=13,
        border=6,
        cursor="hand1",
        text="To Start",
        font=("Arial",18,'bold'),
        command=lambda: [root.destroy(),start()]
        ).place(relx=0.63, rely=0.25)
    
    tk.Button(
        main_frame,
        background="#002366",       #color of back of button
        foreground="#cdfaf5",       #color of text
        activebackground="grey",  #color of back of button activated
        activeforeground="black", #color of text activated
        highlightthickness=2,
        width=13,
        border=6,
        cursor="hand1",
        text="Close",
        font=("Arial",18,'bold'),
        command=lambda: [root.destroy(),close()]
        ).place(relx=0.63, rely=0.65)
    
    tk.Button(
        main_frame,
        background="#002366",       #color of back of button
        foreground="#cdfaf5",       #color of text
        activebackground="grey",  #color of back of button activated
        activeforeground="black", #color of text activated
        highlightthickness=2,
        width=13,
        border=6,
        cursor="hand1",
        text="Cart",
        font=("Arial",18,'bold'),
        command=lambda: [root.destroy(),Cart()]
        ).place(relx=0.63, rely=0.45)
    root.mainloop()
def close():
    cur.execute("update cart set qty=0 where qty>=1;")
    db.commit()
start()
