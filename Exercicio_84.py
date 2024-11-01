#Faça um programa que leia nome e peso de várias pessoas,guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.

temp= list()
pessoas = list()
leve = pesada = 0
while True:
    temp.append(str(input('Digite seu nome: ')))
    temp.append(float(input('Digite seu peso: ')))
    if len(pessoas) == 0:
        leve = pesada = temp[1]
    else:
        if temp[1] < leve:
            leve = temp[1]
        if temp[1] > pesada:
            pesada=temp[1]
    pessoas.append(temp[:])
    temp.clear()
    resp = str(input('Deseja continuar? [S/N]: '))
    if resp in 'Nn':
        break
print(f'Foram cadastradas {len(pessoas)} pessoas.')
print(f'O maior peso foi {pesada}KG. Peso de  ', end=' ')
for p in pessoas:
    if p[1] == pesada:
        print(f'{[p[0]]}', end='')
print()
print(f'O menor peso foi {leve}KG. Peso de ', end=' ')
for p in pessoas:
    if p[1] == leve:
        print(f'{[p[0]]}', end='')
