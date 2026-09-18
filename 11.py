def linea():
    print("-" * 50)

def es_bisiesto(anio):
    return (anio % 4 == 0) and (anio % 100 != 0 or anio % 400 == 0)

def rango_anios(inicio, fin):
    anios_biciestos = []
    for anio in range(inicio, fin + 1):
        biciesto = es_bisiesto(anio)
        if biciesto is True:
            anio = str(anio)
            anios_biciestos.append(anio)
    return anios_biciestos

def plantilla_mensaje(lista_anios_biciestos):
    anios_biciestos = ", ".join(lista_anios_biciestos)
    linea()
    print (f"Los años biciestos del rango ingresado son:\n{anios_biciestos}.")
    linea()

inicio = int(input("Ingrese el comienzo del año: "))
fin = int(input("Ingrese el final del año: "))
lista_anios_biciestos = rango_anios(inicio, fin)
plantilla_mensaje(lista_anios_biciestos)