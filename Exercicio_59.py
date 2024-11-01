#Crie um programa que leia 2 valores e mostre um menu na tela: 1somar/ 2multiplicar/ 3 maior/ 4 novos numeros/ 5 sair do prgrama//  o programa devara ralizar a operação solicitada em cada caso.

num1 = int(input('Digite o primeiro valor: '))
num2 = int(input('Digite o segundo valor: '))

op = 0
while op !=5:
    print('[1] SOMAR \n[2] MULTIPLICAR\n[3] MAIOR\n[4]NOVOS NÚMEROS\n[5] SAIR DO PROGRAMA')
    op = int(input('Qual sua opção? '))
    if op == 1:
        soma= num1 + num2
        print(soma)
        print('=-='*10)
    elif op == 2:
        multiplicar = num1 * num2
        print(multiplicar)
        print('=-=' * 10)
    elif op == 3:
        maior = max(num1,num2)
        print(maior)
        print('=-=' * 10)
    elif op == 4:
        num1= int(input('Digite o primeiro valor:'))
        num2= int(input('Digite o segundo valor'))
        print('=-=' * 10)
    elif op == 5:
        print('Finalizando')
        print('=-=' * 10)
    else:
        print('Opção invalida, tente novamente! ')
print('Fim do programa')

