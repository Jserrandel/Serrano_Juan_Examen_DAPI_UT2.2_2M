Diccionario = {}
while True:
    Seleccion = int(input("Sleccione una opcion: \n" 
                          "(1) Añadir alumno \n"
                          "(2) Numero de aprobados \n"
                          "(3) Mostrar todo el alumnado \n"))
    if Seleccion == 1:
        Alumno = input("Nombre del alumno: ")
        Notas = bool(int(input("Indica '0' si ha "
                               "suspendido '1' si ha aprobado \n")))
        Diccionario[Alumno] = Notas
    elif Seleccion == 2:
        Aprobados = 0
        for Notas in Diccionario.values():
            if Notas:
                Aprobados += 1
                print("El numero de aprobados es: " + str(Aprobados)+"\n")
    elif Seleccion == 3:
        print(Diccionario.keys())
    else:
        print("La opcion elegida no coincide con ninguna de las dadas \n")