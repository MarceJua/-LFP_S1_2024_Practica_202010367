
import os

def cargarArchivo():
    print("Cargando archivo...")

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