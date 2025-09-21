def agre_estudiante_notas(notas):
    while True:
        nombre = input("Enter the name: ")

        if nombre not in notas:
            notas[nombre] = []
            for i in range(3):
                while True:
                    try:
                        nota = int(input("Enter the grades: "))
                        notas[nombre].append(nota)
                        break
                    except ValueError:
                        print("Mistake, please enter a number")
            break
        else:
            print("Existe en el sistema")