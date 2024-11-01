#faça um programa que leia um numero qualquer e mostre o seu fatorial. Ex 5!=5x4x3x2x1=120
from math import factorial

num = int(input('Digite um número: '))
c = num
f = 1
print(f'Calculando {num}!: ',end='')
while c > 0:
    print(f'{c}',end='')
    print(f'x' if c > 1 else'=', end='')
    f*=c
    c-=1
print(f)
