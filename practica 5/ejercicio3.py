numero = int(input("Ingresa el numero de la tabla que deseas conocer: "))

resultado = 0
multiplicador = 0

for i in range(numero):
    if i != numero:
        multiplicador += 1
        for num in range(multiplicador):
            if multiplicador < 11:
                resultado = i*multiplicador
    print(numero, " x ", multiplicador, "=", resultado)