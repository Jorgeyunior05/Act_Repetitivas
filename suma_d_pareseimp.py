suma_pares = 0
suma_impares = 0
for i in range(5):
    numero = int(input("ingresa un numero entero"))
    if numero % 2 == 0:
        suma_pares += numero
    else:
        suma_impares += numero
print("la suma de los numeros pares es:", suma_pares)
print("la suma de los numeros impares es:", suma_impares)
