################################################## Imports ##################################################
import tkinter as tk
from typing import Collection
from juego.config import config
################################################### Clases ##################################################
class Panel(tk.Frame):
    def __init__(self,master,panel_digitos):
        super().__init__(master)

        self.panel_digitos = panel_digitos

        # Primera fila
        self.boton1 = tk.Button(self,text="",font=font,width=3,height=1,command=lambda:self.cambioNumero(self.boton1))
        self.boton1.grid(row=0,column=0)

        Lateral1 = tk.Label(self,text="",font=mayor_menor_font,width=2)
        Lateral1.grid(row=0,column=1)

        self.boton2 = tk.Button(self,text="",font=font,width=3,height=1,command=lambda:self.cambioNumero(self.boton2))
        self.boton2.grid(row=0,column=2)

        Lateral2 = tk.Label(self,text="",font=mayor_menor_font,width=2)
        Lateral2.grid(row=0,column=3)

        self.boton3 = tk.Button(self,text="",font=font,width=3,height=1,command=lambda:self.cambioNumero(self.boton3))
        self.boton3.grid(row=0,column=4)
        
        Lateral3 = tk.Label(self,text="",font=mayor_menor_font,width=2)
        Lateral3.grid(row=0,column=5)

        self.boton4 = tk.Button(self,text="",font=font,width=3,height=1,command=lambda:self.cambioNumero(self.boton4))
        self.boton4.grid(row=0,column=6)

        Lateral4 = tk.Label(self,text="",font=mayor_menor_font,width=2)
        Lateral4.grid(row=0,column=7)

        self.boton5 = tk.Button(self,text="",font=font,width=3,height=1,command=lambda:self.cambioNumero(self.boton5))
        self.boton5.grid(row=0,column=8)

        # Fila1 para una matriz de botones
        fila1 = [self.boton1,self.boton2,self.boton3,self.boton4,self.boton5]
        
        # Fila1 para los espacios laterales entre botones
        fila1lateral = [Lateral1,Lateral2,Lateral3,Lateral4]

        # Separadores
        Superior1 = tk.Label(self,text="",font=mayor_menor_font)
        Superior1.grid(row=1,column=0)

        Superior2 = tk.Label(self,text="",font=mayor_menor_font)
        Superior2.grid(row=1,column=2)

        Superior3 = tk.Label(self,text="",font=mayor_menor_font)
        Superior3.grid(row=1,column=4)

        Superior4 = tk.Label(self,text="",font=mayor_menor_font)
        Superior4.grid(row=1,column=6)

        Superior5 = tk.Label(self,text="",font=mayor_menor_font)
        Superior5.grid(row=1,column=8)


        # Segunda fila
        self.boton6 = tk.Button(self,text="",font=font,width=3,height=1,command=lambda:self.cambioNumero(self.boton6))
        self.boton6.grid(row=2,column=0)

        Lateral1 = tk.Label(self,text="",font=mayor_menor_font,width=2)
        Lateral1.grid(row=2,column=1)

        self.boton7 = tk.Button(self,text="",font=font,width=3,height=1,command=lambda:self.cambioNumero(self.boton7))
        self.boton7.grid(row=2,column=2)

        Lateral2 = tk.Label(self,text="",font=mayor_menor_font,width=2)
        Lateral2.grid(row=2,column=3)
        
        self.boton8 = tk.Button(self,text="",font=font,width=3,height=1,command=lambda:self.cambioNumero(self.boton8))
        self.boton8.grid(row=2,column=4)

        Lateral3 = tk.Label(self,text="",font=mayor_menor_font,width=2)
        Lateral3.grid(row=2,column=5)

        self.boton9 = tk.Button(self,text="",font=font,width=3,height=1,command=lambda:self.cambioNumero(self.boton9))
        self.boton9.grid(row=2,column=6)

        Lateral4 = tk.Label(self,text="",font=mayor_menor_font,width=2)
        Lateral4.grid(row=2,column=7)

        self.boton10 = tk.Button(self,text="",font=font,width=3,height=1,command=lambda:self.cambioNumero(self.boton10))
        self.boton10.grid(row=2,column=8)
        
        # Fila2 para una matriz de botones
        fila2 = [self.boton6,self.boton7,self.boton8,self.boton9,self.boton10]

        # Fila2 para los espacios laterales entre botones
        fila2lateral = [Lateral1,Lateral2,Lateral3,Lateral4]
        
        # Fila1 Para los espacios superiores/inferiores entre botones
        fila1superior = [Superior1,Superior2,Superior3,Superior4,Superior5]

        # Separadores
        Superior1 = tk.Label(self,text="",font=mayor_menor_font)
        Superior1.grid(row=3,column=0)

        Superior2 = tk.Label(self,text="",font=mayor_menor_font)
        Superior2.grid(row=3,column=2)

        Superior3 = tk.Label(self,text="",font=mayor_menor_font)
        Superior3.grid(row=3,column=4)

        Superior4 = tk.Label(self,text="",font=mayor_menor_font)
        Superior4.grid(row=3,column=6)
        
        Superior5 = tk.Label(self,text="",font=mayor_menor_font)
        Superior5.grid(row=3,column=8)

        # tercer fila
        self.boton11 = tk.Button(self,text="",font=font,width=3,height=1,command=lambda:self.cambioNumero(self.boton11))
        self.boton11.grid(row=4,column=0)

        Lateral1 = tk.Label(self,text="",font=mayor_menor_font,width=2)
        Lateral1.grid(row=4,column=1)

        self.boton12 = tk.Button(self,text="",font=font,width=3,height=1,command=lambda:self.cambioNumero(self.boton12))
        self.boton12.grid(row=4,column=2)

        Lateral2 = tk.Label(self,text="",font=mayor_menor_font,width=2)
        Lateral2.grid(row=4,column=3)

        self.boton13 = tk.Button(self,text="",font=font,width=3,height=1,command=lambda:self.cambioNumero(self.boton13))
        self.boton13.grid(row=4,column=4)

        Lateral3 = tk.Label(self,text="",font=mayor_menor_font,width=2)
        Lateral3.grid(row=4,column=5)

        self.boton14 = tk.Button(self,text="",font=font,width=3,height=1,command=lambda:self.cambioNumero(self.boton14))
        self.boton14.grid(row=4,column=6)

        Lateral4 = tk.Label(self,text="",font=mayor_menor_font,width=2)
        Lateral4.grid(row=4,column=7)

        self.boton15 = tk.Button(self,text="",font=font,width=3,height=1,command=lambda:self.cambioNumero(self.boton15))
        self.boton15.grid(row=4,column=8)

        
        # Fila3 para una matriz de botones
        fila3 = [self.boton11,self.boton12,self.boton13,self.boton14,self.boton15]

        # Fila3 para los espacios laterales entre botones
        fila3lateral = [Lateral1,Lateral2,Lateral3,Lateral4]

        # Fila2 Para los espacios superiores/inferiores entre botones
        fila2superior = [Superior1,Superior2,Superior3,Superior4,Superior5]

        # Separadores
        Superior1 = tk.Label(self,text="",font=mayor_menor_font)
        Superior1.grid(row=5,column=0)

        Superior2 = tk.Label(self,text="",font=mayor_menor_font)
        Superior2.grid(row=5,column=2)

        Superior3 = tk.Label(self,text="",font=mayor_menor_font)
        Superior3.grid(row=5,column=4)

        Superior4 = tk.Label(self,text="",font=mayor_menor_font)
        Superior4.grid(row=5,column=6)

        Superior5 = tk.Label(self,text="",font=mayor_menor_font)
        Superior5.grid(row=5,column=8)

        # Cuarta fila
        self.boton16 = tk.Button(self,text="",font=font,width=3,height=1,command=lambda:self.cambioNumero(self.boton16))
        self.boton16.grid(row=6,column=0)

        Lateral1 = tk.Label(self,text="",font=mayor_menor_font,width=2)
        Lateral1.grid(row=6,column=1)

        self.boton17 = tk.Button(self,text="",font=font,width=3,height=1,command=lambda:self.cambioNumero(self.boton17))
        self.boton17.grid(row=6,column=2)

        Lateral2 = tk.Label(self,text="",font=mayor_menor_font,width=2)
        Lateral2.grid(row=6,column=3)

        self.boton18 = tk.Button(self,text="",font=font,width=3,height=1,command=lambda:self.cambioNumero(self.boton18))
        self.boton18.grid(row=6,column=4)

        Lateral3 = tk.Label(self,text="",font=mayor_menor_font,width=2)
        Lateral3.grid(row=6,column=5)

        self.boton19 = tk.Button(self,text="",font=font,width=3,height=1,command=lambda:self.cambioNumero(self.boton19))
        self.boton19.grid(row=6,column=6)
        
        Lateral4 = tk.Label(self,text="",font=mayor_menor_font,width=2)
        Lateral4.grid(row=6,column=7)

        self.boton20 = tk.Button(self,text="",font=font,width=3,height=1,command=lambda:self.cambioNumero(self.boton20))
        self.boton20.grid(row=6,column=8)

        # Fila4 para una matriz de botones
        fila4 = [self.boton16,self.boton17,self.boton18,self.boton19,self.boton20]

        # Fila4 para los espacios laterales entre botones
        fila4lateral = [Lateral1,Lateral2,Lateral3,Lateral4]

        # Fila3 Para los espacios superiores/inferiores entre botones
        fila3superior = [Superior1,Superior2,Superior3,Superior4,Superior5]

        # Separadores
        Superior1 = tk.Label(self,text="",font=mayor_menor_font)
        Superior1.grid(row=7,column=0)

        Superior2 = tk.Label(self,text="",font=mayor_menor_font)
        Superior2.grid(row=7,column=2)

        Superior3 = tk.Label(self,text="",font=mayor_menor_font)
        Superior3.grid(row=7,column=4)
        
        Superior4 = tk.Label(self,text="",font=mayor_menor_font)
        Superior4.grid(row=7,column=6)
        
        Superior5 = tk.Label(self,text="",font=mayor_menor_font)
        Superior5.grid(row=7,column=8)

        # Quinta fila
        self.boton21 = tk.Button(self,text="",font=font,width=3,height=1,command=lambda:self.cambioNumero(self.boton21))
        self.boton21.grid(row=8,column=0)

        Lateral1 = tk.Label(self,text="",font=mayor_menor_font,width=2)
        Lateral1.grid(row=8,column=1)

        self.boton22 = tk.Button(self,text="",font=font,width=3,height=1,command=lambda:self.cambioNumero(self.boton22))
        self.boton22.grid(row=8,column=2)

        Lateral2 = tk.Label(self,text="",font=mayor_menor_font,width=2)
        Lateral2.grid(row=8,column=3)

        self.boton23 = tk.Button(self,text="",font=font,width=3,height=1,command=lambda:self.cambioNumero(self.boton23))
        self.boton23.grid(row=8,column=4)

        Lateral3 = tk.Label(self,text="",font=mayor_menor_font,width=2)
        Lateral3.grid(row=8,column=5)

        self.boton24 = tk.Button(self,text="",font=font,width=3,height=1,command=lambda:self.cambioNumero(self.boton24))
        self.boton24.grid(row=8,column=6)

        Lateral4 = tk.Label(self,text="",font=mayor_menor_font,width=2)
        Lateral4.grid(row=8,column=7)

        self.boton25 = tk.Button(self,text="",font=font,width=3,height=1,command=lambda:self.cambioNumero(self.boton25))
        self.boton25.grid(row=8,column=8)
        
        # Fila5 para una matriz de botones
        fila5 = [self.boton21,self.boton22,self.boton23,self.boton24,self.boton25]

        # Fila5 para los espacios laterales entre botones
        fila5lateral = [Lateral1,Lateral2,Lateral3,Lateral4]
        
        # Fila4 Para los espacios superiores/inferiores entre botones
        fila4superior = [Superior1,Superior2,Superior3,Superior4,Superior5]

        # Matriz de botones
        self.matriz_botones = [fila1,fila2,fila3,fila4,fila5]

        # Matriz de espacios laterales
        self.matriz_laterales = [fila1lateral,fila2lateral,fila3lateral,fila4lateral,fila5lateral]

        # Matriz de espacios superiores/inferiores
        self.matriz_superior = [fila1superior,fila2superior,fila3superior,fila4superior]

        self.desactivarPanel()

    # Metodo para cambiar el numero del panel
    def cambioNumero(self,boton):
        boton["text"] = self.panel_digitos.digito
    
    # Metodo para desactivar los botones del panel
    def desactivarPanel(self):
        for fila in self.matriz_botones:
            for boton in fila:
                boton["state"] = tk.DISABLED

    # Metodo para activar los botones del panel
    def activarPanel(self):
        for fila in self.matriz_botones:
            for boton in fila:
                boton["state"] = tk.NORMAL

    # Metodo para cargar juego de la lista de partidas
    def cargarNumeros(self,coordenada,numero):
        fila = coordenada[0]
        columna = coordenada[1]
        self.matriz_botones[fila][columna]["text"] = numero
        self.matriz_botones[fila][columna]["state"] = tk.DISABLED

    # Metodo para cargar juego de la lista de partidas
    def cargarMayoreMenoresLaterales(self,coordenada,simbolo):
        fila = coordenada[0]
        columna = coordenada[1]
        self.matriz_laterales[fila][columna]["text"] = simbolo

    def cargarMayoreMenoresSuperiores(self,coordenada,simbolo):
        fila = coordenada[0]
        columna = coordenada[1]
        self.matriz_superior[fila][columna]["text"] = simbolo

