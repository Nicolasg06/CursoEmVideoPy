#Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão aritimetica.
primeiro =int(input('Digite o primeiro termo: '))
raz = int(input('Difite a razão: '))
decimo = primeiro + (10-1) * raz
for c in range(primeiro,decimo+raz,raz):
    print(f'{c}', end='->')