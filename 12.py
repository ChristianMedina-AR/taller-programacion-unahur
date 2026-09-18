def numero_feliz(numero):
    return numero <= 10

def sumar_digitos(numero):
    numeros = str(numero)
    for digito in numeros:
        feliz = numero_feliz(int(digito))
        if feliz is True:
            continue
        else:
            return False
    return True

def mensaje(estado):
    if estado is True:
        print("Los digitos del número ingresa son felices.")
    else:
        print("Los números no son todos felices")

numero = int(input("Ingrese el número: "))
feliz = sumar_digitos(numero)
mensaje(feliz)