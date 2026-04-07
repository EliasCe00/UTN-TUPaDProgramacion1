#EJERCICIO 3

lunes1 = ""
lunes2 = ""
lunes3 = ""
lunes4 = ""
martes1 = ""
martes2 = ""
martes3 = ""

nombreOperador = input("Ingrese nombre de operador: ").capitalize()
while not nombreOperador.isalpha():
    nombreOperador = input("Ingrese nombre de operador: ").capitalize()

while True:
    print("1. Reservar turno")
    print("2. Cancelar turno")
    print("3. Ver agenda del dia")
    print("4. Ver resumen genearal")
    print("5. Cerrar sistema")
    opcion = input()
    while not opcion.isdigit() or int(opcion) < 1 or int(opcion) > 5:
        opcion = input("Ingrese una opción válida (1-5): ")

    match opcion:
        case "1":
            dia = input("Elija que dia quiere reservar. (1 para lunes / 2 para martes) ")
            while not dia.isdigit() or not (dia == "1" or dia == "2"):
                dia = input("Ingrese una dia numero valido: ")
            dia = int(dia)

            nombrePaciente = input("Ingrese su nombre: ").capitalize()
            while not nombrePaciente.isalpha():
                nombrePaciente = input("Ingrese un nombre valido. (Solo letras) ").capitalize()
            if dia == 1:
                if nombrePaciente == lunes1 or nombrePaciente == lunes2 or nombrePaciente == lunes3 or nombrePaciente == lunes4:
                    print("Ese paciente ya tiene turno el lunes")
                elif lunes1 == "":
                    lunes1 = nombrePaciente
                elif lunes2 == "":
                    lunes2 = nombrePaciente
                elif lunes3 == "":
                    lunes3 = nombrePaciente
                elif lunes4 == "":
                    lunes4 = nombrePaciente
                else:
                    print("No hay turnos disponibles")
            elif dia == 2:
                if nombrePaciente == martes1 or nombrePaciente == martes2 or nombrePaciente == martes3:
                    print("Ese paciente ya tiene turno el martes")
                elif martes1 == "":
                    martes1 = nombrePaciente
                elif martes2 == "":
                    martes2 = nombrePaciente
                elif martes3 == "":
                    martes3 = nombrePaciente
                else:
                    print("No hay turnos disponibles")
        case "2":
            dia = input("Ingrese un dia: (1 para lunes / 2 para martes) ")
            while not dia.isdigit() or not (dia == "1" or dia == "2"):
                dia = input("Ingrese un numero valido: ")
            dia = int(dia)

            nombrePaciente = input("Ingrese su nombre").capitalize()
            while not nombrePaciente.isalpha():
                nombrePaciente = input("Ingrese un nombre valido. (Solo letras)").capitalize()
            if dia == 1:
                if lunes1 == nombrePaciente:
                    lunes1 = ""
                elif lunes2 == nombrePaciente:
                    lunes2 = ""
                elif lunes3 == nombrePaciente:
                    lunes3 = ""
                elif lunes4 == nombrePaciente:
                    lunes4 = ""
                else:
                    print("Turno no encontrado")
            elif dia == 2:
                if martes1 == nombrePaciente:
                    martes1 = ""
                elif martes2 == nombrePaciente:
                    martes2 = ""
                elif martes3 == nombrePaciente:
                    martes3 = ""
                else:
                    print("Turno no encontrado")
        case "3":
            print("Resumen de turnos:")
            dia = input("Ingrese un dia: (1 para lunes / 2 para martes) ")
            while not dia.isdigit() or not (dia == "1" or dia == "2"):
                dia = input("Ingrese un numero valido: ")
            dia = int(dia)

            if dia == 1:
                print("Lunes:")
                print(f"Turno 1: {lunes1 if lunes1 != '' else '(libre)'}")
                print(f"Turno 2: {lunes2 if lunes2 != '' else '(libre)'}")
                print(f"Turno 3: {lunes3 if lunes3 != '' else '(libre)'}")
                print(f"Turno 4: {lunes4 if lunes4 != '' else '(libre)'}")
            else:
                print("Martes:")
                print(f"Turno 1: {martes1 if martes1 != '' else '(libre)'}")
                print(f"Turno 2: {martes2 if martes2 != '' else '(libre)'}")
                print(f"Turno 3: {martes3 if martes3 != '' else '(libre)'}")
        case "4":
            turnosOcupadosLunes = 0
            turnosOcupadosMartes = 0
            if lunes1 != "":
                turnosOcupadosLunes += 1
            if lunes2 != "":
                turnosOcupadosLunes += 1
            if lunes3 != "":
                turnosOcupadosLunes += 1
            if lunes4 != "":
                turnosOcupadosLunes += 1
            if martes1 != "":
                turnosOcupadosMartes += 1
            if martes2 != "":
                turnosOcupadosMartes += 1
            if martes3 != "":
                turnosOcupadosMartes += 1

            print("Lunes: ")
            print(f"Turnos ocupados: {turnosOcupadosLunes} | Turnos libres: {4 - turnosOcupadosLunes}")
            print("Martes: ")
            print(f"Turnos ocupados: {turnosOcupadosMartes} | Turnos libres: {3 - turnosOcupadosMartes}")

            if turnosOcupadosLunes > turnosOcupadosMartes:
                print("Mayor cantidad de turnos el lunes.")
            elif turnosOcupadosMartes > turnosOcupadosLunes:
                print("Mayor cantidad de turnos el martes.")
            else:
                print("Misma cantidad de turnos en ambos dias.")
        case _:
            print("Sistema cerrado")
            break