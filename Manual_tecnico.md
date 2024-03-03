# LABORATORIO LENGUAJES FORMALES Y DE PROGRAMACION
## PetWorld Manager 
### Primer Semestre 2024
```js
Universidad San Carlos de Guatemala
Programador: Marcelo André juarez Alfaro
Carne: 202010367
Correo: mjuarez2017ig@gmail.com
```
---
## Descripción del Proyecto
El proyecto de PetManager es un sistema de gestión de mascotas diseñado para administrar y cuidar gatos virtuales. El sistema permite a los usuarios crear, interactuar y controlar las actividades de sus gatos virtuales a través de comandos definidos en un archivo de texto.

Los gatos virtuales pueden realizar una serie de acciones, como correr, comer y jugar, cada una de las cuales afecta su nivel de energía. El sistema registra estas interacciones y proporciona retroalimentación al usuario sobre el estado y las actividades de sus mascotas.

## Objetivos
* Objetivo General
    * Desarrollar un sistema de gestión de mascotas (PetManager) que permita a los usuarios interactuar con gatos virtuales mediante comandos definidos en un archivo de texto, proporcionando una experiencia de cuidado de mascotas virtual.
* Objetivos Específicos
    * Diseñar e implementar un mecanismo de lectura y procesamiento de comandos desde un archivo de texto, permitiendo a los usuarios crear, interactuar y controlar las actividades de sus gatos virtuales de manera eficiente.
    * Realizar pruebas exhaustivas para cada módulo y para el sistema en su 
    conjunto.
    * Desarrollar un mecanismo de lectura de archivos

## Funcionalidades del Programa
El programa PetManager ofrece una variedad de funcionalidades diseñadas para la gestión y el cuidado de gatos virtuales. Estas funcionalidades incluyen:

* Interacción mediante Comandos:
    * Los usuarios pueden interactuar con los gatos virtuales a través de comandos definidos en un archivo de texto.
    * Los comandos permiten a los usuarios realizar acciones específicas, como alimentar, jugar y obtener información sobre sus gatos virtuales.

* Creación de Gatos Virtuales:
    * Permite a los usuarios crear gatos virtuales proporcionando un nombre único para cada gato.

* Alimentación de Gatos:
    * Permite a los usuarios alimentar a los gatos virtuales proporcionándoles comida en forma de ratones virtuales.
    * El gato aumenta su energía después de comer, pero si su energía cae a cero, el gato muere.

* Realización de Actividades Físicas:
    * Los gatos virtuales pueden correr, lo que afecta su energía dependiendo de la distancia recorrida.

* Generación de Informes:
    * Proporciona informes detallados sobre el estado y las actividades de cada gato virtual.
    * Los informes incluyen detalles sobre la energía actual del gato, su estado vital (vivo o muerto) y su historial de actividades.

* Resúmenes Globales:
    * Ofrece resúmenes globales que muestran el estado general de todos los gatos virtuales creados por el usuario.

* Generación de Gráficos Visuales:
    * Utiliza la biblioteca Graphviz para generar gráficos visuales que representan el estado y las actividades de cada gato virtual.

## Entorno Operativo
El sistema se desarrollará para funcionar en computadoras de escritorio 
convencionales.

Se requiere un hardware típico de oficina, que incluye una CPU con al menos 
un procesador de doble núcleo, 8 GB de RAM y 10 GB de espacio de disco 
duro para el almacenamiento de datos y el software del sistema.

El sistema de desarrollará principalmente para funcionar con sistemas 
operativos Windows (10/11).

Se utilizará el lenguaje de programación de Python en todo el proyecto.

Se utilizará entorno de desarrollo integrado (IDE) Visual studio code.

Se utilizó herramientas adicionales de desarrollo, como Git para el control de 
versiones

