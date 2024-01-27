text = input("Ingresa unos caracteres:")

textInvertido = text[::-1] 

if text == textInvertido:
    print("Es palindromo")
else:
    print("No es palindromo")