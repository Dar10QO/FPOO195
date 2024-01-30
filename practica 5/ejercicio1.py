numero = int(input("Ingresa un numero entero: "))

resultado = 0
for i in range(numero):
    if i % 2 != 0 and resultado < numero:
        resultado += i
        print(resultado, end=", ") 