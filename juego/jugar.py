################################################## Imports ##################################################
import tkinter as tk

################################################### Clases ##################################################
class Panel(tk.Frame):
    def __init__(self,master):
        super().__init__(master)
        # Primera fila
        tk.Button(self,text="1",font=font,width=3,height=1).grid(row=0,column=0)
        tk.Label(self,text="",font=mayor_menor_font,width=2).grid(row=0,column=1)
        tk.Button(self,text="1",font=font,width=3,height=1).grid(row=0,column=2)
        tk.Label(self,text="",font=mayor_menor_font,width=2).grid(row=0,column=3)
        tk.Button(self,text="1",font=font,width=3,height=1).grid(row=0,column=4)
        tk.Label(self,text="",font=mayor_menor_font,width=2).grid(row=0,column=5)
        tk.Button(self,text="1",font=font,width=3,height=1).grid(row=0,column=6)
        tk.Label(self,text="",font=mayor_menor_font,width=2).grid(row=0,column=7)
        tk.Button(self,text="1",font=font,width=3,height=1).grid(row=0,column=8)

        # Separadores
        tk.Label(self,text="",font=mayor_menor_font).grid(row=1,column=0)
        tk.Label(self,text="",font=mayor_menor_font).grid(row=1,column=2)
        tk.Label(self,text="",font=mayor_menor_font).grid(row=1,column=4)
        tk.Label(self,text="",font=mayor_menor_font).grid(row=1,column=6)
        tk.Label(self,text="",font=mayor_menor_font).grid(row=1,column=8)

        # Segunda fila
        tk.Button(self,text="1",font=font,width=3,height=1).grid(row=2,column=0)
        tk.Label(self,text="",font=mayor_menor_font,width=2).grid(row=2,column=1)
        tk.Button(self,text="1",font=font,width=3,height=1).grid(row=2,column=2)
        tk.Label(self,text="",font=mayor_menor_font,width=2).grid(row=2,column=3)
        tk.Button(self,text="1",font=font,width=3,height=1).grid(row=2,column=4)
        tk.Label(self,text="",font=mayor_menor_font,width=2).grid(row=2,column=5)
        tk.Button(self,text="1",font=font,width=3,height=1).grid(row=2,column=6)
        tk.Label(self,text="",font=mayor_menor_font,width=2).grid(row=2,column=7)
        tk.Button(self,text="1",font=font,width=3,height=1).grid(row=2,column=8)

        # Separadores
        tk.Label(self,text="",font=mayor_menor_font).grid(row=3,column=0)
        tk.Label(self,text="",font=mayor_menor_font).grid(row=3,column=2)
        tk.Label(self,text="",font=mayor_menor_font).grid(row=3,column=4)
        tk.Label(self,text="",font=mayor_menor_font).grid(row=3,column=6)
        tk.Label(self,text="",font=mayor_menor_font).grid(row=3,column=8)

        # tercer fila
        tk.Button(self,text="1",font=font,width=3,height=1).grid(row=4,column=0)
        tk.Label(self,text="",font=mayor_menor_font,width=2).grid(row=4,column=1)
        tk.Button(self,text="1",font=font,width=3,height=1).grid(row=4,column=2)
        tk.Label(self,text="",font=mayor_menor_font,width=2).grid(row=4,column=3)
        tk.Button(self,text="1",font=font,width=3,height=1).grid(row=4,column=4)
        tk.Label(self,text="",font=mayor_menor_font,width=2).grid(row=4,column=5)
        tk.Button(self,text="1",font=font,width=3,height=1).grid(row=4,column=6)
        tk.Label(self,text="",font=mayor_menor_font,width=2).grid(row=4,column=7)
        tk.Button(self,text="1",font=font,width=3,height=1).grid(row=4,column=8)

        # Separadores
        tk.Label(self,text="",font=mayor_menor_font).grid(row=5,column=0)
        tk.Label(self,text="",font=mayor_menor_font).grid(row=5,column=2)
        tk.Label(self,text="",font=mayor_menor_font).grid(row=5,column=4)
        tk.Label(self,text="",font=mayor_menor_font).grid(row=5,column=6)
        tk.Label(self,text="",font=mayor_menor_font).grid(row=5,column=8)

        # Cuarta fila
        tk.Button(self,text="1",font=font,width=3,height=1).grid(row=6,column=0)
        tk.Label(self,text="",font=mayor_menor_font,width=2).grid(row=6,column=1)
        tk.Button(self,text="1",font=font,width=3,height=1).grid(row=6,column=2)
        tk.Label(self,text="",font=mayor_menor_font,width=2).grid(row=6,column=3)
        tk.Button(self,text="1",font=font,width=3,height=1).grid(row=6,column=4)
        tk.Label(self,text="",font=mayor_menor_font,width=2).grid(row=6,column=5)
        tk.Button(self,text="1",font=font,width=3,height=1).grid(row=6,column=6)
        tk.Label(self,text="",font=mayor_menor_font,width=2).grid(row=6,column=7)
        tk.Button(self,text="1",font=font,width=3,height=1).grid(row=6,column=8)

        # Separadores
        tk.Label(self,text="",font=mayor_menor_font).grid(row=7,column=0)
        tk.Label(self,text="",font=mayor_menor_font).grid(row=7,column=2)
        tk.Label(self,text="",font=mayor_menor_font).grid(row=7,column=4)
        tk.Label(self,text="",font=mayor_menor_font).grid(row=7,column=6)
        tk.Label(self,text="",font=mayor_menor_font).grid(row=7,column=8)

        # Quinta fila
        tk.Button(self,text="1",font=font,width=3,height=1).grid(row=8,column=0)
        tk.Label(self,text="",font=mayor_menor_font,width=2).grid(row=8,column=1)
        tk.Button(self,text="1",font=font,width=3,height=1).grid(row=8,column=2)
        tk.Label(self,text="",font=mayor_menor_font,width=2).grid(row=8,column=3)
        tk.Button(self,text="1",font=font,width=3,height=1).grid(row=8,column=4)
        tk.Label(self,text="",font=mayor_menor_font,width=2).grid(row=8,column=5)
        tk.Button(self,text="1",font=font,width=3,height=1).grid(row=8,column=6)
        tk.Label(self,text="",font=mayor_menor_font,width=2).grid(row=8,column=7)
        tk.Button(self,text="1",font=font,width=3,height=1).grid(row=8,column=8)

class Juego(tk.Frame):
    def __init__(self,master):
        super().__init__(master)
        
        self.panel = Panel(self)
        self.panel.grid(row=4,column=2)
        


################################################## Funciones ################################################

############################################### Programa principal ##########################################
font = ("papyrus",32)
mayor_menor_font = ("Times",24)
