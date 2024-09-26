#Refaça o desafio 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triangulo será formado: -Equilátero: todos os lados iguais/ -isosceles: dois lados iguais/ -Escaleno: todos os lados diferentes.
t1 = float(input('Digite o primeiro lado triangulo: '))
t2 = float(input('Digite o segundo lado do triangulo: '))
t3 = float(input('Digite o terceiro lado do triangulo: '))
if t1 < t2 + t3 and t2 < t1 + t3 and t3 < t1 + t2:
    print(f'O triangulo pode ser formado!')
    if t1 == t2 == t3:
        print('Esse é um triangulo equilatero')
    elif t1 == t2 or t2 == t3 or t1 == t3:
        print('Triangulo isoceles')
    elif t1 != t2 != t3 != t1:
        print('Triangulo Escaleno')

else:
    print('O triangulo nao pode ser formado!')
