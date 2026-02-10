# 10_02_2026 py.prog04: classifica numeros de uma lista como par ou impar
# por yuuuchua

def par_ou_impar(n):
    if n % 2 == 0:
        return "par"
    else:
        return "ímpar"

n = int(input("Digite o número: "))

for i in range(1, 1+n):
    print(i, "é", par_ou_impar(i))