class Digitos(tk.Frame):
    digito = 1
    def __init__(self,master):
        super().__init__(master)
        self.digito1 = tk.Button(self,text=1,font=font,bg="green",command=lambda: self.cambioBoton(1,self.digito1))
        self.digito2 = tk.Button(self,text=2,font=font,bg="White",command=lambda: self.cambioBoton(2,self.digito2))
        self.digito3 = tk.Button(self,text=3,font=font,bg="White",command=lambda: self.cambioBoton(3,self.digito3))
        self.digito4 = tk.Button(self,text=4,font=font,bg="White",command=lambda: self.cambioBoton(4,self.digito4))
        self.digito5 = tk.Button(self,text=5,font=font,bg="White",command=lambda: self.cambioBoton(5,self.digito5))
        
        self.digito1.grid(column=0,row=0)
        self.digito2.grid(column=0,row=1)
        self.digito3.grid(column=0,row=2)
        self.digito4.grid(column=0,row=3)
        self.digito5.grid(column=0,row=4)

    def cambioBoton(self,digito,boton):
        if self.digito == 1:
            self.digito1["bg"] = "White"
        elif self.digito == 2:
            self.digito2["bg"] = "White"
        elif self.digito == 3:
            self.digito3["bg"] = "White"
        elif self.digito == 4:
            self.digito4["bg"] = "White"
        elif self.digito == 5:
            self.digito5["bg"] = "White"
        self.digito = digito
        boton["bg"] = "green"

class Juego(tk.Frame):
    def __init__(self,master):
        super().__init__(master)
        if config.posicion == 0:
            COLUMNA_DIGITOS = 4
            tk.Label(self).grid(row=4,column=3)
        elif config.posicion == 1:
            COLUMNA_DIGITOS = 0
            tk.Label(self).grid(row=4,column=1)

        self.digitos = Digitos(self)
        self.digitos.grid(row=4,column=COLUMNA_DIGITOS)

        self.panel = Panel(self,self.digitos)
        self.panel.grid(row=4,column=2)
        
################################################## Funciones ################################################

############################################### Programa principal ##########################################
font = ("papyrus",32)
mayor_menor_font = ("Times",24)