# 10_02_2026 py.prog06: mini calculadora com quatro operações, agora com loop
# por yuuuchua

def soma(num1, num2):
    return num1 + num2

def subtracao(num1, num2):
    return num1 - num2

def multiplicacao(num1, num2):
    return num1 * num2

def divisao(num1, num2):
    if num2 == 0:
        return "Não é possível dividir por zero"
    return num1 / num2

def calculadora():
    while True:
      
     print("Escolha a operação: \n 1 - Soma \n 2 - Subtração \n 3 - Multiplicação \n 4 - Divisão \n 0 - Sair")

     operacao = input("Digite a operação: ")

     if operacao == "0":
         print("Saindo...")
         break
     
     if operacao not in ["1", "2", "3", "4"]:
         print("Operação inválida, tente novamente!")
         continue
     
     num1 = float(input("Digite o primeiro número: "))
     num2 = float(input("Digite o segundo número: "))

     if operacao == "1":
        resultado = soma(num1, num2)
     elif operacao == "2":
        resultado = subtracao(num1, num2)
     elif operacao == "3":
        resultado = multiplicacao(num1, num2)
     elif operacao == "4":
        resultado = divisao(num1, num2)
    
     print(f"O resultado será: {resultado}")


calculadora()
