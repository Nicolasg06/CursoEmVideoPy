#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade: -Se ele ainda vai se alistar./ -Se é a hora de se alistar./ -Se já passou do tempo do alistamento.// Mostre o tempo que falta ou que passou do prazo.
import datetime
sexo =input('Digite seu sexo: [1] para mulher  ou [2] para homem:')
if sexo == '1':
    print('Você não precisa se alistar.')
elif sexo == '2':
    ano = int(input('Digite seu ano de nascimento:'))
    idade = datetime.date.today().year - ano
    if idade == 18:
        print('Esta na hora de se alistar.')
    elif idade > 18:
     print(f'Já se passaram {idade-18} anos, você deveria ter se alistado. ')
    elif idade < 18:
        print(f"Ainda faltam {18-idade} para você se alistar")