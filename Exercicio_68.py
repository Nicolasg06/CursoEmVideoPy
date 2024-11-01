#Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

import random
while True:
    jogador = int(input('Diga um número: '))
    pc = random.randint(0,10)
    soma = jogador + pc
    tipo =' '
    v=0
    while tipo not in 'PpIi':
        tipo = str(input('Você escolhe PAR ou ÍMPAR? ')).strip().upper()[0]
        print(f'Você jogou {jogador} e o pc {pc}, o total foi: {soma}')
    if tipo == 'P':
        if soma % 2 == 0:
            print('Você venceu!')
            v += 1
        else:
            print('Você perdeu!')
            break
    elif tipo =='I':
        if soma % 2 == 1:
            print('Você venceu!')
            v += 1
        else:
            print('Você perdeu!')
            break
    print('Vamos jogar novamente?')
print(f'Game over, você venceu {v} vezes.')