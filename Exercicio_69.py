#Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa
# cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
c = h = m = mu = 0

while True:
    idade = int(input('Digite sua idade: '))
    sexo=' '
    while sexo not in 'MF':
     sexo = str(input('Digite o seu sexo [M/F]: ')).strip().upper()[0]
    resp = ' '
    while resp not in 'SN':
        resp= str(input('Quer continuar? [S/N] ')).strip().upper()[0]


    if sexo == 'M':
        h+=1
        c +=1
    if idade <20 and sexo == 'F':
       mu += 1
       c += 1
    if idade >=18:
        c += 1
    if resp == 'N':
        break
print(f'{c}\n{h}\n{m}\n{mu}')