## Requerimientos funcionales
A continuación, se describirá las funcionalidades con las cuales cuenta el 
proyecto, estas incluyen una imagen del código y una descripción breve 
de como esta funciona.
* Clase gato
![clase-gato](https://i.ibb.co/pwkVFFj/clase-gato.png)
    * Permite la creación y gestión de gatos virtuales en el sistema. Los gatos virtuales tienen la capacidad de correr, comer, jugar, y proporcionar un resumen de su estado.

        * Constructor:
            * La clase Gato tiene un constructor __init__ que recibe el nombre del gato como parámetro. Inicializa los atributos del gato, incluyendo su nombre, energía y estado (vivo).
            * El gato se agrega a la lista de gatos creados.

        * Correr:
            * El método correr(metros) permite que el gato virtual corra una cierta distancia en metros. La energía del gato disminuye en la mitad de los metros recorridos.
            * Si la energía del gato llega a cero o menos, el gato muere.

        * Comer:
            * El método comer(peso_ratón) permite que el gato virtual coma un ratón. Aumenta la energía del gato en una cantidad determinada según la fórmula proporcionada.
            * Si el gato está muerto, no puede comer.

        * Jugar:
            * El método jugar(tiempo_minutos) simula que el gato virtual juega durante un tiempo especificado en minutos. La energía del gato disminuye con el tiempo de juego.
            * Si la energía del gato llega a cero o menos, el gato muere.

        * Resumen:
            * El método resumen() proporciona un resumen del estado actual del gato, incluyendo su nombre, energía, tipo (Gato) y estado (vivo o muerto).

        * Resumen Global:
            * El método de clase resumen_global(cls) recorre la lista de todos los gatos creados y genera un resumen del estado de cada gato.

* Función menú()
    *  proporciona un menú interactivo para que el usuario seleccione diferentes opciones entre ingresar al modulo PetManager o salir del programa.
![defMenu](https://i.ibb.co/mBKnTHG/defMenu.png)

* Función modulPet()
    * proporciona un menú interactivo para que el usuario seleccione diferentes opciones entre cargar archivo de entrada o salir del programa.
![def-Modul-Pet](https://i.ibb.co/wYbpNY7/def-Modul-Pet.png)

* Función leerArchivoPetManager()
    * permite al usuario cargar un archivo con extensión ".petmanager" que contiene comandos para manipular las mascotas en el programa.
![def-Leer-Arch](https://i.ibb.co/syrjs4V/def-Leer-Arch.png)

* Función procesarComandosPetManager(comandos)
    * se encarga de interpretar y ejecutar los comandos proporcionados por el usuario en el módulo PetManager del programa. Estos comandos están diseñados para crear, alimentar, jugar y obtener resúmenes de las mascotas dentro del sistema.
    * Por medio de un diccionario y abre un archivo de salida en modo escritura.
    * Empieza con la generación de la gráfica
![def-Procesar-Comand](https://i.ibb.co/JzVMWTG/def-Procesar-Comand.png)

* Función generar_grafico(nombre_gato, energia, estado)
    * se encarga de crear un gráfico representativo de la información de un gato específico, incluyendo su nombre, energía y estado (vivo o muerto). Este gráfico se genera utilizando la biblioteca Graphviz y se guarda como un archivo PNG con un nombre único.
![def-Gener-Func](https://i.ibb.co/JdWMY32/def-Gener-Func.png)

## Requerimientos no funcionales
* Rendimiento:
    * El sistema debe ser capaz de manejar grandes volúmenes de datos de manera eficiente, garantizando tiempos de respuesta rápidos incluso en situaciones de carga máxima.
    * La generación de gráficos y reportes debe ser rápida y no debe afectar significativamente el rendimiento general del sistema.

* Usabilidad:
    * La interfaz de usuario debe ser intuitiva y fácil de usar para propietarios de mascotas de cualquier nivel de experiencia.
    * El sistema debe ser accesible desde múltiples dispositivos y plataformas, incluyendo computadoras de escritorio, dispositivos móviles y tabletas.