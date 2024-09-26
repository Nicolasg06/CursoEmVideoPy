#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar. Calcule o valor mensal da prestação sabendo que ela nao pode exceder 30% do salário ou então o empréstimo será negado.

salario = float(input('Digite o valor do seu salário: '))
casa = float(input('Digite o valor da casa: '))
tempo = int(input('Em quantos anos pretende realizar o pagamento? '))
prestacao = casa / (tempo * 12)
min = salario * 30 / 100
if prestacao > min:
     print('O valor da prestação é maior que 30% do seu salario, emprestimo negado!')
else:
    print(f'Empréstimo aprovado, o valor da sua prestação sera de R${prestacao:.2f}')

