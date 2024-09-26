#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triangulo.

t1 = float(input('Digite o primeiro lado triangulo: '))
t2 = float(input('Digite o segundo lado do triangulo: '))
t3 = float(input('Digite o terceiro lado do triangulo: '))
if t1 < t2 + t3 and t2 < t1 + t3 and t3 < t1 + t2:
    print(f'{'\033[4;31;46m'}O triangulo pode ser formado!')
else:
    print('O triangulo nao pode ser formado!')
