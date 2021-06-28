################################################## Imports ##################################################
from multiprocessing.context import Process
import tkinter as tk
from tkinter.constants import X
from juego.config import config
import pickle
import random
from tkinter import messagebox

################################################### Clases ##################################################
class Panel(tk.Frame):
    mayores_menores = ()
    ctrlz = []
    def __init__(self,master,panel_digitos,manager,reloj):
        super().__init__(master)

        # Objeto que de llamada
        self.master = master

        self.panel_digitos = panel_digitos

        self.WindowManager = manager

        self.reloj = reloj

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

        # Columnas para una matriz de botones que va por columnas
        columna1 = [self.boton1,self.boton6,self.boton11,self.boton16,self.boton21]
        columna2 = [self.boton2,self.boton7,self.boton12,self.boton17,self.boton22]
        columna3 = [self.boton3,self.boton8,self.boton13,self.boton18,self.boton23]
        columna4 = [self.boton4,self.boton9,self.boton14,self.boton19,self.boton24]
        columna5 = [self.boton5,self.boton10,self.boton15,self.boton20,self.boton25]

        # Matriz de botones por columnas
        self.matriz_botones_columnas = [columna1,columna2,columna3,columna4,columna5]

        # Matriz de botones por filas
        self.matriz_botones_filas = [fila1,fila2,fila3,fila4,fila5]

        # Matriz de espacios laterales
        self.matriz_laterales = [fila1lateral,fila2lateral,fila3lateral,fila4lateral,fila5lateral]

        # Matriz de espacios superiores/inferiores
        self.matriz_superior = [fila1superior,fila2superior,fila3superior,fila4superior]

    # metodo para buscar si un boton esta en una fila o columna
    # Entradas: el boton y el string
    # salidas: Valor booleano dependiendo si esta o no
    def estaEnFilaColumna(self,boton,string):
        # Si son columnas, busca la matriz de columnas
        if string == "COLUMNA":
            matriz = self.matriz_botones_columnas

        # Si son filas, busca la matriz de filas
        elif string == "FILA":
            matriz = self.matriz_botones_filas

        # con un ciclo for busca en cada fila o columna
        for fila in matriz:
            # Si encuentra que esta el boton
            if boton in fila:

                # con un ciclo for, busca en todos los botones de esa fila o columna si alguno tiene
                # el valor que se le quiere asignar al boton
                for botones in fila:
                    if botones['text'] == self.panel_digitos.digito:

                        # En caso de que se encuentre de vuelve True
                        return True

        # Caso contrario devuelve False
        return False
    
    # Metodo para detectar si se gano el juego
    # Se basa en que las restricciones nunca van a permitir que se pueda colocar un numero de forma incorrecta
    # por lo que si panel del juego esta completamente lleno, significa que se termino.
    # Por lo que busca en cada boton del panel, si existe algun boton que tenga un string vacio, en caso
    # de que exista, de vuelve "False" que significa que no se ha ganado el juego, pero si no se encuentra un boton
    # vacio, se devuelve "True" indicando que gano el juego
    def ganoJuego(self):
        for fila in self.matriz_botones_filas:
            for boton in fila:
                if boton['text'] == "":
                    return False
        return True

    # Metodo para detectar restricciones
    # Entradas: el boton
    # Salidas: Valor booleano dependiendo si se comple 
    # de forma correcta la restriccion o no y un string
    # que contiene si era una comparacion de mayor que o menor que
    def es_mayor_menor_lateral(self,boton):
        
        # A base de una lista conteniendo todos los mayores y menores
        # se busca por cada una de ellas y con un simbolo se identifica
        # hacia que direccion van
        for tupla in self.mayores_menores:

            # se obtiene la ubicacion de la comparación
            fila = tupla[0][0]
            columna = tupla[0][1]

            # Si la comparación es horizontal
            if tupla[1] == ">" or tupla[1] == "<": 

                # Condicionales para saber, dependiendo de cual de los botones,
                # izquierdo o derecho, del simbolo se preciono y posteriormente hacer
                # una comparación de la forma correcta
                if boton == self.matriz_botones_filas[fila][columna]:
                    boton1 = self.panel_digitos.digito
                    boton2 = self.matriz_botones_filas[fila][columna+1]['text']
                elif boton == self.matriz_botones_filas[fila][columna+1]:
                    boton1 = self.matriz_botones_filas[fila][columna]['text']
                    boton2 = self.panel_digitos.digito
                else:
                    continue

                # Si alguno de los dos botones contiene un string vacio, 
                # no se puede hacer comparación por lo que se devuelve "True"
                # y un string vacio
                if boton1 == "" or boton2 == "":
                    return True,""

                # En esta parte se hace la comparación y en caso de que se haya hecho de forma
                # correcta, se devuelve True con un string vacio, de lo contrario de vuelve "False"
                # con un String indicando el signo de comparación
                if tupla[1] == ">":
                    if boton1 > boton2:
                        return True,""
                    return False,"MAYOR"
                elif tupla[1] == "<":
                    if boton1 < boton2:
                        return True,""
                    return False,"MENOR"
            
            # Si la comparación es vertical
            if tupla[1] == "˅" or tupla[1] == "˄":

                # Condicionales para saber, dependiendo de cual de los botones,
                # izquierdo o derecho, del simbolo se preciono y posteriormente hacer
                # una comparación de la forma correcta
                if boton == self.matriz_botones_filas[fila][columna]:
                    boton1 = self.panel_digitos.digito
                    boton2 = self.matriz_botones_filas[fila+1][columna]['text']
                elif boton == self.matriz_botones_filas[fila+1][columna]:
                    boton1 = self.matriz_botones_filas[fila][columna]['text']
                    boton2 = self.panel_digitos.digito
                else:
                    continue

                # Si alguno de los dos botones contiene un string vacio, 
                # no se puede hacer comparación por lo que se devuelve "True"
                # y un string vacio
                if boton1 == "" or boton2 == "":
                    return True,""

                # En esta parte se hace la comparación y en caso de que se haya hecho de forma
                # correcta, se devuelve True con un string vacio, de lo contrario de vuelve "False"
                # con un String indicando el signo de comparación
                if tupla[1] == "˅":
                    if boton1 > boton2:
                        return True,""
                    return False,"MAYOR"
                elif tupla[1] == "˄":
                    if boton1 < boton2:
                        return True,""
                    return False,"MENOR"

        # Si nada de lo anterior se cumple, se retorna True con un string vacio
        return True,""

    # metodo para buscar la fila y la columna de un boton
    def buscarFilaColumna(self,boton):
        for fila in range(5):
            for columna in range(5):
                if boton == self.matriz_botones_filas[fila][columna]:
                    return fila,columna

    # metodo para ordenar el top10 mediante un algoritmo de 
    # acomodo.
    def ordenarTop10(self):
        lista_temporal = []
        lista_salida = []
        for jugada in config.top10[config.dificultad_actual]:
            lista_temporal.append(jugada[0])
        indices = lista_temporal.copy()
        while lista_temporal != []:
            elemento = min(lista_temporal)
            indice = indices.index(elemento)
            indice2 = lista_temporal.index(elemento)
            del lista_temporal[indice2]
            lista_salida.append(config.top10[config.dificultad_actual][indice])
        config.top10[config.dificultad_actual] = lista_salida[:10]

    # Metodo para cambiar el numero del panel
    def cambioNumero(self,boton):
        # Si el juego esta en progreso realiza las acciones correspondientes
        if self.master.en_progreso == True:
            
            # revisa si el elemento no esta en la fila, en caso que si este, se manda un mensaje al usuario y se 
            # coloca el boton en rojo que el usuario presiono
            if self.estaEnFilaColumna(boton,"FILA"):
                boton['bg'] = "red"
                messagebox.showerror("ERROR","JUGADA NO ES VÁLIDA PORQUE EL ELEMENTO YA ESTÁ EN LA FILA")
                boton['bg'] = "SystemButtonFace"
                return

            # revisa si el elemento no esta en la columna, en caso que si este, se manda un mensaje al usuario y se 
            # coloca el boton en rojo que el usuario presiono
            if self.estaEnFilaColumna(boton,"COLUMNA"):
                boton['bg'] = "red"
                messagebox.showerror("ERROR","JUGADA NO ES VÁLIDA PORQUE EL ELEMENTO YA ESTÁ EN LA COLUMNA")
                boton['bg'] = "SystemButtonFace"
                return
            
            # revisa si el elemento cumple con los signos de mayor o menor, en caso que no lo haga, se manda un mensaje al usuario y se 
            # coloca el boton en rojo que el usuario presiono
            validacion,string = self.es_mayor_menor_lateral(boton)
            if not(validacion):
                boton['bg'] = "red"
                messagebox.showerror("ERROR","JUGADA NO ES VÁLIDA PORQUE NO CUMPLE CON LA RESTRICCIÓN DE " + string)
                boton['bg'] = "SystemButtonFace"
                return
            
            # si lo anterior no se cumple:
            # se obtiene la fila y columna del boton
            fila,columna = self.buscarFilaColumna(boton)

            # se añade la siguiente accion a la pila de jugadas
            self.ctrlz.append((fila,columna))
            
            # Se cambia el texto del boton
            boton["text"] = self.panel_digitos.digito

            # se verifica si se gano el juego
            if self.ganoJuego():
                #En caso que si, se detiene el reloj y se manda un mensaje
                # de exito
                self.reloj.detenerReloj()
                messagebox.showinfo("¡EXCELENTE!","JUEGO TERMINADO CON ÉXITO")

                # se verifica si el timer estaba en uso y no se paso el tiempo para
                # convertir el tiempo que falta en tiempo que paso
                if config.reloj == 2 and not(self.reloj.cambio_cronometro):
                    tiempo1 =  3600*config.tiempo_reloj[0]
                    tiempo1 += 60*config.tiempo_reloj[1]
                    tiempo1 += config.tiempo_reloj[2]
                    self.reloj.tiempo = tiempo1 - self.reloj.tiempo

                # se agrega al top 10 la jugada
                config.top10[config.dificultad_actual].append((self.reloj.tiempo,self.master.nombre_jugador.get()))
                
                # se ordena el top 10 por el nuevo elemento
                self.ordenarTop10()

                # se reinicia la pestaña
                self.WindowManager.cerrarJuego()
                self.WindowManager.abrirJuego()

    # Metodo para colocar los numeros del juego en los botones a la
    # hora de cargar el nuevo nivel
    def cargarNumeros(self,coordenada,numero,desabilitar):
        fila = coordenada[0]
        columna = coordenada[1]
        self.matriz_botones_filas[fila][columna]["text"] = numero
        if desabilitar:
            self.matriz_botones_filas[fila][columna]["state"] = tk.DISABLED

    # Metodo para colocar los menores y mayores que en los laterales de los botones a la
    # hora de cargar el nuevo nivel
    def cargarMayoreMenoresLaterales(self,coordenada,simbolo):
        fila = coordenada[0]
        columna = coordenada[1]
        self.matriz_laterales[fila][columna]["text"] = simbolo

    # Metodo para colocar los menores y mayores que en la parte superior o inferior de los botones a la
    # hora de cargar el nuevo nivel
    def cargarMayoreMenoresSuperiores(self,coordenada,simbolo):
        fila = coordenada[0]
        columna = coordenada[1]
        self.matriz_superior[fila][columna]["text"] = simbolo

    # Metodo para cargar el juego en el Panel
    def cargarPartida(self):
        # Se elige un juego aleatorio
        juego = random.randint(0,2)

        # Se usa la dificultad escogida por el juegador
        dificultad = config.dificultad
        
        if config.cargar_juego:
            config.cargar_juego = False
            juego = config.juego_actual
            dificultad = config.dificultad_actual

        config.juego_actual = juego
        config.dificultad_actual = dificultad

        # Se hace un ciclo que recorra la partida que se va a mostrar
        for tupla in partidas[dificultad][juego]:

            # Se obtiene el numero o simbolo que hay que colocar
            simbolo_numero = tupla[0]

            # Se obtienen las coordenadas donde hay que colocarlo dentro de la matriz de botones y espacios
            coordenadas = tupla[1:]

            # Con condicionales se elije cual metodo de los anteriormente creados usar para colocar los
            # elementos en el panel
            if simbolo_numero == ">" or tupla[0] == "<":
                self.mayores_menores += ((coordenadas,simbolo_numero),)
                self.cargarMayoreMenoresLaterales(coordenadas,simbolo_numero)
            elif simbolo_numero == "˅" or tupla[0] == "˄":
                self.mayores_menores += ((coordenadas,simbolo_numero),)
                self.cargarMayoreMenoresSuperiores(coordenadas,simbolo_numero)
            else:
                simbolo_numero = int(simbolo_numero)
                self.cargarNumeros(coordenadas,simbolo_numero,True)

