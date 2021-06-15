################################################## Imports ##################################################
import tkinter as tk

################################################### Clases ##################################################
# Clase de control de ventanas
class Generador():
    def __init__(self,master): # Metodo constructor: inicia la clase con la ventana principal
        self.master = master

    # Metodo para abrir la ventana de configuración
    def abrirConfiguracion(self):
        self.ventana_configuracion = Configuracion(self.master)
        self.ventana_configuracion.grid(row=0,column=0,sticky="nswe")
    
    # Metodo para cerrar la ventana de configuración
    def cerrarConfiguracion(self):
        self.ventana_configuracion.destroy() # Con el metodo destroy() de tkinter se cierra

# Clase contenedora de la ventana de configuracion
class Configuracion(tk.Frame):
    dificultad = 0
    def __init__(self,master):
        super().__init__(master)

        self.facil = tk.IntVar()
        tk.Label(self,text="1. Nivel:").grid(row=0,column=0)
        tk.Checkbutton(self,text="Fácil",variable=self.facil,command=self.cambioDificultadFacil).grid(row=0,column=1,sticky="w")

        self.intermedio = tk.IntVar()
        tk.Checkbutton(self,text="Intermedio",variable=self.intermedio,command=self.cambioDificultadIntermedio).grid(row=1,column=1,sticky="w")

        self.dificil = tk.IntVar()
        tk.Checkbutton(self,text="Difícil",variable=self.dificil,command=self.cambioDificultadDificil).grid(row=2,column=1,sticky="w")

        self.dificultadInicial()

        tk.Button(self,text="Aplicar",command=None).grid(row=8,column=0)
        tk.Button(self,text="Salir",command=lambda:WindowManager.cerrarConfiguracion()).grid(row=8,column=1)

    # Metodo para colocar la dificultad que estaba elegida desde antes
    def dificultadInicial(self):
        if self.dificultad == 0:
            self.facil.set(1)
        elif self.dificultad == 1:
            self.intermedio.set(1)
        elif self.dificultad == 2:
            self.dificil.set(1)
    # Metodos para que solo se pueda seleccionar una dificultad
    def cambioDificultadFacil(self):
        self.intermedio.set(0)
        self.dificil.set(0)
    def cambioDificultadIntermedio(self):
        self.facil.set(0)
        self.dificil.set(0)
    def cambioDificultadDificil(self):
        self.intermedio.set(0)
        self.facil.set(0)
        

################################################## Funciones ################################################


############################################### Programa principal ##########################################
ventana = tk.Tk() # Crea ventana principal

WindowManager = Generador(ventana) # Administra la creación de ventanas

# Hace que los contenidos de la fila 0 y columna 0 se expandan hasta lo que otros widgets
# lo permitan junto a la ventana cuando cambia de dimensiones
ventana.rowconfigure(0,weight=1)
ventana.columnconfigure(0,weight=1)


ventana.title("FUTOSHIKI") # Titulo de la ventana
ventana.geometry("256x256+804+300") # dimensiones de la ventana

menu = tk.Frame(ventana) # Marco que contiene el menu principal
menu.grid(row=0,column=0) # Coloca el marco

tk.Label(menu,text="FUTOSHIKI",font=("Papyrus",20)).grid(row=0,column=0) # Titulo principal en el menu

# Separador
tk.Label(menu).grid(row=1,column=0)

# Opciones del menu
tk.Button(menu,text="JUGAR",font=("Papyrus"),width=10,height=1,command= None).grid(row=2,column=0)
tk.Button(menu,text="Configurar",font=("Papyrus"),width=10,height=1,command= lambda: WindowManager.abrirConfiguracion()).grid(row=3,column=0)
tk.Button(menu,text="Ayuda",font=("Papyrus"),width=10,height=1).grid(row=4,column=0)
tk.Button(menu,text="Acerca de",font=("Papyrus"),width=10,height=1).grid(row=5,column=0)

ventana.mainloop() # Loop de ventana para eventos
