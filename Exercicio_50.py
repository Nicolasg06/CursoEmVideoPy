#Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado foi ímpar, desconsidere.
soma=0
cont=0
for c in range(1,7):
    num=int(input(f'Digite o {c} numero: '))
    if num % 2 == 0 :
        soma= soma + num
        cont += 1
print(f'Você digitou {cont} números pares e a soma é: {soma}')