import tkinter as tk 
from Windows import StorageGui, NavBar

class Main:
    root = tk.Tk()
    root.geometry("1000x600")
    root.title(" [EDD] Fase-1" )
    app = StorageGui(master=root)
    app.configure(bg='#2C3E50') 
    app.place(x=200,width=200,height=200)
    
    app.mainloop()
 



start = Main()