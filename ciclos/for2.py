#Este programa va a calcular la suma de los numeros pares del 1 al 10

suma = 0
for num in range(1,11):
    if num % 2 == 0:
        suma += num
        
print(f"La suma de los números pares del 1 al 10 es: {suma}")    