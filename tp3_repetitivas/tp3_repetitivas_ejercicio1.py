#TRABAJO PRACTICO 3 - ESTRUCTURAS REPETITIVAS
#-
#EJERCICIO 1
totalSinDescuento = 0
totalConDescuento = 0

nombreCliente = input("Ingrese un nombre: ")
while nombreCliente != "" or not(nombreCliente.isalpha()):
    nombreCliente = input("Ingrese un nombre valido: ")

cantProductos = (input("Ingrese la cantidad de productos a comprar: "))
while not(cantProductos.isdigit()):
    cantProductos = (input("Ingrese la cantidad de productos a comprar: "))

cantProductos = int(cantProductos)
for i in range(cantProductos):
    precio = (input("Precio: "))
    while precio == 0 or not(precio.isdigit()):
        precio = (input("Precio: "))
    
    descuento = input("Descuento (S/N): ").upper()
    while not(descuento == "S" or descuento == "N"):
        descuento = input("Descuento (S/N): ").upper()

    precio = int(precio)
    totalSinDescuento += precio 
    if descuento == "S":
        totalConDescuento += precio * 0.90
    else:
        totalConDescuento += precio

ahorro = totalSinDescuento - totalConDescuento
promedio = float(totalConDescuento / cantProductos)

print(f"Total sin descuentos: ${totalSinDescuento}")
print(f"Total con descuentos: ${totalConDescuento}")
print(f"Ahorro: ${ahorro}")
print(f"Promedio por producto: ${promedio:.2f}")



