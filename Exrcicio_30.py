#Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

num = int(input('Me informe um número: '))
if num % 2 == 1 :
    print(f'O número {num} é impar.')
else:
    print(f'O número {num} é par.')
