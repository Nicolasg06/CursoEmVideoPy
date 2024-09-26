#
# frase =str(input('insira seu cpf: '))
#
# # print(int(frase[3:6]))
# print (frase.replace('1','*'))
# print(frase[0:6])
# print(frase.count('1'))
# print(frase[::5])
# print(frase[2::])
# print(frase[1:12:2])
# print(len(frase))
# print(frase.split())
from os.path import split

# nome = str(input('Qual o seu nome completo?: ')).strip()
# print('Seu nome Maiusculo é: ', nome.upper())
# print('Seu nome minusculo é: ',nome.lower())
# print('Seu nome tem ao todo', len(nome)-nome.count(' '), 'letras.')
# print('Seu primeito nome tem', nome.find(' '), 'letras.')
# separa= nome.split()
# print(f'Seu primeiro nome é {separa[0]} e ele tem {len(separa[0])} letras.')
# # cidade = str(input('Digite o nome da sua cidade: '))
# # print(cidade.find('Santo'))

# num= int(input('Digite um numero de 0 a 9999: '))
# u = num // 1 % 10
# d = num // 10 % 10
# c = num // 100 % 10
# m = num // 1000 % 10
# print(f'Uniddade: {u}')
# print(f'Dezena: {d}')
# print(f'Centena: {c}')
# print(f'Milhar: {m}')

# cid = str(input('Digite o nome da cidade que você nasceu: ')).strip()
# print(cid[:5].lower() == 'santo')

# nome = str(input('Digite seu nome: ')).strip()
# print(f'Seu nome tem SILVA?' , 'silva' in nome.lower())

# frase = str(input('Digite uma frase: ')).strip()
# frase = frase.lower()
# print(f'A letra (A) aparece {frase.count('a')} vezes.')
# print(f'A primeira letra (A) aparece na posição {frase.find('a')+1}')
# print(f'A ultima letra (A) aparece na posição {frase.rfind('a')+1}')

# n = str(input('Digite seu nome completo: '))
# nome = n.split()
# print(f'Seu primeiro nome é "{nome[0]}" e o ultimo é "{nome[len(nome)-1]}"')