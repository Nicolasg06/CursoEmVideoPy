# import math
# # Importa todas as funcionalidade da biblioteca
# num=int(input('Digite um número: '))
# raiz = math.sqrt(num)
# print(f'A raiz de {num} é igual a: {raiz}')
#
# from math import sqrt,floor
# # Importa apenas as funcionalidades especificas.
# num2=int(input('Digite um número: '))
# raiz = sqrt(num2)
# print(f'A raiz de {num2} é igual a: {floor(raiz)}')

# import random
# # gera numeros aleatorios
# # random.randint gera um numero aleatorio de 1 a 10
# num3 = random.random()
# num4 = random.randint(1,10)
# print(f'{num3}, \n {num4}')

# import math ##exercicio16
# num=float(input('Digite um numero real: '))
# print(f'O número real tranformado em inteiro é igual a: {int(num)}')

# #trianguloRetangulo ##exe17
# import math
# comp=float(input('Digite o comprimento do cateto oposto: '))
# comp2 = float(input('Digite o comprimento do cateto adjacente: '))
# hipotenusa= math.hypot(comp,comp2) # (comp ** 2 + comp2 **2) ** (1/2) Formula matematica
#
# print(f'O valor da hipotenusa é: {hipotenusa:.2f}')

# import math #exe18 seno cosseno tangente
# num=float(input('Digite um angulo: '))
# seno= math.sin(math.radians(num))
# cosseno = math.cos(math.radians(num))
# tangente = math.tan(math.radians(num))
# print(f'O angulo de {num} tem o seno de:{seno :.2f} \nO cosseno de: {cosseno:.2f} \nE a tangente de {tangente:.2f}')

# import random #exe19
# a1 = str(input('Insira seu nome: '))
# a2 = str(input('Insira seu nome: '))
# a3 = str(input('Insira seu nome: '))
# a4 = str(input('Insira seu nome: '))
# lista = [a1, a2, a3, a4]
# print(f'O aluno sorteado foi: {random.choice(lista)}')

# from random import shuffle #exe20
# n1 =str(input('Digite seu nome: '))
# n2 = str(input('Digite seu nome: '))
# n3 = str(input('Digite seu nome: '))
# n4 = str(input('Digite seu nome: '))
# lista= [n1, n2, n3, n4]
# print(f'A ordem da lista será: {shuffle(lista)} {lista}')

import pygame
pygame.init()
pygame.mixer.music.load('SOMDESPERTADOR.mp3')
pygame.mixer.music.play()

