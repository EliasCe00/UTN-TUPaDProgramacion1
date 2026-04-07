#EJERCICIO 4

#declaracion de variables
energia = 100
tiempo = 12
cerradurasAbiertas = 0
alarma = False
codigoParcial = ""

forzarSeguidas = 0
#ingreso y validacion de nombre
nombreAgente = input("Ingrese el nombre del agente: ")
while not nombreAgente.isalpha():
    nombreAgente = input("Error. Ingrese un nombre valido, solo letras: ")

while energia > 0 and tiempo > 0 and cerradurasAbiertas < 3:
    
    #mostrar estado
    print(f"\nEstado del Agente: {nombreAgente}")
    print(f"Energia: {energia}")
    print(f"Tiempo: {tiempo}")
    print(f"Cerraduras Abiertas: {cerradurasAbiertas}")
    print(f"Alarma: {alarma}")
    print(f"Codigo Parcial: {codigoParcial}")
    
    #imprimir menu de opciones
    print("1. Forzar cerradura")
    print("2. Hackear")
    print("3. Descansar")
    #validar opcion ingresada
    opcion = input("Ingrese una opcion: (1, 2 o 3) ")
    while not opcion.isdigit() or int(opcion) < 1 or int(opcion) > 3:
        opcion = input("Error. Ingrese una opcion valida (1, 2 o 3): ")
    #convierte a entero el numero ingresado 
    opcion = int(opcion)

    match opcion:
        case 1:
            forzarSeguidas += 1
            if forzarSeguidas == 3:
                energia -= 20
                tiempo -= 2
                alarma = True
                print("Cerradura trabada por forzar demasiadas veces!")
                forzarSeguidas = 0
            else:
                energia -= 20
                tiempo -= 2
                
                if energia < 40:
                    numero = input("Ingrese 1, 2 o 3: ")
                    while not numero.isdigit() or int(numero) < 1 or int(numero) > 3:
                        numero = input("Error. Ingrese 1, 2 o 3: ")
                    if int(numero) == 3:
                        alarma = True
                if not alarma:
                    cerradurasAbiertas += 1
        case 2:
            energia -= 10
            tiempo -= 3
            for i in range(4):
                print(f"Paso{i+1}/4")
                codigoParcial += "A"
            if len(codigoParcial) >= 8:
                if cerradurasAbiertas < 3:
                    cerradurasAbiertas += 1
            forzarSeguidas = 0
        case 3:
            energiaMaxima = 100
            if energia < energiaMaxima:
                if energia <= 85:
                    energia += 15
                else:
                    energia = energiaMaxima

            tiempo -= 1

            if alarma == True:
                energia -=10
            
            forzarSeguidas = 0
    
    if alarma == True and tiempo <= 3 and cerradurasAbiertas < 3:
        print("Sistema bloqueado. Perdiste")
        break
    if cerradurasAbiertas == 3:
        print("Victoria")
        break
    if energia <= 0 or tiempo <= 0:
        print("Derrota")
        break
print("Fin del juego.")