# Clase que tiene la ventana del top 10
class Top10(tk.Frame):
    def __init__(self,master):
        super().__init__(master)

        # Frames para poder colocar los tops de forma acomodada y poder moverlos como se quiera
        # de forma facil
        top_facil = tk.Frame(self)
        top_intermedio = tk.Frame(self)
        top_dificil = tk.Frame(self)

        # indica a que top se refiere la columna
        tk.Label(self,text="NIVEL FACIL",font=mayor_menor_font).place(x=180,y=150)
        tk.Label(self,text="NIVEL INTERMEDIO",font=mayor_menor_font).place(x=810,y=150)
        tk.Label(self,text="NIVEL DIFICIL",font=mayor_menor_font).place(x=1560,y=150)

        # voton para volver
        tk.Button(self,text="volver",font=mayor_menor_font,command=self.master.cerrarTop10).place(x=900,y=800)

        # se coloca los tops
        top_facil.place(x=100,y=200)
        top_intermedio.place(x=800,y=200)
        top_dificil.place(x=1500,y=200)

        # revisa que la lista de nivel facil no este vacia
        if len(config.top10[0]) != 0:
            # variable contador: cuenta por cual numero del top se va
            contador = 1

            # se coloca una label para indicar el jugador y el tiempo que hizo
            tk.Label(top_facil,text="JUGADOR",font=mayor_menor_font).grid(row=0,column=1)
            tk.Label(top_facil,text="TIEMPO",font=mayor_menor_font).grid(row=0,column=2)

            # ciclo for: coloca los datos en pantalla de los top 10
            for jugador in config.top10[0]:

                # se convierte el tiempo de segundos a horas, minutos y segundos
                horas = jugador[0]//3600
                tiempo_restante = jugador[0]%3600
                minutos = tiempo_restante//60
                segundos = tiempo_restante%60

                # se colocan en un formato especifico
                tiempo = "{:02d}:{:02d}:{:02d}".format(horas,minutos,segundos)
                
                # se colocan en pantalla
                tk.Label(top_facil,text=str(contador)+".",font=mayor_menor_font).grid(row=contador,column=0)
                tk.Label(top_facil,text=jugador[1],font=mayor_menor_font).grid(row=contador,column=1)
                tk.Label(top_facil,text=tiempo,font=mayor_menor_font).grid(row=contador,column=2)

                # avanza el contador
                contador += 1
        
        # revisa que la lista de nivel intermedio no este vacia
        if len(config.top10[1]) != 0:

            # variable contador: cuenta por cual numero del top se va
            contador = 1

            # se coloca una label para indicar el jugador y el tiempo que hizo
            tk.Label(top_intermedio,text="JUGADOR",font=mayor_menor_font).grid(row=0,column=1)
            tk.Label(top_intermedio,text="TIEMPO",font=mayor_menor_font).grid(row=0,column=2)

            # ciclo for: coloca los datos en pantalla de los top 10
            for jugador in config.top10[1]:

                # se convierte el tiempo de segundos a horas, minutos y segundos
                horas = jugador[0]//3600
                tiempo_restante = jugador[0]%3600
                minutos = tiempo_restante//60
                segundos = tiempo_restante%60

                # se colocan en un formato especifico
                tiempo = "{:02d}:{:02d}:{:02d}".format(horas,minutos,segundos)

                # se colocan en pantalla
                tk.Label(top_intermedio,text=str(contador)+".",font=mayor_menor_font).grid(row=contador,column=0)
                tk.Label(top_intermedio,text=jugador[1],font=mayor_menor_font).grid(row=contador,column=1)
                tk.Label(top_intermedio,text=tiempo,font=mayor_menor_font).grid(row=contador,column=2)

                # avanza el contador
                contador += 1

        # revisa que la lista de nivel dificil no este vacia
        if len(config.top10[2]) != 0:

            # variable contador: cuenta por cual numero del top se va
            contador = 1

            # se coloca una label para indicar el jugador y el tiempo que hizo
            tk.Label(top_dificil,text="JUGADOR",font=mayor_menor_font).grid(row=0,column=1)
            tk.Label(top_dificil,text="TIEMPO",font=mayor_menor_font).grid(row=0,column=2)

            # ciclo for: coloca los datos en pantalla de los top 10
            for jugador in config.top10[2]:

                # se convierte el tiempo de segundos a horas, minutos y segundos
                horas = jugador[0]//3600
                tiempo_restante = jugador[0]%3600
                minutos = tiempo_restante//60
                segundos = tiempo_restante%60

                # se colocan en un formato especifico
                tiempo = "{:02d}:{:02d}:{:02d}".format(horas,minutos,segundos)

                # se colocan en pantalla
                tk.Label(top_dificil,text=str(contador)+".",font=mayor_menor_font).grid(row=contador,column=0)
                tk.Label(top_dificil,text=jugador[1],font=mayor_menor_font).grid(row=contador,column=1)
                tk.Label(top_dificil,text=tiempo,font=mayor_menor_font).grid(row=contador,column=2)

                # avanza el contador
                contador += 1

