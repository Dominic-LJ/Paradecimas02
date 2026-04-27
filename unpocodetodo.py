"""
probar todas las opciones de python que hemos aprendido
while, break
f(hola {vrariable})
contador i <- i + 1
if elif else
lista
bool
""" 

clientes = 0
opcion = 0
items = ["leche", "fideos", "fruta"]

print("----------------SUPERMERCADO DONDE PEPITO----------------")
print("Bienvenido al supermercado!")


while clientes >= 0:
    print("\n1. Comprar")
    print("2. Pagar")
    print("3. Salir")
    opcion = int(input("indique el numero de opcion: "))
    if opcion == 1:
        print("\nProductos disponibles:")
        items = ["leche", "huevos", "queso", "cafe"]
        for i in range(len(items)):
         print(f"{i}: {items[i]}")
        ItemSeleccionado = int(input("\nseleccione el numero de producto: "))
        addtocart = items[ItemSeleccionado]
        print(f"\nse ha agregado a el carrito ", {addtocart})
        
    if opcion == 2:
        pago = input("indique su sistema de pago: ")
        print("pago aprobado")
        clientes = clientes + 1


    if opcion == 3:
     print("Estas saliendo de la tienda...")
     break


