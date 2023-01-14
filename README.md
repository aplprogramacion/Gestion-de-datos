# feedbacks-universivad
programa para gestionar datos de clientes
Ejercicio Feedback
Escribir un programa que permita gestionar los datos de clientes de una empresa. Los clientes se guardarán en un diccionario en el que la clave de cada cliente será su NIF.
El valor asociado a cada cliente será otro diccionario o una lista, con los datos del cliente (apellidos y nombre, dirección, teléfono, correo electrónico, cliente habitual, fecha de la operación), donde “cliente habitual” tendrá el valor True si se trata de un cliente no esporádico. Se valorará que se realicen dos versiones: con campo de valor diccionario y lista.
El carácter de cliente habitual lo introducirá el empleado de la empresa que utilizar el programa (si/no). La fecha se introducirá entre comillas en la forma: ‘12/01/2020’.
El programa debe preguntar al usuario por una opción del siguiente menú: 
(1) Añadir cliente. 
(2) Eliminar cliente.
(3) Mostrar cliente. 
(4) Listar todos los clientes. 
(5) Listar clientes habituales. 
(6) Salir. 
En función de la opción elegida el programa tendrá que hacer lo siguiente:
Preguntar los datos del cliente, crear un diccionario (o lista) con los datos y añadirlo al contenido del campo valor del cliente.
Preguntar por el NIF del cliente y eliminar sus datos de la variable que contiene los datos.
Preguntar por el NIF del cliente y mostrar todos sus datos.
Mostrar lista de todos los clientes de la base datos con su NIF y nombre.
Mostrar la lista de clientes habituales de la base de datos con su NIF y nombre.
Terminar la ejecución del programa.
En su resolución se deberá programar el menú de forma que cada opción se realice implementando una función. Caso de introducir una opción fuera del rango de 1 a 6, no debe terminar el programa, sino que debe advertirlo para que se vuelva a seleccionar otro punto del menú. El programa sólo terminará cuando se seleccione la opción 6. Se comprobará que el NIF contiene 9 caracteres, los 8 primeros numéricos. A su vez, el teléfono debe contener 9 dígitos. También se puede comprobar la fecha. Estas comprobaciones no se deben gestionar mediante excepciones.
