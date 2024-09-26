#Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1- para binário/ 2- para octal/ 3- para hexadecimal

num = int(input('Digite um número inteiro: '))
print('Digite a opção desejada: 1-para binário/ 2-para octal/ 3-para hexadecimal')
op = int(input('Sua opção:'))
if  op == 1:
     print(f'O valor {num} convertido para binario é:{bin(num)[2:]}')
elif op ==2:
    print(f'o valor {num} convertido para octal é: {oct(num)[2:]}')
elif op == 3:
    print(f'o valor {num} convertido para hexadecimal é: {hex(num)[2:]}')
else:
    print('Opção invalida!')