# clase que contiene los botones de los digitos laterales
class Digitos(tk.Frame):

    # guarda el digito actual
    digito = 1
    def __init__(self,master):
        super().__init__(master)

        # Se definen los botones
        self.digito1 = tk.Button(self,text=1,font=font,bg="green",command=lambda: self.cambioBoton(1,self.digito1))
        self.digito2 = tk.Button(self,text=2,font=font,bg="White",command=lambda: self.cambioBoton(2,self.digito2))
        self.digito3 = tk.Button(self,text=3,font=font,bg="White",command=lambda: self.cambioBoton(3,self.digito3))
        self.digito4 = tk.Button(self,text=4,font=font,bg="White",command=lambda: self.cambioBoton(4,self.digito4))
        self.digito5 = tk.Button(self,text=5,font=font,bg="White",command=lambda: self.cambioBoton(5,self.digito5))
        
        # Se colocan los botones
        self.digito1.grid(column=0,row=0)
        self.digito2.grid(column=0,row=1)
        self.digito3.grid(column=0,row=2)
        self.digito4.grid(column=0,row=3)
        self.digito5.grid(column=0,row=4)

    # metodo para cambiar el boton de color e indicar cual es el
    # digito para usar en el panel actualmente
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

# Clase que contiene los botones que administran el juego (excepto los de cargar y guardar juegos)
class Botones(tk.Frame):

    # Registra si el juego no es un juego que se cargo del archivo de guardado
    cargado = False
    def __init__(self,master,panel,reloj,WindowManager):
        super().__init__(master)

        # variables que almacenan los otros objetos que modifican los botones
        self.master = master
        self.panel = panel
        self.reloj = reloj
        self.WindowManager = WindowManager

        # Se colocan los botones:
        self.iniciar = tk.Button(self,text="INICIAR\nJUEGO",bg="red",font=fontbotones,width=9,command=self.iniciarJuego)
        self.iniciar.grid(row=0,column=0)

        tk.Label(self,text="",width=2).grid(row=0,column=1)

        self.jugada = tk.Button(self,text="BORRAR\nJUGADA",bg="#00A5D1",font=fontbotones,width=9,command=self.borrarJugada,state=tk.DISABLED)
        self.jugada.grid(row=0,column=2)

        tk.Label(self,text="",width=2).grid(row=0,column=3)

        self.terminar = tk.Button(self,text="TERMINAR\nJUEGO",bg="green",font=fontbotones,width=9,command=self.terminarJuego,state=tk.DISABLED)
        self.terminar.grid(row=0,column=4)

        tk.Label(self,text="",width=2).grid(row=0,column=5)

        self.borrar = tk.Button(self,text="BORRAR\nJUEGO",bg="#4E82B8",font=fontbotones,width=9,command=self.borrarJuego,state=tk.DISABLED)
        self.borrar.grid(row=0,column=6)

        tk.Label(self,text="",width=2).grid(row=0,column=7)

        tk.Button(self,text="TOP\n10",bg="yellow",font=fontbotones,width=9,command=self.master.abrirTop10).grid(row=0,column=8)

    # metodo encargado de iniciar el juego
    def iniciarJuego(self):

        # restriccion y verificación de inicio
        if self.master.nombre_jugador.get() == "":
            messagebox.showerror("ERROR","POR FAVOR COLOQUE SU NOMBRE ANTES DE EMPEZAR")
            return
        if self.master.revisarNombres(self.master.nombre_jugador.get()):
            messagebox.showerror("ERROR","EL NOMBRE YA EXISTE EN EL TOP10, POR FAVOR ELEGIR OTRO")
            return
        if len(self.master.nombre_jugador.get()) > 20:
            messagebox.showerror("ERROR","EL NOMBRE DEBE SER DE 1 A 20 CARACTERES DE LARGO")
            return

        # Proceso de inicio:
        self.master.en_progreso = True
        self.master.guardar['state'] = tk.NORMAL
        self.master.cargar['state'] = tk.DISABLED
        self.iniciar['state'] = tk.DISABLED
        self.jugada['state'] = tk.NORMAL
        self.terminar['state'] = tk.NORMAL
        self.borrar['state'] = tk.NORMAL
        self.master.nombre_jugadorEntry['state'] = tk.DISABLED
        if self.cargado:
            self.reloj.continuarReloj()
        else:
            self.reloj.iniciarReloj()

    # Metodo para borrar una jugada
    def borrarJugada(self):

        # si el juego esta en proceso hace su funcionalidad
        if self.master.en_progreso:
            
            # Si no hay jugadas se manda un mensaje
            if self.panel.ctrlz == []:
                messagebox.showerror("ERROR","NO HAY MÁS JUGADAS")
                return
            ultima_jugada = self.panel.ctrlz.pop()
            self.panel.cargarNumeros(ultima_jugada,"",False)
    
    # Metodo para terminar el juego
    def terminarJuego(self):
        respuesta = messagebox.askyesno("¿DESEA CONTINUAR?","¿ESTÁ SEGURO DE TERMINAR EL JUEGO?")
        if respuesta:
            self.WindowManager.cerrarJuego()
            self.WindowManager.abrirJuego()
    
    # Metodo para borrar el juego
    def borrarJuego(self):
        respuesta = messagebox.askyesno("¿DESEA CONTINUAR?","¿ESTÁ SEGURO DE BORRAR EL JUEGO?")
        if respuesta:
            config.cargar_juego = True
            self.WindowManager.cerrarJuego()
            self.WindowManager.abrirJuego()

