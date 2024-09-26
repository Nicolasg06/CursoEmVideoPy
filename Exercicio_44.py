#Calcule o valor a ser pago por um produto, preço normal e condição de pagamento: -À vista dinheiro/pix: 10% de desconto// -À vista no cartão: 5% de desconto// -Em até 2x no cartão: preço normal//-3x ou mais no cartão: 20% de juros.
from wsgiref.validate import validator
print(f'{" LOJAS GOULART ":=^40} ')
produto = float(input('Digite o valor do produto:'))
print('Informe a forma de pagamento: \n[1] DINHEIRO/PIX \n[2] À VISTA NO CARTÃO \n[3] 2X NO CARTÃO \n[4] 3X OU MAIS NO CARTÃO ')
opcao = input('Digite:')
if opcao == '1':
    valor = produto - (produto * 10 / 100)
    print(f'O valor do produto R${produto}, será de R${valor} com 10% de desconto.')
elif opcao =='2':
    valor = produto - (produto * 5 / 100)
    print(f'O valor do produto R${produto}, será de R${valor} com 5% de desconto.')
elif opcao == '3':
    print(f'O total é de R${produto} !')
elif opcao == '4':
    valor = produto + (produto * 20 / 100)
    print(f'O valor do produto R${produto}, será de {valor} com 20% de juros!')
else:
    print('Opção invalida!')