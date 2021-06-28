################################################## Imports ##################################################
import tkinter as tk
from tkinter import messagebox
from tkinter.constants import TRUE
from juego.jugar import Juego
from juego.config import config
import pickle
################################################### Clases ##################################################
# Clase de control de ventanas
class Generador():
    def __init__(self,master): # Metodo constructor: inicia la clase con la ventana principal
        self.master = master
    
    # metodo para mostrar ventana con un mensaje de error:
    def mensajeError(self,mensaje):
        messagebox.showerror("ERROR",mensaje)

    # metodo para mostrar ventana con un mensaje informativo:
    def mensajeInformativo(self,mensaje):
        messagebox.showinfo("Enhorabuena",mensaje)

    # Metodo para abrir la ventana de configuración
    def abrirConfiguracion(self):
        self.ventana_configuracion = Ventana_configuracion(self.master)
        self.ventana_configuracion.grid(row=0,column=0,sticky="nswe")
        ventana.geometry("435x256+804+300")

    # Metodo para cerrar la ventana de configuración
    def cerrarConfiguracion(self):
        self.ventana_configuracion.destroy() # Con el metodo destroy() de tkinter se cierra
        ventana.geometry("256x256+804+300")
    
    # Metodo para abrir la ventana de configuración
    def abrirJuego(self):
        self.ventana_juego = Juego(self.master,WindowManager)
        self.ventana_juego.grid(row=0,column=0,sticky="nswe")
        tk.Button(self.ventana_juego,text="Salir",command=self.cerrarJuego,font=("times",14)).place(x=1650,y=912)
        ventana.state('zoomed')
        ventana.resizable(True,True)

    # Metodo para cerrar la ventana de configuración
    def cerrarJuego(self):
        self.ventana_juego.destroy() # Con el metodo destroy() de tkinter se cierra
        ventana.state('normal')
        ventana.geometry("256x256+804+300")
        ventana.resizable(False,False)

