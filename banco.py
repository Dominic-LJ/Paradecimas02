"""
solicitar numero de rut, 
debe ser validado con el  numero de verificacion. 
luego debe poner la clave de no mas de 10 digitos ni menos.
"""
rut = 0
clave = 0
digitoVer = 0

print("_______________BANCO SANTANDER________________")
print("\nBienvenido!")

rut = input("Ingrese su rut sin digito verificador: ")
while len(rut) < 7 or len(rut) > 8:
  print("Error: deben ser 7 u 8 caracteres.")
  rut = (input("Ingrese su rut sin digito verificador: "))

digitoVer = (input("ingrese su digito verificador: "))
while len(digitoVer) != 1:
  print("Error: Solo debe ingresar un carácter.")
  digitoVer = (input("ingrese su digito verificador: "))

print(f"su rut: {rut}-{digitoVer}")

clave = input("Escriba su contraseña (10 digit): ")
while len(clave) != 10:
  clave = input("Escriba su contraseña (10 digit): ")

print("Has ingresado correctamente.")


