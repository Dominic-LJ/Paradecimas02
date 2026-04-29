"""
Una tienda de retail necesita un programa que permita calcular el descuento aplicado a una compra.
Nombre del cliente (mínimo 3 caracteres)
Monto de la compra (número entero positivo)
Validaciones:

Nombre válido
Monto mayor o igual a 0
"""
print("________TIENDITA________")
nombre = None
monto = 0

nombre = input("Ingrese su nombre: ")
while len(nombre) < 3:
    print("su nombre debe tener al menos 3 digitos")
    nombre = input("Ingrese su nombre: ")
print(f"bienvenid@ {nombre}")

monto = int(input("Ingrese el monto de la compra: "))
while monto < 0:
    print("\nmonto no válido, ingrese monto mayor a 0")
    monto = int(input("Ingrese el monto de la compra: "))
print("yabien")

if monto < 10000:
    print("\nmontos menores de $10000 no obtienen descuento")
    print(f"Su monto total: {monto}")
elif monto >= 10000 and monto <= 50000:
    monto = monto - (monto/10)
    print("\nSe le ha aplicado un descuento del 10%")
    print(f"Su monto total: {monto}")
elif monto > 50000:
    print("\nSe le ha aplicado un descuento del 20%")
    print(f"Su monto total: {monto}")