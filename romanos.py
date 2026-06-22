'''
Programa que retorna o valor em algarismos de um dado numero romano
'''

romanos_valores = {
    "I" : 1,
    "V" : 5,
    "X" : 10,
    "L" : 50,
    "C" : 100,
    "D" : 500,
    "M" : 1000
}

numeros_romanos = ("IVXLCDM")
while True:
    numeros = str(input("insira um numeral romano:"))
    numeros = numeros.upper()
    if(all(digito in numeros_romanos for digito in numeros)):
        break
    else:
        print("\nInsira numerais romanos válidos!(Os dígitos são i, v, x, l, c, d e m)")
    
print("\nO numeral em romano é esse:", numeros)

resultado = 0
i = 0

for digito in numeros:
    if (i + 1 < len(numeros) and romanos_valores[numeros[i]] < romanos_valores[numeros[i+1]]):
        resultado = resultado - romanos_valores[numeros[i]]
    else:
         resultado = resultado + romanos_valores[numeros[i]]
    i += 1

print("O número em algarismos desse numeral é:", resultado)