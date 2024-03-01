from gato import Gato
import datetime
import os
from graphviz import Digraph

def modulPet(): #módulo petmanager
    # Limpiar la pantalla
    os.system('cls' if os.name == 'nt' else 'clear')

    print("--- Módulo PetManager ---")
    print("1. Cargar Archivo")
    print("2. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        leerArchivoPetManager()
    elif opcion == "2":
        menu()
    else:
        print("Opción incorrecta")

def salir():
    print("Gracias por usar el programa")
    input("Presione una tecla para continuar...") 

def menu():
    print("| LENGUAJES FORMALES Y DE PROGRAMACION |")
    print("| SECCION: B-                          |")
    print("| CARNET:20201367                      |")

    input("Presione Enter para continuar...")

    while True:
        print("\n--- Menú Principal ---")
        print("1. Módulo PetManager")
        print("2. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            modulPet()
        elif opcion == "2":
            salir()
            break
        else:
            print("Opción incorrecta")

def procesarComandosPetManager(comandos):
    gatos = {}  # Diccionario para almacenar los gatos creados


    with open("resultado.petworld_result", "w") as archivo_salida:
        for comando in comandos:
            partes = comando.split(':')
            if partes[0] == "Crear_Gato":
                nombre_gato = partes[1]
                gatos[nombre_gato] = Gato(nombre_gato)  # Crear un nuevo gato y almacenarlo en el diccionario
                mensaje = f"[{datetime.datetime.now()}] Se creó el gato {nombre_gato}\n"
                print(mensaje)
                archivo_salida.write(mensaje)
                
            elif partes[0] == "Dar_de_Comer":
                nombre_gato = partes[1].split(',')[0]  # Obtener el nombre del gato
                if nombre_gato in gatos:  # Verificar si el gato existe en el diccionario
                    gato = gatos[nombre_gato]
                    if gato.vivo:
                        peso_ratón = int(partes[1].split(',')[1])
                        gato.comer(peso_ratón)
                        mensaje = f"[{datetime.datetime.now()}] {nombre_gato}, Gracias por alimentarme. Ahora mi energía es {gato.energia}.\n"
                        print(mensaje)
                        archivo_salida.write(mensaje)
                    else:
                        mensaje = f"[{datetime.datetime.now()}] Muy tarde. Ya me morí.\n"
                        print(mensaje)
                        archivo_salida.write(mensaje)
                else:
                    mensaje = f"[{datetime.datetime.now()}] Gato no encontrado: {nombre_gato}\n"
                    print(mensaje)
                    archivo_salida.write(mensaje)

            elif partes[0] == "Jugar":
                nombre_gato = partes[1].split(',')[0]  # Obtener el nombre del gato
                if nombre_gato in gatos:  # Verificar si el gato existe en el diccionario
                    gato = gatos[nombre_gato]
                    if gato.vivo:
                        tiempo_juego = int(partes[1].split(',')[1])
                        gato.jugar(tiempo_juego)
                        mensaje = f"[{datetime.datetime.now()}] {nombre_gato}, Gracias por jugar conmigo. Ahora mi energía es {gato.energia}.\n"
                        print(mensaje)
                        archivo_salida.write(mensaje)
                    else:
                        mensaje = f"[{datetime.datetime.now()}] Ya me morí.\n"
                        print(mensaje)
                        archivo_salida.write(mensaje)
                else:
                    mensaje = f"[{datetime.datetime.now()}] Gato no encontrado: {nombre_gato}\n"
                    print(mensaje)
                    archivo_salida.write(mensaje)

            elif partes[0] == "Resumen_Mascota":
                nombre_gato = partes[1]
                if nombre_gato in gatos:  # Verificar si el gato existe en el diccionario
                    gato = gatos[nombre_gato]
                    mensaje = f"[{datetime.datetime.now()}] {nombre_gato}, Energía: {gato.energia}, Tipo: Gato, Estado: {'Vivo' if gato.vivo else 'Muerto'}\n"
                    print(mensaje)
                    archivo_salida.write(mensaje)
                    # Generar el gráfico con la información del gato
                    generar_grafico(nombre_gato, gato.energia, 'Vivo' if gato.vivo else 'Muerto')
                else:
                    mensaje = f"[{datetime.datetime.now()}] Gato no encontrado: {nombre_gato}\n"
                    print(mensaje)
                    archivo_salida.write(mensaje)

            elif partes[0] == "Resumen_Global":
                archivo_salida.write(f"[{datetime.datetime.now()}] {'-'*30} Resumen Global {'-'*30}\n")
                for nombre_gato, gato in gatos.items():
                    mensaje = f"[{datetime.datetime.now()}] {nombre_gato}, Energía: {gato.energia}, Tipo: Gato, Estado: {'Vivo' if gato.vivo else 'Muerto'}\n"
                    print(mensaje)
                    archivo_salida.write(mensaje)
                if not gatos:  # Verificar si no hay gatos
                    mensaje = f"[{datetime.datetime.now()}] No hay gatos para resumir.\n"
                    print(mensaje)
                    archivo_salida.write(mensaje)
                archivo_salida.write(f"[{datetime.datetime.now()}] {'-'*70}\n")

            else:
                mensaje = f"[{datetime.datetime.now()}] Comando desconocido: {partes[0]}\n"
                print(mensaje)
                archivo_salida.write(mensaje)
            
def leerArchivoPetManager():
    print("\nHa seleccionado cargar archivo .petmanager\n")
    ruta = input("Ingrese la ruta del archivo: ")

    while True:
        nombre, extension = os.path.splitext(ruta)
        if extension == ".petmanager":
            print("\nArchivo válido\n")
            break
        else:
            print("\nArchivo inválido\n")
            ruta = input("\nIngrese la ruta del archivo: ")

    with open(ruta, "r") as archivo:
        comandos_petmanager = [linea.strip() for linea in archivo]

    #procesar_comandos(comandos_petmanager)
    procesarComandosPetManager(comandos_petmanager)

# Función para generar el gráfico
def generar_grafico(nombre_gato, energia, estado):
    # Crear un objeto Digraph
    dot = Digraph()

    # Agregar el nodo principal (nombre del gato)
    dot.node(nombre_gato, label=nombre_gato)

    # Agregar nodos secundarios (energía y estado)
    dot.node('energia', label=f'Energía: {energia}')
    dot.node('tipo', label=f'Tipo: Gato')
    dot.node('estado', label=f'Estado: {estado}')

    # Agregar bordes desde el nodo principal a los nodos secundarios
    dot.edge(nombre_gato, 'energia')
    dot.edge(nombre_gato, 'tipo')
    dot.edge(nombre_gato, 'estado')

    # Renderizar y guardar el gráfico como un archivo PNG con un nombre único
    nombre_archivo = f'grafico_{nombre_gato}'
    dot.render(nombre_archivo, format='png', cleanup=True)

menu()

