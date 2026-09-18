def clasificar_nota(nota):
    match nota:
        case nota if nota >= 7:
            return "aprobado"
        case nota if nota < 7:
            return "desaprobado"
        case _:
            return "ausente"

def definir_nota():
    nota = input("Ingrese la nota del alumno: ")
    nota = int(nota)
    estado = clasificar_nota(nota)
    print(f"Su exámen esta {estado}.")

definir_nota()