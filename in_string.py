def check_vowels():

    nombre = str(input("Ingresa tu nombre:"))
    nombre = nombre.lower()

    contiene_a = "a" in nombre
    contiene_e = "e" in nombre
    contiene_i = "i" in nombre
    contiene_o = "o" in nombre
    contiene_u = "u" in nombre

    print(f"Contiene a: {contiene_a}")
    print(f"Contiene e: {contiene_e}")
    print(f"Contiene i: {contiene_i}")
    print(f"Contiene o: {contiene_o}")
    print(f"Contiene u: {contiene_u}")
