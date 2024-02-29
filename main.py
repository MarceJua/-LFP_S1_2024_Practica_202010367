
import datetime
import os

diccionarioDatos = dict()
listaDatos = []

class Gato:
    def __init__(self, nombre):
        self.nombre = nombre
        self.energia = 50  # Energía inicial del gato
        self.vivo = True

    def correr(self, metros):
        if self.vivo:
            self.energia -= metros / 2
            if self.energia <= 0:
                self.vivo = False
                print(f"[{datetime.datetime.now()}] {self.nombre}, Me he quedado sin energía y me morí.")
        else:
            print(f"[{datetime.datetime.now()}] {self.nombre}, Ya me morí.")

    def comer(self, peso_ratón):
        if self.vivo:
            self.energia += 12 + peso_ratón
            print(f"[{datetime.datetime.now()}] {self.nombre}, Gracias por alimentarme. Ahora mi energía es {self.energia}.")
        else:
            print(f"[{datetime.datetime.now()}] {self.nombre}, Muy tarde. Ya me morí.")

    def jugar(self, tiempo_minutos):
        if self.vivo:
            self.energia -= tiempo_minutos * 0.1
            if self.energia <= 0:
                self.vivo = False
                print(f"[{datetime.datetime.now()}] {self.nombre}, Me cansé demasiado y me morí.")
            else:
                print(f"[{datetime.datetime.now()}] {self.nombre}, Gracias por jugar conmigo. Ahora mi energía es {self.energia}.")
        else:
            print(f"[{datetime.datetime.now()}] {self.nombre}, Ya me morí.")

    def resumen(self):
        estado = "Vivo" if self.vivo else "Muerto"
        print(f"[{datetime.datetime.now()}] {self.nombre}, Energía: {self.energia}, Tipo: Gato, Estado: {estado}")

"""
# Ejemplo de uso
gato = Gato("Garfield")

# Crear gato
gato.resumen()

# Dar de comer al gato
gato.comer(100)

# Jugar con el gato
gato.jugar(30)

# Correr con el gato
gato.correr(20)

# Resumen del gato
gato.resumen()
"""


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

def procesarComandosPetManager(comandos):
    gato = None  # Creamos una instancia de Gato fuera del bucle para que sea accesible en todo momento

    for comando in comandos:
        partes = comando.split(':')

        if partes[0] == "Crear_Gato":
            nombre_gato = partes[1]
            gato = Gato(nombre_gato)
            print(f"[{datetime.datetime.now()}] Se creó el gato {nombre_gato}")

        elif partes[0] == "Dar_de_Comer":
            if gato is not None:
                if gato.vivo:
                    # Dividir la cadena en nombre del gato y peso del ratón
                    nombre_gato, peso_ratón = partes[1].split(',')
                    peso_ratón = int(peso_ratón)  # Convertir peso_ratón a entero
                    gato.comer(peso_ratón)
                else:
                    print(f"[{datetime.datetime.now()}] Muy tarde. Ya me morí.")

        elif partes[0] == "Jugar":
            if gato is not None:
                if gato.vivo:
                    # Dividir la cadena en nombre del gato y tiempo de juego
                    nombre_gato, tiempo_juego = partes[1].split(',')
                    tiempo_juego = int(tiempo_juego)  # Convertir tiempo_juego a entero
                    gato.jugar(tiempo_juego)
                else:
                    print(f"[{datetime.datetime.now()}] Ya me morí.")

        elif partes[0] == "Resumen_Mascota":
            if gato is not None:
                gato.resumen()

        elif partes[0] == "Resumen_Global":
            if gato is not None:
                gato.resumen()
            else:
                print("[{}] No hay gato para resumir.".format(datetime.datetime.now()))

        else:
            print(f"[{datetime.datetime.now()}] Comando desconocido: {partes[0]}")

            
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

    procesarComandosPetManager(comandos_petmanager)

menu()

