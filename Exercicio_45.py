#Cire um programa que faça o computador jogar jokenpô.
import random
from random import randint
from time import sleep
print('Escolha:\n[0]PEDRA\n[1]PAPEL\n[2]TESOURA ')
mao = int(input('Qual a sua jogada? '))
print('JO')
sleep(1)
print('KEM')
sleep(1)
print('PÔ')
sleep(1)
itens = ('Pedra', 'Papel','Tesoura')
pc = randint(0,2)
print('-='*16)
print(f'O computador escolheu: {itens[pc]}')
print(f'O jogador escolheu: {itens[mao]}')
print('-='*16)
if pc == 0:
    if mao == 0:
        print('Empate')
    elif mao ==1:
        print('Jogador ganhou!')
    elif mao == 2:
        print('PC ganhou')
    else:
        print('JOGADA INVALIDA')
if pc == 1:
    if mao == 0:
        print('PC Ganhou')
    elif mao ==1:
        print('Empate!')
    elif mao == 2:
        print('Jogador ganhou')
    else:
        print('JOGADA INVALIDA')
if pc == 2:
    if mao == 0:
        print('Jogador ganhou')
    elif mao ==1:
        print('PC ganhou!')
    elif mao == 2:
        print('Empate!')
    else:
        print('JOGADA INVALIDA')

