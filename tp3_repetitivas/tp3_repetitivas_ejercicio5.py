#nombre del personaje y validacion
nombreGladiador = input("Ingrese nombre del Gladeador: ").capitalize()
while not nombreGladiador.isalpha():
    print("Error. Solo se permiten letras.")
    nombreGladiador = input("Ingrese nombre del Gladeador: ").capitalize()
#definicion de variables
vidaGladiador = 100
vidaEnemigo = 100
pocionesVida = 3
dañoBaseGladiador = 15
dañoBaseEnemigo = 12
turnoGladiador = True
#inicio del juego
while vidaGladiador >= 0 and vidaEnemigo >= 0:
    #mostrar mensajes
    print("\nEstado de los jugadores")
    print(f"Vida Gladiador: {vidaGladiador} | Vida Enemigo: {vidaEnemigo}")
    print(f"Pociones restantes: {pocionesVida}")
    print("\nMenu")
    print("1. Ataque Pesado")
    print("2. Ráfaga Veloz")
    print("3. Curar")
    opcion = input("Elija una opcion (1-3): ")
    #validar ingreso de numeros
    while not opcion.isdigit():
        print("Error. Ingrese solo números")
        opcion = input("Elija una opcion (1-3): ")
    opcion = int(opcion)
    #validar rango
    while opcion < 1  or opcion > 3:
        print("Opción de menu invalida. Ingrese (1-3): ")
        opcion = input()
        while not opcion.isdigit():
            print("Error. Ingrese solo números")
            opcion = input("Elija una opcion (1-3): ")
    opcion = int(opcion)
    match opcion:
        case 1:
            if vidaEnemigo < 20:
                golpeCritico = dañoBaseGladiador * 1.5
                vidaEnemigo -= golpeCritico
                print(f"¡Atacaste al enemigo por {golpeCritico} puntos de daño!")
            else:
                vidaEnemigo -= dañoBaseGladiador
                print(f"¡Atacaste al enemigo por {dañoBaseEnemigo} puntos de daño!")
        case 2:
            for i in range(3):
                vidaEnemigo -= 5
                print("Golpe conectado por 5 de daño")
        case 3:
            if pocionesVida > 0:
                vidaGladiador += 30
                pocionesVida -= 1
            else:
                print("No quedan pociones")
                #perder turno
    turnoGladiador = False
    print("\nTurno del enemigo")
    if turnoGladiador == False:
        vidaGladiador -= dañoBaseEnemigo
        print(f"¡El enemigo te atacó por {dañoBaseEnemigo} puntos de daño!")
        turnoGladiador = True
        print("\nTurno del Gladiador")
#evualuar nivel de vida y definir ganador
if vidaGladiador > 0:
    print(f"¡VICTORIA! {nombreGladiador} ha ganado la batalla.")
else:
    print("Derrota. Has caido en combate.")





