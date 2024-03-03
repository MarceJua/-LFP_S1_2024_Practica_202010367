import datetime
from graphviz import Digraph

diccionarioDatos = dict()
listaDatos = []
lista_gatos = []  # Lista para almacenar los gatos creados
gatos = {}

class Gato:
    def __init__(self, nombre):
        self.nombre = nombre
        self.energia = 50
        self.vivo = True
        lista_gatos.append(self)  # Añadir el gato a la lista de gatos creados

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

    def resumen_global(cls):
        for gato in lista_gatos:
            gato.resumen()  # Llama al método resumen de cada gato