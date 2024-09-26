#Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem: -O primeiro valor é maior./ -O segundo valor é maior./ -Não existe valor maior, os dois são iguais.
n1 = int(input('Digite um valor:'))
n2 = int(input('Digite o segundo valor:'))

if n1 > n2:
    print(f'O {n1} é o maior número:')
elif n2 > n1:
    print(f'O {n2} é o maior numero')
elif n1 == n2:
    print('Os valores são iguais.')
