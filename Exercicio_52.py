# Faça um programa que leia um número inteiro e diga se ele é ou nao um número primo.
num = int(input('Digite um número: '))
cont=0
for c in range(1, num+1):
    if num % c == 0:
        print('\033[33m', end='')
        cont += 1
    else:
        print('\033[34m',end='')
    print(f'{c}', end=' ')
print(f'\n\033[m0 número {num} foi divisivel por {cont} vezes.')
if cont == 2:
    print('Por isso ele é um número primo!')
else:
    print('Por isso ele não é um número primo!')