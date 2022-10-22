def tlfValido(tlf):
    t = tlf.isdigit() #creamos una variable con la que comprobaremos si los caracteres son numericos con el comando isdigit
    if len(tlf) < 9 or len(
            tlf) > 9:  # utilizamos la funcion len para contar los caracteres de tlf
        print("el telefono debe contener 9 caracteres")
        return False
    elif t is False:
        print("el tlf debe contener 9 caracteres numericos")
        return False
    else:
        return True
