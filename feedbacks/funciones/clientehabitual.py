def vip(habitual):
    if habitual == "s" or habitual == "S" or habitual == "SI" or habitual == "si":
        tipo = "Cliente habitual"
        return True
    elif habitual == "n" or habitual == "N" or habitual == "NO" or habitual == "no":
        tipo = "otro tipo"
        return True
    else:
        print("[Error] Ingrese si o no.")
        return False