# Metodo que contiene le reloj/timer del juego
class Reloj(tk.Frame):

    # Variables importantes
    activador = True
    tiempo = 0
    cambio_cronometro = False
    def __init__(self,master,WindowManager):
        super().__init__(master)

        self.WindowManager = WindowManager
        
        # coloca todos los elementos en pantalla
        tk.Label(self,text="Tiempo: ",font=fontbotones).grid(row=0,column=0)
        self.horas = tk.Label(self,text="00",font=fontbotones)
        self.horas.grid(row=0,column=1)
        tk.Label(self,text=":",font=fontbotones).grid(row=0,column=2)
        self.minutos = tk.Label(self,text="00",font=fontbotones)
        self.minutos.grid(row=0,column=3)
        tk.Label(self,text=":",font=fontbotones).grid(row=0,column=4)
        self.segundos = tk.Label(self,text="00",font=fontbotones)
        self.segundos.grid(row=0,column=5)

        # Si es timer, coloca el tiempo donde debe empezar
        if config.reloj == 2:
            self.horas['text'] = "{:02d}".format(config.tiempo_reloj[0])
            self.minutos['text'] = "{:02d}".format(config.tiempo_reloj[1])
            self.segundos['text'] = "{:02d}".format(config.tiempo_reloj[2])
    
    # metodo que ejecuta los cambios del reloj o timer
    def cronometroTimer(self):
        self.actualizarReloj()
        # verifica si el timer llego a 0
        if config.reloj == 2 and self.tiempo == 0:
            confirmacion = messagebox.askyesno("TIEMPO EXPIRADO","¿DESEA CONTINUAR EL MISMO JUEGO?")
            if confirmacion:
                self.cambio_cronometro = True
                return self.reiniciarEnCronometro()
            else:
                messagebox.showwarning("¡JUEGO PERDIDO!","SERA DEVUELTO A OTRO JUEGO")
                self.WindowManager.cerrarJuego()
                return self.WindowManager.abrirJuego()

        # cambia el tiempo
        self.tiempo += self.sumando

        # repite el proceso
        if self.activador:
            self.after(1000,lambda:self.cronometroTimer())
    
    # Metodo que se encarga de la inicializacion del reloj
    def iniciarReloj(self):
        self.activador = True
        self.tiempo = 0
        self.sumando = 1
        if config.reloj == 2:
            self.tiempo += 3600*config.tiempo_reloj[0]
            self.tiempo += 60*config.tiempo_reloj[1]
            self.tiempo += config.tiempo_reloj[2]
            self.sumando = -1
        self.cronometroTimer()

    # metodo que reinicia el reloj en modo cronometro desde el punto donde lo dejo el timer
    def reiniciarEnCronometro(self):
        self.tiempo += 3600*config.tiempo_reloj[0]
        self.tiempo += 60*config.tiempo_reloj[1]
        self.tiempo += config.tiempo_reloj[2]
        self.sumando = 1
        self.cronometroTimer()
    
    # metodo para detener el reloj
    def detenerReloj(self):
        self.activador = False
    
    # metodo para reanuar el reloj
    def continuarReloj(self):
        self.activador = True
        self.cronometroTimer()
    
    # metodo para actualizar el reloj
    def actualizarReloj(self):
        horas = self.tiempo//3600
        tiempo = self.tiempo%3600
        minutos = tiempo//60
        segundos = tiempo%60
        self.horas['text'] = "{:02d}".format(horas)
        self.minutos['text'] = "{:02d}".format(minutos)
        self.segundos['text'] = "{:02d}".format(segundos)

