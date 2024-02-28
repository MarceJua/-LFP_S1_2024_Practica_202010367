
import os

diccionarioDatos = dict()
listaDatos = []

class Gato:
    def __init__(self, nombre, energia):
        self.nombre = nombre
        self.energia = energia

    def correr(self, metros):
        self.energia -= metros / 2

    def comer(self, peso_ratón):
        self.energia += 12 + peso_ratón

    def jugar(self, minutos):
        self.energia -= minutos

def cargarArchivo():
    print("Cargando archivo...")
    # Solicitar al usuario la ruta del archivo
    ruta = input("Ingrese la ruta del archivo .petmanager: ")

    while True:
        nombre, extension = os.path.splitext(ruta)
        if extension == ".petmanager":
            print("\nArchivo válido\n")
            break
        else:
            print("\nArchivo inválido\n")
            ruta = input("\nIngrese la ruta del archivo .petmanager: ")

    gatos = {}  # Diccionario para almacenar los gatos creados

    try:
        with open(ruta, "r") as archivo:
            for linea in archivo:
                
                elementos = linea.strip().split(": ")
                if len(elementos) == 2:
                    comando, parametros = elementos
                    parametros = parametros.split(", ")

                    if comando == "Crear_Gato" and len(parametros) == 2:
                        nombre_gato = parametros[0]
                        energia_inicial = int(parametros[1])
                        gatos[nombre_gato] = Gato(nombre_gato, energia_inicial)
                    elif comando in ["Correr", "Comer", "Jugar"] and len(parametros) == 2:
                        nombre_gato = parametros[0]
                        if nombre_gato in gatos:
                            gato = gatos[nombre_gato]
                            if comando == "Correr":
                                gato.correr(int(parametros[1]))
                            elif comando == "Comer":
                                gato.comer(int(parametros[1]))
                            elif comando == "Jugar":
                                gato.jugar(int(parametros[1]))
                    else:
                        print(f"Error en la línea: {linea.strip()}")

        # Imprimir estado de los gatos después de procesar los comandos
        for nombre, gato in gatos.items():
            print(f"Estado de {nombre}: Energía = {gato.energia}")

    except FileNotFoundError:
        print(f"No se pudo encontrar el archivo {ruta}")
    except Exception as e:
        print(f"Ocurrió un error al procesar el archivo: {e}")


def modulPet(): #módulo petmanager
    # Limpiar la pantalla
    os.system('cls' if os.name == 'nt' else 'clear')

    print("--- Módulo PetManager ---")
    print("1. Cargar Archivo")
    print("2. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        cargarArchivo()
    elif opcion == "2":
        menu()
    else:
        print("Opción incorrecta")

    # Puedes implementar más lógica según las opciones seleccionadas

def salir():
    print("Gracias por usar el programa")
    input("Presione una tecla para continuar...") 


def menu():
    print("| LENGUAJES FORMALES Y DE PROGRAMACION |")
    print("| SECCION: B+                          |")
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

menu()

