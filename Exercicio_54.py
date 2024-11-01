#Leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda nao atingiram a maioridade e quantas já são maiores.
import datetime
conta=0
cont=0
for c in range(0,7):
    ano = int(input('Digite seu ano de nascimento: '))
    idade = datetime.date.today().year - ano
    if idade >= 18:
        print(f'Já atingiu maior idade!')
        conta+=1

    else:
        print('Não')
        cont+=1
print(f'{cont,conta}')
