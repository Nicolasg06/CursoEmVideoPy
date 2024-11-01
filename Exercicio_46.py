#Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifícios, indo de 10 até, com 1s de pausa entre eles.
from time import sleep

for c in range(10,-1 ,-1):

  sleep(1)
  print(c)

print('*'*20)