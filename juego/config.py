################################################## Imports ##################################################
import pickle

################################################### Clases ##################################################
# Clase que mantendra los datos de la configuración
class Configuracion():

    # Facil = 0, Intermedio = 1, Dificil = 2
    dificultad = 0

    # Si = 0, No = 1, Timer = 2
    reloj = 0
    
    # Horas = Indice 0, Minutos = Indice 1, Segundos = indice 2
    tiempo_reloj = (0,30,0)

    # Derecha = 0, Izquierda = 1
    posicion = 0

    # variables que guardan el ultimo juego jugado
    juego_actual = 0

    dificultad_actual = 0

    cargar_juego = False

    top10 = [[],[],[]]
    
############################################### Programa principal ##########################################
config = Configuracion()
try:
    archivo_top = open("futoshiki2021top10.dat","rb")
    config.top10 = pickle.load(archivo_top)
    archivo_top.close()

    
except:
    pass
try:
    archivo_configuracion = open("futoshiki2021configuración.dat","rb")
    config.dificultad = pickle.load(archivo_configuracion)
    config.reloj = pickle.load(archivo_configuracion)
    config.tiempo_reloj = pickle.load(archivo_configuracion)
    config.posicion = pickle.load(archivo_configuracion)
    archivo_configuracion.close
except:
    pass