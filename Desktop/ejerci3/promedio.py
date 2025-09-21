def promedio_estudiante(notas):
    while True:
        print("1. Ver notas de estudiantes que si tienen")
        print("2. Ver estudiantes que no tienen notas")
        print("3. Exit")

        opcion = input("Enter an option: ")

        if opcion == "1":
            for clave, valor in notas.items():
                if valor:
                    promedio = sum(valor) / len(valor)
                    print(f"{clave} y la nota {promedio:.2f}")
        elif opcion == "2":
            for clave, valor in notas.items():
                if not valor:
                    print(f"{clave}")
        elif opcion == "3":
            print("Terminado")
            break
        else:
            print("Enter an option")
        