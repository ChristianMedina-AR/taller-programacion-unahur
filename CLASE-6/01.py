def es_par(numero):
	return numero % 2 == 0

def comprobar():
	lista_numero = [0, 1, 2, 43, 123, 54]
	for numero in lista_numero:
		if es_par(numero) is True:
			print(numero)

comprobar()