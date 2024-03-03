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
## Propósito

### Nombre del Software: PetManager
### Número de versión/release: Versión 1.0

El propósito de este documento es proporcionar una visión general completa del Sistema de Gestión de Mascotas, conocido como PetManager. Cubre todos los aspectos relevantes relacionados con los requerimientos de software, las funcionalidades y las características planificadas del sistema. El objetivo principal de PetManager es satisfacer las necesidades de los usuarios en la gestión y el cuidado de sus mascotas.

## Alcance del producto/ Software
El sistema de gestión de mascotas, denominado PetManager, es una aplicación diseñada para facilitar la administración y el cuidado de mascotas. El objetivo principal es ofrecer una solución integral que permita a los usuarios llevar un registro detallado de sus gatos, así como proporcionar herramientas para interactuar con ellos de manera adecuada y monitorear su estado de salud y bienestar.

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

## Requerimientos de interfaces externas  
A continuación, se describirá las funcionalidades con las cuales cuenta el 
proyecto, estas incluyen una imagen del programa y una descripción breve 
de como esta funciona.
* Carátula
    * se contienen datos acerca del programa, se debe Presionar Enter para ingresar al menú principal
![caratula](https://i.ibb.co/6bHNQjQ/caratula.png)

* Menú Principal
    * se le solocitará al usuario ingresar el número de la opción a ejecutar, siendo 1 para ir a Módulo PetManager o 2 para Salir.
![MenPri](https://i.ibb.co/MCHwSNY/MenPri.png)

* Módulo Petmanager
    * se le solocitará al usuario ingresar el número de la opción a ejecutar, siendo 1 para Cargar Archivo o 2 para Salir.
![ModPet](https://i.ibb.co/rQd5JYF/ModPet.png)

* Cargar Archivo
    * se le solicitara al usuario ingresar la ruta del archivo .petmanager para poder ejecutar los comandos, crear e intaruactuar con los gatos y crear el archivo de salida (.petworld_result) y las gráficas de los gatos.
    En caso no sea un archivo .petmanager se le indicara al usuario que ingrese un archivo válido.
![CargArch](https://i.ibb.co/8br5MBx/CargArch.png)

## Requerimientos no funcionales
* Rendimiento:
    * El sistema debe ser capaz de manejar grandes volúmenes de datos de manera eficiente, garantizando tiempos de respuesta rápidos incluso en situaciones de carga máxima.
    * La generación de gráficos y reportes debe ser rápida y no debe afectar significativamente el rendimiento general del sistema.

* Usabilidad:
    * La interfaz de usuario debe ser intuitiva y fácil de usar para propietarios de mascotas de cualquier nivel de experiencia.
    * El sistema debe ser accesible desde múltiples dispositivos y plataformas, incluyendo computadoras de escritorio, dispositivos móviles y tabletas.