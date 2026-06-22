'''
Programa que identifica se um numero esta na composição algaritmica de outro maior
'''

while True:
    try:
        maior = int(input("insira um número grande: "))
        menor = int(input("insira um número menor que o anterior: "))

        if len(str(maior)) > len(str(menor)):
            break
        else:
            print("\nO número grande deve ter mais dígitos que o número seguinte!\n")
    except:
            print("\nInsira números inteiros somente!")


maior_str = str(maior)
menor_str = str(menor)

if menor_str in maior_str:
    print("O número", menor, "é um subnúmero de:", maior)
else:
    print("O número", menor, "não é um subnúmero de:", maior)