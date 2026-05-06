num1 = int(input("ingresa el limite inferior: "))
num2 = int(input("ingresa el limite superior: "))
while num1>=num2:
    print("error el limite inferior debe ser menor al superior")
    num1 = int(input("ingresa el limite inferior"))
    num2 = int(input("ingresa el limite superior"))
import random
numero = random.randint(num1,num2)
ajustado = (numero//3)*3

if ajustado < num1:
    ajustado = num1
    #intento 1
intento = int(input("intenta adivinar: "))
if intento == ajustado:
    print("felicitaciones, adivino el numero")
else:
    if intento < ajustado:
        print("el numero que buscas es mayor")
    else:
        print("el numero que buscas es menor")

#intento 2
    intento2 = int(input("intenta de nuevo: "))
if intento2 == ajustado:
    print("felicitaciones, adivino el numero")
else:
    if intento2 < ajustado:
        print("el numero que buscas es mayor")
    else:
        print("el numero que buscas es menor")

#pista
    
print("t dare una pisra")
dist1  = abs (ajustado - intento)
dist2 = abs (ajustado - intento2)
if dist1 < dist2:
    print(f"el numeor que buscas es mas cerac de {intento} que de {intento2}")
elif dist2 < dist1:
    print(f"el numero es mas cerca de  {intento2} que de {intento}")
else:
    print("ambos intentos estan a la misma distancai")

    #intento 3

intento3 = int(input("intenta una ultima vez: "))
if intento3 == ajustado:
    print("increible, lo has logrado")
else:
    print("cagaste")
