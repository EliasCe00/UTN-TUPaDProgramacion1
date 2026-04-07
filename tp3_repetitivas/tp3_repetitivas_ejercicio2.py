#EJERCICIO 2
usuarioCorrecto = "alumno"
claveCorrecta = "python123"
salir = False

for i in range(3):
    usuario = input("Ingese su usuario: ")
    clave = input("Ingrese su clave: ")
    while usuario == usuarioCorrecto and clave == claveCorrecta:
        print("1. Ver estado de inscripción")
        print("2. Cambiar clave")
        print("3. Mostrar mensaje motivacional")
        print("4. Salir")
        opcion = input()
        while not(opcion.isdigit()) and (opcion < 1 or opcion > 4):
            print("1. Ver estado de inscripción")
            print("2. Cambiar clave")
            print("3. Mostrar mensaje motivacional")
            print("4. Salir")
            opcion = input()
        
        match opcion:
            case "1":
                print("Inscripto")
            case "2":
                nuevaClave = input("Ingrese su nueva clave: ")
                while nuevaClave.len() < 6:
                    nuevaClave = input("Intente con una clave mas larga. Minimo 6 caracteres")
                validarClave = input("Confirme su clave: ")
                while not validarClave == nuevaClave:
                    validarClave = input("Confirme su clave: ")
                clave = nuevaClave
                print("Clave cambiada correctamente")
            case "3":
                print("Si puedes soñarlo, puedes programarlo")
            case _:
                salir = True
                break
    if salir:
        break
    print("Error: credenciales invalidas")
    intento = i + 1
    print(f"Intento ({intento}/3)")
if intento == 3:
    print("Cuenta Bloqueada")