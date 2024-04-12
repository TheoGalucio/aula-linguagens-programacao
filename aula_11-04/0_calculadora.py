valor1 = float(input())
operador = input()
valor2 = float(input())

while valor1 != -1 and operador != "-1" and valor2 != -1:

    if operador == '+':
        resultado = valor1 + valor2
        print(resultado)
    elif operador == '-':
        resultado = valor1 - valor2
        print(resultado)
    elif operador == '*':
        resultado = valor1 * valor2
        print(resultado)
    elif operador == '/':
        if valor2 != 0:
            resultado = valor1 / valor2
            print(resultado)
        else:
            print("Erro: Divisão por zero.")
    else:
        print('Operador inválido!')

    valor1 = float(input())
    operador = input()
    valor2 = float(input())

print("Programa encerrado.")
