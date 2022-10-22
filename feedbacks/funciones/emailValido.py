def EmailValido(email):
    if email.count("@hotmail") or email.count("@gmail") or email.count("@outlook") and email.count("."):
        return True
    else:
        print("el email es incorrecto")
        return False
