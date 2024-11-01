#Leia varios numeros inteiros, no final mostre a media entre todos os valores e qual foi o maior e o menor valor lido. o prgrama deve perguntar se ele quer ou nao conntinuar a digitar valores
resp = 'S'
soma = cont = maior = menor =0
while resp in 'S':
    num = int(input('Digite um número: '))
    soma += num
    cont += 1
    if cont == 1:
        maior=num
        menor=num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('Deseja continuar [S,N]')).strip().upper()[0]
media = soma / cont
print(f'{cont}\n{media}\n{maior}\n{menor}',end='')