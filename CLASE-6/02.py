def es_vocal(caracter):
	vocales = ["a", "e", "i", "o", "u"]
	return caracter in vocales
		
def contar_vocales(palabra):
	contador = 0
	for letra in palabra:
		if es_vocal(letra) is True:
			contador += 1
	return contador

palabra = input("Ingrese una palabra: ")
contador = contar_vocales(palabra)
print("La cantidad de vocales que tiene la palabra es:", contador)