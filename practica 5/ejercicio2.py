numero = int(input("Ingresa un numero entero: "))

resultado = numero
for i in range(numero):
    if i != numero:
        resultado -= 1
        
        print(resultado, end=", ")