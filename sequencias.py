'''
Programa que mostra qual a maior subsequencia crescente em uma sequencia de números inteiros
'''


while True:
    try:
        numeros = int(input("insira uma sequencia de numeros:"))
        if(len(str(numeros)) > 3 and type(numeros) == int):
            break
        else:
            print("\nInsira uma sequencia de 3 ou mais numeros inteiros\n")
    except:
        print("\nInsira numeros inteiros somente!")

lista = [int(digito) for digito in str(numeros)]
print("\nEssa é a lista resultante:")
print(lista)

sublista = []
sublista_atual = [lista[0]]

for i in range(1, len(lista)): 
    if lista[i] > lista[i-1]:
        sublista_atual.append(lista[i])
    else:
        sublista.append(sublista_atual)
        sublista_atual = [lista[i]]

sublista.append(sublista_atual)
resultado = [sublista_atual for sublista_atual in sublista if len(sublista_atual) > 1]
maior = max(resultado, key=len)

print("\nAs sequencias são essas:",resultado)
print("A maior sequencia é:", maior)
