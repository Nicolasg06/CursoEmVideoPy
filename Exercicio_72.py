#Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por
# extenso, de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
num = ('Zero','UM', 'DOIS', 'TRêS', 'QUATRO', 'CINCO', 'SEIS', 'SETE', 'OITO',
       'NOVE', 'DEZ', 'ONZE', 'DOZE', 'TREZE', 'QUATORZE', 'QUINZE', 'DEZESSEIS', 'DEZESSETE','DEZOITO', 'DEZENOVE','VINTE')
resp ='S'
while resp in 'S':
    escolha = int(input('Digite um número de 0 à 20: '))

    if escolha <0 or escolha > 20:
        print('Número invalido, digite novamente:')

    else:
        print(f'Você digitou o número {num[escolha]}')
        resp = str(input('Você quer continuar? [S/N]')).strip().upper()[0]


