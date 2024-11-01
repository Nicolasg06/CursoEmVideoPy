#Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
lista = []
for c in range(0,5):
    lista.append(int(input('Digite um valor: ')))

print(f'Os valores da lista são: {lista}')
print(f'Maior valor é: {max(lista)}, nas posições: ',end=' ')
for i,v in enumerate(lista):
    if v==max(lista):
        print(f'{i}...',end=' ')
print()
print(f'Menor valor é: {min(lista)}, nas posições: ',end=' ')
for i,v in enumerate(lista):
    if v==min(lista):
        print(f'{i}...',end=' ')
