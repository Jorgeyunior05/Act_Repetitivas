numero = int(input("ingresa un numero entero"))
invertido = 0
while numero > 0:
    digito = numero % 10
    invertido = invertido * 10 + digito
    numero = numero // 10
print("el numero invertido es:", invertido)