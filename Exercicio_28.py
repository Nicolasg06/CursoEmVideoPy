# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador, o programa deverá escrever na tela se o usuário venceu ou perdeu.

import random

num = random.randint(0,5)
usu = int(input('Digite um nuúmero de 0 à 5: '))

if usu == num:
    print(f'Você acertou, o número é: {num}')
else:
    print(f'Você errou, o número certo é: {num}')