# Clase contenedora de la ventana de configuracion
class Ventana_configuracion(tk.Frame):
    def __init__(self,master):
        super().__init__(master)

        self.facil = tk.IntVar()
        tk.Label(self,text="1. Nivel:").grid(row=0,column=0,sticky="w")
        tk.Checkbutton(self,text="Fácil",variable=self.facil,command=self.cambioDificultadFacil).grid(row=0,column=1,sticky="w")

        self.intermedio = tk.IntVar()
        tk.Checkbutton(self,text="Intermedio",variable=self.intermedio,command=self.cambioDificultadIntermedio).grid(row=1,column=1,sticky="w")

        self.dificil = tk.IntVar()
        tk.Checkbutton(self,text="Difícil",variable=self.dificil,command=self.cambioDificultadDificil).grid(row=2,column=1,sticky="w")

        self.dificultadInicial()


        tk.Label(self,text="1. Reloj:").grid(row=3,column=0,sticky="w")
        self.reloj_si = tk.IntVar()
        tk.Checkbutton(self,text="Si",variable=self.reloj_si,command=self.cambioRelojSi).grid(row=3,column=1,sticky="w")

        self.reloj_no = tk.IntVar()
        tk.Checkbutton(self,text="No",variable=self.reloj_no,command=self.cambioRelojNo).grid(row=4,column=1,sticky="w")

        self.timer = tk.IntVar()
        tk.Checkbutton(self,text="Timer",variable=self.timer,command=self.cambioRelojTimer).grid(row=5,column=1,sticky="w")

        self.relojInicial()

        verificacion_horas = self.register(self.comprobar_horas)
        verificacion_minutos_segundos = self.register(self.comprobar_minutos_segundos)

        self.hora = tk.StringVar()
        tk.Label(self,text="Hora").grid(row=3,column=2,columnspan=2)
        entry1 = tk.Entry(self,textvariable=self.hora,width=4)
        entry1.grid(row=4,column=2,columnspan=2)
        entry1.config(validate="key",validatecommand=(verificacion_horas,"%P"))

        self.minutos = tk.StringVar()
        tk.Label(self,text="Minutos").grid(row=3,column=3)
        entry2 = tk.Entry(self,textvariable=self.minutos,width=6)
        entry2.grid(row=4,column=3)
        entry2.config(validate="key",validatecommand=(verificacion_minutos_segundos,"%P"))


        self.segundos = tk.StringVar()
        tk.Label(self,text="Segundos").grid(row=3,column=4)
        entry3 = tk.Entry(self,textvariable=self.segundos,width=9)
        entry3.grid(row=4,column=4)
        entry3.config(validate="key",validatecommand=(verificacion_minutos_segundos,"%P"))

        self.horasMinutosSegundosInicial()


        tk.Label(self,text="3. Posición en la ventana del panel de dígitos:").grid(row=6,column=0,columnspan=2)

        self.derecha = tk.IntVar()
        tk.Checkbutton(self,text="Derecha",variable=self.derecha,command=self.cambioDerecha).grid(row=6,column=2,sticky="w")

        self.izquierda = tk.IntVar()
        tk.Checkbutton(self,text="Izquierda",variable=self.izquierda,command=self.cambioIzquierda).grid(row=7,column=2,sticky="w")

        self.posicionInicial()

        tk.Button(self,text="Aplicar",command=self.aplicarConfiguración).grid(row=8,column=0)
        tk.Button(self,text="Salir",command=lambda:WindowManager.cerrarConfiguracion()).grid(row=8,column=1)

    # Metodo para aplicar la configuración
    def aplicarConfiguración(self):

        # verificación y restricción de datos
        if self.facil.get() == 0 and self.intermedio.get() == 0 and self.dificil.get() == 0:
            WindowManager.mensajeError("PORFAVOR ELEGIR UNA DIFICULTAD")
            return
        if self.reloj_si.get() == 0 and self.reloj_no.get() == 0 and self.timer.get() == 0:
            WindowManager.mensajeError("PORFAVOR ELEGIR UN TIPO DE RELOJ")
            return
        if self.derecha.get() == 0 and self.izquierda.get() == 0:
            WindowManager.mensajeError("PORFAVOR ELEGIR UNA POSICIÓN PARA EL PANEL")
            return
        if self.hora.get() == "" or self.minutos.get() == "" or self.segundos.get() == "":
            WindowManager.mensajeError("PORFAVOR RELLENAR LAS HORAS, MINUTOS Y SEGUNDOS DEL RELOJ")
            return

        # Aplicar la dificultad dependiendo de cual dificultad se seleccionó
        if self.facil.get() == 1:
            config.dificultad = 0
        elif self.intermedio.get() == 1:
            config.dificultad = 1
        elif self.dificil.get() == 1:
            config.dificultad = 2

        # Aplicar el tipo de reloj dependiendo de cual dificultad se seleccionó
        if self.reloj_si.get() == 1:
            config.reloj = 0
        elif self.reloj_no.get() == 1:
            config.reloj = 1
        elif self.timer.get() == 1:
            config.reloj = 2

        # Aplicar la posición dependiendo de cual dificultad se seleccionó
        if self.derecha.get() == 1:
            config.posicion = 0
        elif self.izquierda.get() == 1:
            config.posicion = 1

        # Aplica los valores del reloj con los asignados por el usuario
        horas = int(self.hora.get())
        minutos = int(self.minutos.get())
        segundos = int(self.segundos.get())
        config.tiempo_reloj = (horas,minutos,segundos)

        # Mensaje de exito para el usuario
        WindowManager.mensajeInformativo("LA OPERACIÓN SE REALIZO CON EXITO, SERA DEVUELVO AL MENÚ PRINCIPAL")

        # Se cierra la ventana de configuración
        WindowManager.cerrarConfiguracion()
    
    # Metodo para colocar la dificultad que estaba en la configuración anterior
    def dificultadInicial(self):
        if config.dificultad == 0:
            self.facil.set(1)
        elif config.dificultad == 1:
            self.intermedio.set(1)
        elif config.dificultad == 2:
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

    # Metodo para colocar el reloj que estaba en la configuración anterior
    def relojInicial(self):
        if config.reloj == 0:
            self.reloj_si.set(1)
        if config.reloj == 1:
            self.reloj_no.set(1)
        if config.reloj == 2:
            self.timer.set(1)

    # Metodo para colocar las horas, minutos y segundos que estaba en la configuración anterior
    def horasMinutosSegundosInicial(self):
        self.hora.set(str(config.tiempo_reloj[0]))
        self.minutos.set(str(config.tiempo_reloj[1]))
        self.segundos.set(str(config.tiempo_reloj[2]))

    # Metodos para que solo se pueda elegir un tipo de reloj
    def cambioRelojSi(self):
        self.reloj_no.set(0)
        self.timer.set(0)
    def cambioRelojNo(self):
        self.reloj_si.set(0)
        self.timer.set(0)
    def cambioRelojTimer(self):
        self.reloj_si.set(0)
        self.reloj_no.set(0)
    
    # Metodo para colocar la posición que estaba en la configuración anterior
    def posicionInicial(self):
        if config.posicion == 0:
            self.derecha.set(1)
        elif config.posicion == 1:
            self.izquierda.set(1)

    # Metodos para que solo se pueda elegir una posición
    def cambioDerecha(self):
        self.izquierda.set(0)
    def cambioIzquierda(self):
        self.derecha.set(0)

    # Metodo para comprobación de horas:
    def comprobar_horas(self,entrada):
        # Comprueba si la entrada es una de las 4 opciones presentadas
        # para retornar True, de lo contrario retorna False
        if entrada == "" or entrada == "2" or entrada == "1" or entrada == "0":
            return True
        return  False
    
    # Metodo para comprobación de minutos y segundos:
    def comprobar_minutos_segundos(self,entrada):
        # Si la entrada es un string vacio retorna True
        if entrada == "":
            return True

        # Prueba a convertir un string en int
        try:
            
            # Si logra convertir el string en int
            entrada = int(entrada)

            # Comprueba si es un numero entre 0 y 59
            if 0 <= entrada <= 59:
                return True
            else:
                return False

        # Si no puede retorna False
        except ValueError:
            return False
