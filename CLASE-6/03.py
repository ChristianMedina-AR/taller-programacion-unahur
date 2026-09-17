def celsius_a_fahrenheit(grados):
	return (grados * 1.8) + 32

def crear_lista(lista_temp):
	lista_convertida = []
	for temp in lista_temp:
		fahrenheit = celsius_a_fahrenheit(temp)
		lista_convertida.append(fahrenheit)
	return lista_convertida

temp_celsius = [10, 32, 12, 14]
temp_fahrenheit = crear_lista(temp_celsius)
for orden, temp in enumerate(temp_fahrenheit):
	print(f"{temp_celsius[orden]} C° > {temp} F°")
	orden += 1