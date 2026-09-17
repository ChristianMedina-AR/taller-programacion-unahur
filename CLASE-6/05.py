def invertir_cadena(texto):
    return texto[::-1]
    
def identificar_palindromo(texto):
    texto = texto.replace(" ", "") # Quitamos los espacios.
    texto = texto.lower() # Convertimos todo en minuscula.
    texto_invertida = invertir_cadena(texto) # Enviamos a invertir.
    return texto_invertida == texto


texto = input('Ingrese texto para identificar si es un palíndromo: ')
resultado = identificar_palindromo(texto)
if resultado is True:
    print('✔ El texto es un palíndromo.')
else:
    print('✖ El texto no es un palíndromo.')