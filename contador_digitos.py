numero = int(input("ingresa un numero entero"))
contador = 0
numero = abs(numero)
if numero == 0:
    contador = 1
else:
    while numero > 0:
        numero = numero // 10 
        contador += 1
print("el numero tiene ", contador, "digitos.")