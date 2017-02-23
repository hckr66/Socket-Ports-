import socket
import time
from tkinter import *
 
class FTP(object):
    def __init__(self, janela):
 
        def ir ():
            ip = self.IP1.get() + '.' +self.IP2.get() + '.' +self.IP3.get() + '.' +self.IP4.get()
            porta = int(self.b.get())
         
            meusocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 
            if meusocket.connect_ex((ip, porta)):
                self.Texto['text'] = "PORTA FECHADA"
                self.Texto['fg'] = 'green'
                 
            else:
                self.Texto['text'] = "PORTA ABERTA"
                self.Texto['fg'] ='red'
        
        self.MainF = Frame(janela, height = 100)
        self.MainF.pack()

        self.FrameIp = Frame(self.MainF)
        self.FrameIp.grid(column = 2, row = 1)
        
        self.Lip = Label(self.MainF, text="IP")
        self.IP1 = Entry(self.FrameIp, width= 3, exportselection=3,textvariable=IntVar())
        self.IP2 = Entry(self.FrameIp, width= 3, exportselection=3,textvariable=IntVar())
        self.IP3 = Entry(self.FrameIp, width= 3, exportselection=3,textvariable=IntVar())
        self.IP4 = Entry(self.FrameIp, width= 3, exportselection=3,textvariable=IntVar())

        self.Lip.grid(column = 2, row = 0)
        self.IP1.grid(column = 0, row = 1)
        self.IP2.grid(column = 1, row = 1)
        self.IP3.grid(column = 2, row = 1)
        self.IP4.grid(column = 3, row = 1)
 
        self.Lporta = Label(self.MainF, text="Porta")
        self.b = Entry(self.MainF)
        self.Lporta.grid(column = 2, row = 3)
        self.b.grid(column = 2, row = 4)
 
        self.Go = Button(self.MainF, text="Go", command=ir)
        self.Go.grid(column = 2, row = 6)
        
        self.Texto = Label(self.MainF, text="")
        self.Texto.grid(column = 2, row = 10)
 
        #Automaticamente
       

janela = Tk()
FTP(janela)


janela.title("Test Of Doors")
janela.geometry("300x150")
janela.iconbitmap("download.ico")
janela.mainloop()