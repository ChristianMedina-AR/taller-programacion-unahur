def es_primo(numero):
    return numero % 2 != 0

def filtrar_primos(lista):
    lista_primos = []
    for numero in lista:
        if es_primo(numero) is True:
            lista_primos.append(numero)
    lista_primos = map(str, lista_primos)
    lista_primos = ", ".join(lista_primos)
    return lista_primos

lista_numeros = [0, 3, 5, 4, 9, 7, 8, 25, 3652, 26236]
lista_primos = filtrar_primos(lista_numeros)
lista_numeros = map(str, lista_numeros)
lista_numeros = ", ".join(lista_numeros)
print(f"Números listados: {lista_numeros}.\nNúmeros primos de la lista: {lista_primos}.")