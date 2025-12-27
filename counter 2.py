import tkinter as tk
class Input_checker:

    def counter(self,root):
        main_frame=tk.Frame(root,bg="#cdfaf5",pady=0) #background of tk
        main_frame.pack(fill=tk.BOTH,expand=True)
        num= tk.Label(main_frame,text=0,height=3,width=5,bg="light grey",font=("Arial",60,'bold'))
        num.place(relx=0.35,rely=0.03)
        bt_count = tk.Button(main_frame,text="Counter",bg="light grey",activebackground="grey",cursor="hand1",command=lambda: self.counteradd(num),font=("Arial",18,'bold')).place(relx=0.44,rely=0.67)
        bt_back = tk.Button(main_frame,text="Previous",bg="light grey",activebackground="grey",cursor="hand1",command=lambda: self.counterback(num),font=("Arial",18,'bold')).place(relx=0.14,rely=0.67)
        bt_back = tk.Button(main_frame,text="Reset",bg="light grey",activebackground="grey",cursor="hand1",command=lambda: self.counterreset(num),font=("Arial",18,'bold')).place(relx=0.74,rely=0.67)
        
    def __init__(self):   
        root=tk.Tk()
        root.title("Project")
        root.geometry("770x650")
        root.resizable(width=False,height=False)
        self.counter(root)
        root.mainloop()

    def counteradd(self,num):
        num['text'] += 1
    def counterback(self,num):
        if num['text'] > 0:
            num['text'] -= 1
    def counterreset(self,num):
        num['text'] = 0

if __name__ == "__main__":
    input_checker = Input_checker()


