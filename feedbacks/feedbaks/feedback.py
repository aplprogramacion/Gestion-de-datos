import os
import sys
script_dir = "../funciones"  #variable donde le diremos el directorio que queremos
sys.path.append(os.path.abspath(script_dir)) #metodo ruta absoluta
import validarDni, validarTlf, emailValido, validarfecha, clientehabitual #importamos funciones
clients = {}
client = {}
def crear_cliente():
    #dni
    while True:
        dni = input("introduce tu dni: ")  # definimos la variable que pedira datos al usuario
        if validarDni.dniValido(dni): #dentro de validarDni llamamos a la funcion dniValido() para comprobar el dni
            break #si el dni es True saldra del bucle
    #nombre
    nombre = input("escribe tu nombre: ")
    #apellidos
    apellidos = input("escribe tus apellidos: ")
    #direccion
    direccion = input("escribe tu direccion: ")
    #telefono
    while True:
        tlf = input("escribe tu tlf: ")
        if validarTlf.tlfValido(tlf):
            break
    #email
    while True:
        email = input("introduce tu direccion email, solo validos @hotmail,@gmail,@outlook: ")
        if emailValido.EmailValido(email):
            break
    #fecha
    while True:
        fecha = input("introduzca fecha en forma: 01/01/0001:")
        if validarfecha.validarFecha(fecha):
            break
    #tipo de cliente
    while True:
        habitual = input("¿eres cliente habitual? (s/n): ")
        if clientehabitual.vip(habitual):
            break
    #introduccion de parametros en los diccionarios
    clients[dni] = client = {'nombre': nombre, 'apellidos': apellidos, 'direccion': direccion, 'teléfono': tlf,
                         'email': email, "fecha": fecha,
                         "habitual": habitual == "s" or habitual == "S" or habitual == "SI" or habitual == "si"}
def eliminar_cliente():
    dni = input('Introduce dni del cliente: ')
    if dni in clients: #si el dni esta en la lista de clientes la funcion del lo borrara
        del clients[dni]
        print("el cliente con dni", dni, "se a eliminado")
    else:
        print('No existe el cliente con dni', dni)
def mostrar_cliente():
    dni = input('Introduce dni del cliente: ')
    if dni in clients:
        print('dni:', dni)
        for key, value in clients[dni].items(): #para la clave valor en clientes donde la clave sera el dni y los valores los datos
            print(key.title() + ':', value)
    else:
        print('No existe el cliente con ese dni', dni)
def lista_clientes():
    print('Lista de clientes')
    for key, value in clients.items(): #para la clave valor en clients la funcion items devuelve una tupla con los pares clave-valor del diccionario.
        print(key, value["nombre"])
def lista_habituales():
    print('Lista de clientes habituales')
    for key, value in clients.items():
        if value['habitual']:
            print(key, value['nombre'])
def menu():          #Definimos la funcion menu
    salir = False     #mientras salir sea = a false se ejecutara el programa
    while not (salir):   #mientras no se cumpla la condicion salir repetira el bucle
        try:    # Sentencia try para las excepciones
            print('______ MENU ______')    #El menu impreso en pantalla
            print()
            print("1. crear cliente \n"
                  "2. eliminar cliente \n"
                  "3. mostrar cliente \n"       
                  "4. lista de clientes \n"
                  "5. lista clientes habituales \n"
                  "6. Salir \n     ")
            op = int(input("escoja una opción:")) # impresion en pantalla para opcion
            if op == 1:
                crear_cliente()
            elif op == 2:
                eliminar_cliente()
            elif op == 3:
                mostrar_cliente()     #opciones del menu
            elif op == 4:
                lista_clientes()
            elif op == 5:
                lista_habituales()
            elif op == 6:     # si opcion es igual a 6
                salir = True  # salir sera verdadero
                print("fin del programa")
            else:      #sino seleccione un numero dentro del rango indicado
                print()
                print("seleccione un numero del 1 al 6")
        except ValueError:     # esta es la sentecia except que va con el bloque try y si ocurre un error entrara la sentencia
            print("escribe un numero entero") # imprimira esto
menu()  #la llamada a la funcion menu






