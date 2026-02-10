# 10_02_2026 py.prog05: mini calculadora com quatro operações
# por yuuuchua

print("Escolha a operação: \n 1 - Soma \n 2 - Subtração \n 3 - Multiplicação \n 4 - Divisão")

operacao = int(input("Digite a operação: "))
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

def soma(num1, num2):
    return num1 + num2

def subtracao(num1, num2):
    return num1 - num2

def multiplicacao(num1, num2):
    return num1 * num2

def divisao(num1, num2):
    return num1 / num2

if operacao == 1:
    resultado = soma(num1, num2)
elif operacao == 2:
    resultado = subtracao(num1, num2)
elif operacao == 3:
    resultado = multiplicacao(num1, num2)
elif operacao == 4:
    if num2 == 0:
        print("Não é possível dividir por zero")
    else:
        resultado = divisao(num1, num2)

if resultado is not None:
    print("O resultado será", resultado)