#Ejercicio if
numerolf = int(input("Escribe un numero: "))
if numerolf < 0:
  print("Es negativo")
elif numerolf == 0:
  print("Es 0")
else:
  print(" Es positivo")
#Ejercicio While
numeroWhile = int(input("Escribe un numero: "))
while numeroWhile < 3:
  numeroWhile += 1
  print(numeroWhile)
#Ejercicio Bucle Do While
while True:
  numeroWhile = int(input("Escribe un numero: "))
  numeroWhile +=1
  print(numeroWhile)
  if numeroWhile == 3:
    break
#Ejercicio For Bucle
numeros = [0,1,2,3]
numeroFor = 0
for numero in numeros:
  if numero <= 3:
    numeroFor += 1
    print(numeroFor)
#Ejercicio Switch
estacion = input("Diga la estación: ")
if estacion == "Primavera":
  print("Estamos en primavera.")
elif estacion == "Verano":
  print("Estamos en Verano.")
elif estacion == "Otoño":
  print("Estamos en Otoño.")
elif estacion == "Invierno":
  print("Estamos en Invierno")
else:
  print("Default")