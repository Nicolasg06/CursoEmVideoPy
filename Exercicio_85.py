#Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.

lista = [[],[]]
valor = 0
for c in range(0,7):
    valor = (int(input('Digite um valor: ')))
    if valor % 2 == 0:
        lista[0].append(valor)
    else:
        lista[1].append(valor)
print(f'Os valores pares digitados foram {sorted(lista[0])}')
print(f'Os valores ímpares digitados foram {sorted(lista[1])}')