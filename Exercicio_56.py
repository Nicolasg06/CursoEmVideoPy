#Desenvolva o um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa mostre: A media de idade do grupo./ Qual é o nome do homem mais velho./ Quantas mulheres tem menos de 20 anos.

somaidade = 0
media = 0
homemvelho = ''
maioridade = 0
contm = 0
for c in range(1,5):
    nome = str(input('Digite seu nome:')).strip()
    idade = int(input('Digite sua idade: '))
    sexo = int(input('Digite seu sexo ( 1 para [H], 2 para [M]): '))
    somaidade += idade
    if c == 1 and sexo == 1:
        maioridade = idade
        homemvelho = nome
    if sexo == 1 and idade > maioridade:
        maioridade = idade
        homemvelho = nome
    if sexo == 2 and idade < 20:
        contm += 1
media = somaidade / 4
print(f'A média de idade é: {media} anos.\nO homem mais velho se chama: {homemvelho} e tem {maioridade} anos.\nO numero de mulheres com menos de 20 anos é: {contm}')

