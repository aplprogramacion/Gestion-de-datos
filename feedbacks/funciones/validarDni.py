def dniValido(dni):  # definimos la funcion
    nif = dni[:8]  # definimos una variable para contar dni de 0 hasta 8 que son los numeros que queremos contar para comprobar el dni
    n = nif.isdigit()  # creamos variable que te dice si todos los strings de 0 a 8 son numericos con el comando isdigit
    i = len(dni)  # variable para contanr el numero de caracteres
    if i != 9:  # si el numero de caracteres es diferente de 9
        print("el dni debe contener 9 caracteres")  # imprimira esto
        return False
    elif n is False:  # si n es falso
        print("dni incorrecto")  # imprimira esto
        return False
    else:
        return True
