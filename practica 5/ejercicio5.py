frase = input("Ingresa una frase")
letra = input("Ingresa una vocal")

contadorLetra = 0

for letra in frase:
    if letra.lower() in letra:
        
        contadorLetra += 1
print(f"La frase '{frase}' tiene {contadorLetra} letra(s)")