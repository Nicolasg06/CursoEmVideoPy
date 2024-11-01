#Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci.
num = int(input('Digite um número: '))
f = 0
fa = 1
cont = 3
print(f'{f}->{fa}->', end='')
while  cont <= num:
    soma = f + fa
    f = fa
    fa = soma
    print(f'{soma}->',end='')
    cont +=1
print('fim')