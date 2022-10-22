def validarFecha(fecha):
    i = len(fecha)  # creamos una variable para contar los caracteres
    fechaSplit = fecha.split("/") #metodo split introduce una / como separador y divide una cadena en una lista
    if i != 10:  # si los caracteres son diferentes de 10 imprimira la siguiente linea
        print("la fecha debe contener 10 caracteres / incluidas")
    if (not fecha.count("/")) or len(fechaSplit) != 3 and i >= 8 and i <= 10: #comprobamos que hay / o que la cadena se a dividido en 3 partes y que i es mayor o igual que 8 y menor o igual que 10
        print("la fecha debe incluir minimo 2 /")
    else:
        if (fechaSplit[0].isdigit() and int(fechaSplit[0]) > 0 and int(fechaSplit[0]) < 32):#comprobamos que la primera parte en este caso los dias son caracteres numericos que el numero introducido es mayor que 2 y menor de 32
            if (fechaSplit[1].isdigit() and int(fechaSplit[1]) > 0 and int(fechaSplit[1]) <= 12):#comprobamos que la segunda parte en este caso los meses son caracteres numericos, mayor que 0 y menor o igual 12
                if (fechaSplit[2].isdigit() and int(fechaSplit[2]) < 2100 and int(fechaSplit[2]) >= 1920):#comprobamos que la tercera parte en este caso el año son caracteres numericos, menor que 2100 y mayor que 1920
                    return True
                else:
                    print("año incorrecto")
                    return False
            else:
                print("mes incorrecto")
                return False
        else:
            print("dia incorrecto")
            return False
