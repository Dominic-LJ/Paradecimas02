rut = 0
digitoVer = 0
montofinal = 0
desc = 0
print("_______________FALABELLA________________")
print("\nBienvenido!")

rut = input("Ingrese su rut sin digito verificador: ")

while len(rut) != 8: 
 print("Error: deben ser 8 caracteres.")
 rut = (input("Ingrese su rut sin digito verificador: "))

digitoVer = (input("ingrese su digito verificador: "))
while len(digitoVer) != 1:
  print("Error: Solo debe ingresar un carácter.")
  digitoVer = (input("ingrese su digito verificador: "))

nombre = input(str("ingrese su nombre "))
monto = int(input("ingrese el monto de la compra "))

if monto <= 10000:
  print("montos de $10000 o menos no reciben descuento")
  montofinal = monto

if monto <= 50000 and monto >= 10001: #toda compra mayor a 10.001 hasta 50.000 pesos optiene uno 10% de descuento
  montofinal = monto - (monto/10)
  desc = str("Descuento aplicado de 10%")
  
if monto > 50000:
  montofinal = monto - (monto/20)
  desc = str("Descuento aplicado de 20%")

print(nombre)
print(f"su rut: {rut}-{digitoVer}")
print(desc)
print("su total a pagar es: $", montofinal)




