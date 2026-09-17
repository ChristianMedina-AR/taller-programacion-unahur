def linea():
    print("-" * 50)

def contar_ocurrencias(lista, elemento):
    return lista.count(elemento)

def agrupar_ocurrencias(lista_modelos):
    lista_modelos_concurrente = []
    for modelo in set(lista_modelos):
        cantidad_modelos = contar_ocurrencias(lista_modelos, modelo)
        lista_modelos.remove(modelo)
        lista_temporal = []
        lista_temporal.append(modelo)
        lista_temporal.append(cantidad_modelos)
        lista_modelos_concurrente.append(lista_temporal)
    return lista_modelos_concurrente

def normalizar_lista(lista_modelos):
    lista_normalizada = []
    acentos = str.maketrans("áéíóú", "aeiou")
    for modelo in lista_modelos:
        normalizado = modelo.strip()
        normalizado = normalizado.lower()
        normalizado = normalizado.translate(acentos)
        lista_normalizada.append(normalizado)
    return lista_normalizada


def consultar_indices_ocurrencia_max(lista_modelos_concurrente):
    cantidad = 0
    indices_max = []
    for orden, modelo in enumerate(lista_modelos_concurrente):
        if modelo[1] == cantidad:
            indices_max.append(orden)
            cantidad = modelo[1]
        elif modelo[1] > cantidad:
            indices_max.clear()
            indices_max.append(orden)
            cantidad = modelo[1]
        else:
            continue
    return indices_max

def plantilla_mensaje(indices_ganadores, lista_modelos_concurrentes):
    linea()
    print("Lista original de los modelos registrados:")
    linea()
    lista_modelos_str = ", ".join(lista_modelos)
    print(f"{lista_modelos_str}.")
    linea()
    print("Lista normalizada y agrupada con sus cantidades registradas:")
    linea()
    for modelo in lista_modelos_concurrentes:
        modelo_capitalizado = modelo[0].capitalize()
        cantidad = str(modelo[1])
        print(f"Modelo: {modelo_capitalizado} - Cantidad: {cantidad}")
    linea()
    print("Modelo, o modelos, con mayor cantidad de ocurrencias:")
    linea()
    print("Modelo/s:")
    for indice in indices_ganadores:
        modelo = lista_modelos_concurrentes[indice][0]
        modelo_capitalizado = modelo.capitalize()
        print(f"- {modelo_capitalizado}")
    cantidad = lista_modelos_concurrentes[indices_ganadores[0]][1]
    cantidad = str(cantidad)
    print(f"Cantidades: {cantidad}")
    linea()

lista_modelos = ["ford", "Fórd", "ford ", "renáut", "renaut", "ford", "renaut", "renaut", "renaut", "ford"]
lista_modelos_normalizada = normalizar_lista(lista_modelos)
lista_modelos_concurrentes = agrupar_ocurrencias(lista_modelos_normalizada)
indices_ganadores = consultar_indices_ocurrencia_max(lista_modelos_concurrentes)
plantilla_mensaje(indices_ganadores, lista_modelos_concurrentes)