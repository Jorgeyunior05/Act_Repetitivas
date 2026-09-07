#Dibuja una pirámide de altura n.
n = int(input("ingresa la altura de la pirámide: "))
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * (2 * i - 1))
    