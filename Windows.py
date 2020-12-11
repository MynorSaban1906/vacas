from tkinter import *
from tkinter import ttk
from tkinter import messagebox      # message box
from LoadData import Data as Cargar
from tkinter import filedialog
from tkinter import Image

class StorageGui(Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        #self.pack(fill='both', expand=1)
       
        self.WinPrincipal()


    def WinPrincipal(self):
        label1=Label( text="¡ Welcome To TitusDB!")
        label1.config(font=("Verdana",50))
        label1.pack(anchor=CENTER)
        label2=Label( text="¡ Select your option : ")
        label2.config(font=("Verdana",28))
        label2.pack(anchor=CENTER)
        label3=Label( text="\n\n1.option 1\n2.option 2\n3.option 3\n4. ISAM \n5.option 5")
        label3.config(font=("Verdana",23))
        label3.pack(anchor=CENTER)

        label3=Label( text="\n\nInsert Number")
        label3.config(font=("Verdana",15))
        label3.pack()
        entry = Entry()
        entry.pack(anchor=CENTER)
        button = Button(text= 'Accept', padx= 15, pady=6, bg= 'grey',fg='white', command=self.viewDb)
        button.pack(anchor=CENTER)
        
       

    def say_hi(self):
        print("hi there, everyone!")

    def viewDb(self):
        self.master.withdraw()
        Win2 = Toplevel()
        Win2.geometry("1000x600")
        Win2.title(" [EDD] Fase-1" )
        Win2.configure(bg='#2C3E50') 
        label1=Label(Win2, text="\nLOADING DATA BASE\n")
        label1.place(x=200,y=250,width=200,height=200)
        label1.config(font=("Verdana",50))
        label1.pack(anchor=CENTER)
        label2=Label(Win2, text=" insert load CSV  ")
        label2.config(font=("Verdana",15))
        label2.pack()
        self.pathCSV = Entry(Win2)
        self.pathCSV.pack()
        self.master=Win2
        
        button = Button(Win2, text= 'Accept', padx= 15, pady=6, bg= 'grey',fg='white',command=self.Open_Archive)
        
        button.pack(anchor=CENTER)
       
    def window3(self):
        
        Win3 = Tk()
        Win3.geometry("1000x600")
        Win3.title(" [EDD] Fase-1" )
        Win3.configure(bg='#2C3E50') 
        label1=Label(Win3,text="\nSelect your Data Base\n\n\n")
        label1.config(font=("Verdana",15))
        label1.pack(anchor=CENTER)
        comboExample =  ttk.Combobox (Win3, 
                            values=[
                                    "January", 
                                    "February",
                                    "March",
                                    "April"])
       
        comboExample.pack()
        button = Button(Win3, text= 'Accept', padx= 15, pady=6, bg= 'grey',fg='white',command=self.Open_Archive)
        button.pack(anchor=CENTER)

      #  img =  PhotoImage(file="TytusLogo.gif") 
       # panel = Label(Win3, image = img).place(x=100,y=500) 
       
        self.master=Win3


    def loadtable(self,path):
        Cargar.CargarArchivo(path)
        self.master.withdraw()
        self.window3()

    def Open_Archive(self):
        archive=filedialog.askopenfilename(initialdir="/home/msaban",
        title="seleccione Archivo",filetypes=(("jpeg files","*jpg"),
        ("all files","*.*")))
        print( archive)
        messagebox.showinfo("Loading data","DATA SAVED IN ISAM")
        self.loadtable(archive)
        

class NavBar(Frame):
    
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack(fill='both', expand=1)
        self.create_butons()

    def create_butons(self):
        self.prueba = Button(self, text="DBs",fg="black", bg="white")
        

        self.prueba.place(x=40,y=40,width=50,height=30)