################################################## Funciones ################################################
def guardar_top():
    confirmacion = messagebox.askyesno("¿SEGURO?","¿DESEA CERRAR EL PROGRAMA?")
    if confirmacion:
        archivo_top = open("futoshiki2021top10.dat","wb")
        pickle.dump(config.top10,archivo_top)
        archivo_top.close()
        ventana.destroy()

############################################### Programa principal ##########################################

ventana = tk.Tk() # Crea ventana principal

WindowManager = Generador(ventana) # Administra la creación de ventanas

# Hace que los contenidos de la fila 0 y columna 0 se expandan hasta lo que otros widgets
# lo permitan junto a la ventana cuando cambia de dimensiones
ventana.rowconfigure(0,weight=1)
ventana.columnconfigure(0,weight=1)


ventana.title("FUTOSHIKI") # Titulo de la ventana
ventana.geometry("256x256+804+300") # dimensiones de la ventana
ventana.resizable(False,False)

menu = tk.Frame(ventana) # Marco que contiene el menu principal
menu.grid(row=0,column=0) # Coloca el marco

tk.Label(menu,text="FUTOSHIKI",font=("Papyrus",20)).grid(row=0,column=0) # Titulo principal en el menu

# Separador
tk.Label(menu).grid(row=1,column=0)

# Opciones del menu
tk.Button(menu,text="JUGAR",font=("Papyrus"),width=10,height=1,command=WindowManager.abrirJuego).grid(row=2,column=0)
tk.Button(menu,text="Configurar",font=("Papyrus"),width=10,height=1,command=WindowManager.abrirConfiguracion).grid(row=3,column=0)
tk.Button(menu,text="Ayuda",font=("Papyrus"),width=10,height=1).grid(row=4,column=0)
tk.Button(menu,text="Acerca de",font=("Papyrus"),width=10,height=1,command=lambda:messagebox.showinfo("Acerca de","FUTOSHIKI\nVer. 1.0 \
\nCreador: Deyan Sanabria\nFecha de creación: 4 de Junio del 2021")).grid(row=5,column=0)

# revisa cuando la ventana se cierra para ejecutar la funcion de cerrado
ventana.protocol("WM_DELETE_WINDOW",guardar_top)

ventana.mainloop() # Loop de ventana para eventos
