#Capitalizar palabra.
def capitalizar_palabra(palabra):
    return palabra.capitalize()

#Capitalizar frase entera.
def capitalizar_frase(frase):
    lista_palabras = frase.split()
    lista_palabras_capitalizadas = []
    for palabra in lista_palabras:
        palabra_capitalizada = capitalizar_palabra(palabra)
        lista_palabras_capitalizadas.append(palabra_capitalizada)
    palabras_capitalizadas = " ".join(lista_palabras_capitalizadas)
    return palabras_capitalizadas

frase = input("Ingrese una frase para capitalizar:\n")
frase_capitalizada = capitalizar_frase(frase)
print(f"La frase capitalizada ingresada es:\n{frase_capitalizada}")