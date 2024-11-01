#Refaça o desafio 51, lendo o primeiro termo e a razao de uma pa, mostrando os 10 primeiros termos usando a estrutura while

primeiro = int(input('Digite o primeiro numero: '))
razao = int(input('Digite a razão: '))
termo = primeiro
cont = 1
while cont <= 10:
    print(f'{termo}->', end='' )
    termo += primeiro
    cont += 1
