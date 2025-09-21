def agregar_notas(notas):
    while True:
        print("1. Display student grades")
        print("2. Display student who haven`t grades")
        print("3. Exit")

        opcion = input("Enter an option: ")

        if opcion == "1":
            while True:
                estudiante = input("Enter the name: ").title()
                if estudiante in notas:
                        if notas[estudiante]:
                            print(f"{estudiante} has grade {notas[estudiante]}")
                        else:
                            print(f"{estudiante} haven`t grades")
                        break
        elif opcion == "2":
            while True:
                estudiante = input("Enter the name: ").title()
                
                if estudiante in notas:
                    if not notas[estudiante]:
                        print(f"{estudiante} hasn`t grade {notas[estudiante]}")
                        while True:
                            print("Do y want to enter grades? ")
                            print("Enter 'True' to enter grades or 'False' to exit")

                            opcion = (input("Enter an option: ")).strip().lower()

                            if opcion == "true":
                                for i in range(3):
                                    while True:
                                        try:
                                            nota = int(input("Enter the grades: "))
                                            notas[estudiante].append(nota)
                                            break
                                        except ValueError:
                                            print("Enter a whole number")
                            elif opcion == "false":
                                print("Not enter grades")
                                break
                            else:
                                print("Error")

                    else:
                        print(f"{estudiante} have grades")
                    break
        elif opcion == "3":
             print("Finish")
             break
        else:
            print(f"{estudiante} doesn`t exist")