# Clase que contiene todo el juego
class Juego(tk.Frame):
    en_progreso = False
    def __init__(self,master,manager):
        super().__init__(master)

        # Comprueba donde debe ir el panel de digitos
        if config.posicion == 0:
            x_digitos = 1250
            y_digitos = 180
        elif config.posicion == 1:
            x_digitos = 510
            y_digitos = 180
        
        # Hace que la fila 0 y colimna 0 se pueda expandir hasta donde le permitan
        self.rowconfigure(0,weight=1)
        self.columnconfigure(0,weight=1)

        self.WindowManager = manager
        
        # Panel de digitos
        self.digitos = Digitos(self)
        self.digitos.place(x=x_digitos,y=y_digitos)

        # Reloj
        self.reloj = Reloj(self,self.WindowManager)
        self.mostarReloj()

        # Panel prinipal del juego
        self.panel = Panel(self,self.digitos,manager,self.reloj)
        self.panel.place(x=590,y=100)

        # Se llama al metodo de cargar partida
        self.panel.cargarPartida()

        # Panel de botones
        self.botones = Botones(self,self.panel,self.reloj,manager)
        self.botones.place(x=425,y=875)  

        # Variable del nombre del jugador
        self.nombre_jugador = tk.StringVar()

        # Caja de texto para colocar le nombre
        self.nombre_jugadorEntry = tk.Entry(self,textvariable=self.nombre_jugador,width=26,font=fontbotones)
        self.nombre_jugadorEntry.place(x=840,y=50)

        # etiqueta para indicar que la caja pertenece al nombre del jugador
        tk.Label(self,text="Nombre del jugador:",font=fontbotones).place(x=590,y=50)

        # Etiqueta que muestra la dificultad del futoshiki
        self.nivel = tk.Label(self,text="",font=fontbotones)
        
        # Metodo para mostrar la dificultad actual
        self.mostrarNivel()

        # boton para guardar el juego
        self.guardar = tk.Button(self,text="GUARDAR JUEGO",font=("times",14),width=15,state=tk.DISABLED,command=self.guardarJuego)
        self.guardar.place(x=1450,y=875)

        # boton para cargar el juego
        self.cargar = tk.Button(self,text="CARGAR JUEGO",font=("times",14),width=15,command=self.cargarJuego)
        self.cargar.place(x=1450,y=950)
    
    # metodo para revisar si el nombre ya existe en el top10
    def revisarNombres(self,nombre):
        for dificultad in config.top10:
            for jugador in dificultad:
                if jugador[1] == nombre:
                    return True
        return False

    # Metodo para abrir la ventana del top10
    def abrirTop10(self):
        if self.en_progreso == True:
            self.reloj.detenerReloj()
        self.top10 = Top10(self)
        self.top10.grid(row=0,column=0,sticky="nswe")
        
    # Metodo para cerrar la ventana del top10
    def cerrarTop10(self):
        if self.en_progreso == True:
            self.reloj.continuarReloj()
        self.top10.destroy()

    # Metodo para mostrar el reloj en la interfaz
    def mostarReloj(self):
        if config.reloj != 1:
            self.reloj.place(x=90,y=915)

    # Metodo para mostrar el nivel actual
    def mostrarNivel(self):
        self.nivel.destroy()

        if config.dificultad_actual == 0:
            nivel = "FÁCIL"
            x_nivel = 815
        elif config.dificultad_actual == 1:
            nivel = "INTERMEDIO"
            x_nivel = 750
        elif config.dificultad_actual == 2:
            nivel = "DIFÍCIL"
            x_nivel = 815
        
        self.nivel = tk.Label(self,text="NIVEL "+nivel,font=fontbotones)
        self.nivel.place(x=x_nivel,y=0)

    # metodo que crea una matriz con los contenidos de texto y estado de la matriz de botones
    def matrizBotones(self):
        matriz_final = []
        for fila in self.panel.matriz_botones_filas:
            fila_temporal = []
            for boton in fila:
                tupla = (boton["text"],)
                tupla += (boton["state"],)
                fila_temporal.append(tupla)
            matriz_final.append(fila_temporal)
        return matriz_final
    
    # metodo que crea una matriz con los contenidos de texto de la matriz de mayores y menores que
    def matrizMayoresMenores(self,matriz):
        matriz_final = []
        for fila in matriz:
            fila_temporal = []
            for label in fila:
                fila_temporal.append(label["text"])
            matriz_final.append(fila_temporal)
        return matriz_final

    # Metodo que guarda el juego con pickle
    def guardarJuego(self):
        self.reloj.detenerReloj()
        archivo_juego = open("futoshiki2021juegoactual.dat","wb")
        pickle.dump(self.matrizBotones(),archivo_juego)
        pickle.dump(self.matrizMayoresMenores(self.panel.matriz_laterales),archivo_juego)
        pickle.dump(self.matrizMayoresMenores(self.panel.matriz_superior),archivo_juego)
        pickle.dump(config.dificultad_actual,archivo_juego)
        pickle.dump(config.juego_actual,archivo_juego)
        pickle.dump(config.reloj,archivo_juego)
        pickle.dump(self.reloj.tiempo,archivo_juego)
        pickle.dump(self.reloj.sumando,archivo_juego)
        pickle.dump(self.reloj.cambio_cronometro,archivo_juego)
        pickle.dump(self.nombre_jugador.get(),archivo_juego)
        pickle.dump(self.panel.ctrlz,archivo_juego)
        archivo_juego.close()
        messagebox.showinfo("OPERACIÓN EXITOSA","SU JUEGO SE HA GUARDADO, SERA PRESENTADO CON UNO NUEVO")
        self.WindowManager.cerrarJuego()
        self.WindowManager.abrirJuego()

    # metodo que carga el juego
    def cargarJuego(self):
        try:
            archivo_juego = open("futoshiki2021juegoactual.dat","rb")
        except FileNotFoundError:
            messagebox.showerror("ERROR","NO EXISTE NINGUNA PARTIDA GUARDADA CON ANTERIORIDAD")
            return
        matriz_botones_filas = pickle.load(archivo_juego)
        matriz_laterales = pickle.load(archivo_juego)
        matriz_superior = pickle.load(archivo_juego)
        dificultad = pickle.load(archivo_juego)
        juego = pickle.load(archivo_juego)
        reloj = pickle.load(archivo_juego)
        reloj_tiempo = pickle.load(archivo_juego)
        reloj_sumando = pickle.load(archivo_juego)
        reloj_cambio_cronometro = pickle.load(archivo_juego)
        nombre_jugador = pickle.load(archivo_juego)
        self.panel.ctrlz = pickle.load(archivo_juego)
        archivo_juego.close()

        if self.revisarNombres(nombre_jugador):
            messagebox.showerror("ERROR","EL NOMBRE DE ESTA PARTIDA YA EXISTE EN EL TOP POR ENDE NO PUEDE CARGARSE")
            return

        for fila in range(5):
            for columna in range(5):
                self.panel.matriz_botones_filas[fila][columna]['state'] = matriz_botones_filas[fila][columna][1]
                self.panel.matriz_botones_filas[fila][columna]['text'] = matriz_botones_filas[fila][columna][0]
        
        for fila in range(5):
            for columna in range(4):
                self.panel.matriz_laterales[fila][columna]['text'] = matriz_laterales[fila][columna]
        
        for fila in range(4):
            for columna in range(5):
                self.panel.matriz_superior[fila][columna]['text'] = matriz_superior[fila][columna]
        config.dificultad_actual = dificultad
        config.juego_actual = juego
        if config.reloj != reloj:
            mensaje = "SE HA CARGADO SU JUEGO, PRESIONE 'INICIAR JUEGO' PARA CONTINUARLO. \
            \nADICIONALMENTE SE CAMBIO LA CONFIGURACIÓN DE RELOJ PARA PARIDAD CON ESTA PARTIDA"
        else:
            mensaje = "SE HA CARGADO SU JUEGO, PRESIONE 'INICIAR JUEGO' PARA CONTINUARLO"
        config.reloj = reloj
        self.mostarReloj()
        self.reloj.tiempo = reloj_tiempo
        self.reloj.sumando = reloj_sumando
        self.reloj.cambio_cronometro = reloj_cambio_cronometro
        self.nombre_jugador.set(nombre_jugador)
        self.nombre_jugadorEntry['state'] = tk.DISABLED
        self.mostrarNivel()
        self.reloj.actualizarReloj()
        messagebox.showinfo("OPERACIÓN EXITOSA",mensaje)
        self.botones.cargado = True
                
################################################## Funciones ################################################

############################################### Programa principal ##########################################

# Letras y tamaños
font = ("papyrus",32)
fontbotones = ("papyrus",20)
mayor_menor_font = ("Times",24)

# Instrucciones para cargar las partidas precreadas del juego
archivo_partidas = open("futoshiki2021partidas.dat","rb")
partidas = pickle.load(archivo_partidas)
archivo_partidas.close()