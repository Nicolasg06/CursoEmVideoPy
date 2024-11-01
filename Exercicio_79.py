#Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

nu= list()

while True:
    n =(int(input('Digite um número: ')))
    if n not in nu:
        nu.append(n)
    else:
        print('Valor duplicado!')

    resp = (str(input('Deseja continuar? [S/N]'))).strip().upper()[0]
    if resp in 'Nn':
        break
print(f'Esses são os valores da lista: {sorted(nu)}')

