clients = []
vip = []
def crear_cliente():
    #dni
    while True:
        dni = input("introduce tu dni: ")  # definimos la variable que pedira datos al usuario
        nif = dni[
              :8]  # definimos una variable para contar dni de 0 hasta 8 que son los numeros que queremos contar para comprobar el dni
        n = nif.isdigit()  # creamos variable que te dice si todos los strings de 0 a 8 son numericos
        i = len(dni)  # variable para contanr el numero de caracteres
        if i != 9:  # si el numero de caracteres es diferente de 9
            print("el dni debe contener 9 caracteres")  # imprimira esto
        elif n is False:  # o si n es falso
            print("los 8 primeros caracteres deben ser numericos")  # imprimira esto
        else:
            break
    #nombre
    nombre = input("escribe tu nombre: ")
    #apellidos
    apellidos = input("escribe tus apellidos: ")
    #direccion
    direccion = input("escribe tu direccion: ")
    #telefono
    while True:
        tlf = input("escribe tu tlf: ")
        if len(tlf) < 9 or len(
                tlf) > 9:  # si el numero de caracteres es menor o mayor que 9 entrara la siguiente linea sino entrara else:
            print("el tlf debe contener 9 caracteres numericos")
        else:
            break  # sale de la iteracion
    #email
    while True:
        email = input("introduce tu direccion email: ")
        if email.count("@hotmail") or email.count("@gmail") or email.count("@outlook") and email.count("."):
            break
        else:
            print("el email es incorrecto")
    #fecha
    while True:
        fecha = input("introduzca fecha en forma: 01/01/0001:")
        i = len(fecha)  # creamos una variable para contar los caracteres
        fechaSplit = fecha.split("/")
        if i != 10:  # si los caracteres son diferentes de 10 imprimira la siguiente linea
            print("la fecha debe contener 10 caracteres / incluidas")
        if (not fecha.count("/")) or len(fechaSplit) != 3 and i >= 8 and i <= 10:
            print("la fecha debe incluir minimo 2 /")
        else:
            if (fechaSplit[0].isdigit() and int(fechaSplit[0]) > 0 and int(fechaSplit[0]) < 32):
                if (fechaSplit[1].isdigit() and int(fechaSplit[1]) > 0 and int(fechaSplit[1]) <= 12):
                    if (fechaSplit[2].isdigit() and int(fechaSplit[2]) < 2100 and int(fechaSplit[2]) >= 1920):
                        break
                    else:
                        print("año incorrecto")
                else:
                    print("mes incorrecto")
            else:
                print("dia incorrecto")
    #tipo de cliente
    while True:
        habitual = input("¿eres cliente habitual? (s/n): ")
        if habitual == "s" or habitual == "S" or habitual == "SI" or habitual == "si":
            habitual = True #creamos el valor de la variable bool para poder comprobar el tipo de cliente mas adelante
            break
        elif habitual == "n" or habitual == "N" or habitual == "NO" or habitual == "no":
            habitual = False
            break
        else:
            print("[Error] Ingrese si o no.")
            continue
    #listas a las que iran los datos
    if habitual:
        vip.extend([[dni, nombre, apellidos, direccion, tlf, email, fecha, habitual]]) #metodo extend para introducir varios parametros
        clients.extend([[dni, nombre, apellidos, direccion, tlf, email, fecha, habitual]])
    else:
        clients.extend([[dni, nombre, apellidos, direccion, tlf, email, fecha, habitual]])
def eliminar_cliente():
    dni = input('Introduce dni del cliente: ')
    for client in clients:  # dentro de clientes buscaremos un cliente
        if dni in client: #si el dni esta en algun cliente
            del client[:] #eliminara el cliente con ese dni y sus datos
            print("el cliente con dni", dni, "se a eliminado")
            break
    else:
        print('No existe el cliente con dni', dni)
def mostrar_cliente():
    dni = input('Introduce dni del cliente: ')
    for client in clients:
        if dni in client:
            print(client[:]) #mostrara todos los datos del cliente
            break
    else:
        print('No existe el cliente con ese dni', dni)
def lista_clientes():
    print('Lista de clientes')
    for client in clients:
        print(client[:2]) #mostrara los dos primeros datos del cliente
def lista_habituales():
    print('Lista de clientes habituales')
    for v in vip:
        print(v[:2])
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
            op = int(input("escoga una opción:")) # impresion en pantalla para opcion
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

