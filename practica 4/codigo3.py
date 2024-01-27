edad = int(input("Ingresa la edad del cliente: "))

if edad < 4:
    print("Entra gratis")
elif edad > 3 and edad < 18: 
    print("Debe pagar $110 pesos.")
else:
    print("De paga $190 pesos")