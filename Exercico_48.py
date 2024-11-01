#Faça um programa que calcule a soma entre todos os números impares que sao múltiplos de 3 e que se encontrarem no intervalo de 1 até 500
soma = 0
cont = 0
for c in range(1,501,2):
    if c % 3 == 0 :
        soma = soma + c
        cont = cont + 1
print (f'A semoa de todos os "{cont}" valores solicitados é: {soma}')
