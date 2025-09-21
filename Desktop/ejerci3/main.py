from promedio import promedio_estudiante
from notas import agregar_notas
from estudiante import agre_estudiante_notas

notas = {
    "David": [10, 8, 9],
    "Ana": [7, 9, 10],
    "Jose":[]
}

while True:
    print(notas)
    print("1. Imprimir promedio de cada estudiante")
    print("2. Agregar a estudiante existente")
    print("3. Agregar estudiante y nota")
    print("4. Exit")

    opcion = input("Choose an option: ")

    if opcion == "1":
        promedio_estudiante(notas)
    elif opcion == "2":
        agregar_notas(notas)
    elif opcion == "3":
        agre_estudiante_notas(notas)
    elif opcion == "4":
        print("Y`v gone out")
        break
    else:
        print("Enter an option")