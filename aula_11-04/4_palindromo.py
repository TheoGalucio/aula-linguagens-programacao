texto = str(input("Digite um texto: ")).strip()
texto_invertido = ''.join(caracter.lower() for caracter in texto if caracter.isalnum())
inverso = texto_invertido[::-1]
if inverso == texto_invertido:
    print("É um palíndromo!")
else:
    print("Não é um palíndromo.")
