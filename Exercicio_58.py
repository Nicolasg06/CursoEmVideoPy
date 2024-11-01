#Melhore o jogo do desafio 28 onde o computador vai pensar em um numero entre 0 e 10. só que agora o jogador vai tentar adivinhar até acertar. mostrando no final quantos palpiter foram necessarios para vencer.

import random


pc = random.randint (0,10)
cont = 0
acertou = False
while not acertou:
    num = int(input('Digite um número: '))
    cont +=1
    if num == pc:
        acertou = True
    else:
        if num < pc:
            print('Errou, o numero é maior.')
        else:
            print('o numero é menor')
print(f'Você tentou {cont} vezes e acertou o numero {pc}')