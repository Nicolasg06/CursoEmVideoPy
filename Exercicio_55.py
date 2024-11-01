#Faça um programa que leia o peso de 5 pessoas. No final, mostre qual foi o maior e o menor peso lido.
maior = 0
menor = 0
for c in range(1,6):
    peso = float(input(f'Digite seu {c} peso: '))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior  = peso
        if peso < menor:
            menor = peso

print(f'O mais pessado foi o de {maior} KG \nO mais leve foi o de {menor} KG')