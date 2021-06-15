################################################## Imports ##################################################
import tkinter as tk

################################################### Clases ##################################################


################################################## Funciones ################################################


############################################### Programa principal ##########################################
ventana = tk.Tk() # Crea ventana principal

# Hace que los contenidos de la ventana se expandan con la ventana
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
tk.Button(menu,text="JUGAR",font=("Papyrus"),width=10,height=1).grid(row=2,column=0)
tk.Button(menu,text="Configurar",font=("Papyrus"),width=10,height=1).grid(row=3,column=0)
tk.Button(menu,text="Ayuda",font=("Papyrus"),width=10,height=1).grid(row=4,column=0)
tk.Button(menu,text="Acerca de",font=("Papyrus"),width=10,height=1).grid(row=5,column=0)

ventana.mainloop() # Loop de ventana para eventos
