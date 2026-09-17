def calcular_promedio(lista_numeros):
    suma_total = 0
    nota_total = 0
    for numero in lista_numeros:
        suma_total = numero + suma_total
        nota_total += 1
    return suma_total / nota_total

def obtener_promedios(datos_alumnos):
    lista_promedios = []
    for dato in datos_alumnos:
        lista_notas = dato[1:]
        promedio = calcular_promedio(lista_notas)
        dato.append(promedio)
        lista_promedios.append(dato)
    return lista_promedios

def linea():
    print("-" * 25)

def mensaje_promedios(lista_promedios):
    linea()
    print("Promedio de alumnos listados:")
    linea()
    for promedio_alumno in lista_promedios:
        promedio = promedio_alumno[-1]
        promedio = round(promedio, 2)
        alumno = promedio_alumno[0]
        lista_notas = promedio_alumno[1:-1]
        notas = ", ".join(map(str, lista_notas))
        print(f'Alumno: {alumno}\nNotas: {notas}\nPromedio: {promedio}')
        linea()

datos_alumnos = (['Roberto', 3, 4, 5, 6, 8], ['Ayelen', 5, 8, 9])

lista_promedios = obtener_promedios(datos_alumnos)
mensaje_promedios(lista_promedios)