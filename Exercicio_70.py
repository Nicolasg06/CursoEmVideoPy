#Crie um programa que leia o nome e o preço de vários produtos. O programa deverá
# perguntar se o usuário vai continuar ou não. No final, mostre: A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.

total = mil = menor = cont =  0
barato =''
while True:

    nome = str(input('Digite o nome do produto: '))
    preco = float(input('Digite o valor do produto: R$'))
    total += preco

    if preco > 1000:
        mil += 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = nome
    resp = ' '
    while resp not in "SN":
        resp = str(input('Quer continuar [S/N]')).strip().upper()
    if resp == 'N':
         break

print(f'{"FIM DO PROGRAMA":*^40} ')
print(f'O valor total da compra é: R${total:.2f}')
print(f'Temos o  total de {mil} produto(s) que custam mais de Mil Reais.')
print(f'O produto mais barato foi "{nome}" e o seu preço é: R${preco:.2f}')