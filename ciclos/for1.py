palabra = input("Ingresa una palabra: ")

contadorVocales = 0

for letra in palabra: 
    if letra.lower() in "aeiou":
        contadorVocales += 1
print(f"La palabra '{palabra}' tiene {contadorVocales} vocal(es)")
