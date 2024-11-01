#Crie um programa que vai ler vários números e colocar em uma lista.                  Depois disso, mostre:                                                                                                                                                A) Quantos números foram digitados.                                                                                                                    B) A lista de valores, ordenada de forma decrescente.                                                                                          C) Se o valor 5 foi digitado e está ou não na lista.

lista=[]
while True:
    lista.append(int(input('Digite um valor: ')))

    resp = str(input('Deseja continuar? [S/N]'))
    if resp in 'Nn':
        break


print(f'Voce digitou {len(lista)} números')
lista.sort(reverse=True)
print(f'Os números em ordem decrescente são: {lista}')
if 5 in lista:
    print('O numero "5" está na lista.')
else:
    print('O numero "5" não está na lista.')