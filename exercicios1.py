# #string
# msg = 'Olá Mundo'
# print(msg)
#
# #Input
# name=input('Digite seu nome: ')
# print(f'Seja bem vindo {name} !' )
#
# # Soma
# n1= int(input('Digite um número:'))
# n2= int(input('Digite um número:'))
# soma= n1+n2
# print(f'A soma dos valores é: {soma}')

#type
# a=input('Digite algo: ')
# print('Esta tudo em maiusculo?',a.isupper())
# print('So tem espaços?', a.isspace())
# print('É alfabetico?', a.isalpha())
# print('É alfanumerico?', a.isnumeric())
# print('É capitalizada', a.istitle())

# #sucessor
# n=int(input('Digite um número: '))
# print(f'O sucessor desse valor {n} é: {n+1} e o antecessor é : {n-1}')
#
# #multiplos
# n1=int(input('Digite um número: '))
# print(f'O dobro do número {n1} é: {n1*2}, o triplo é: {n1*3}, e a raiz quadrada é: {n1**(1/2)}' )
#
# media
# n2=float(input('Digite sua 1° nota: '))
# n3=float(input('Digite sua 2° nota: '))
# print(f'A media das suas notas são: {(n2+n3)/2}')

#metragem
# n4=float(input('Digite a metragem: '))
# print(f'O metro convertido para centimetros é: {n4*100:.0f}, e em milimetros é: {n4*1000:.0f}')
#
# #tabuada
# n5=int(input('Digite um número de 1 à 10: '))
# print(f'A tabuada do número {n5} é: \n {n5}*1: {n5*1}\n {n5}*2: {n5*2}\n {n5}*3: {n5*3}\n {n5}*4: {n5*4} \n {n5}*5: {n5*5} \n {n5}*6: {n5*6} \n {n5}*7: {n5*7} \n {n5}*8: {n5*8} \n {n5}*9: {n5*9}\n {n5}*10: {n5*10}')
#
# #conversão dolar
# n6=float(input('Digite o valor que você tem em sua carteira em real R$: '))
# print(f'Você pode comprar o total de US${n6/5.64} dolares.')
#
#pintura
# n7=float(input('Digite a altura da parede: '))
# n8=float(input('Digite a largura da parede: '))
# area= n7*n8
# tinta= area/2
# print(f'A área dessa parede é de: {area} e sera necessario de {tinta} litros de tinta')

# #valor
# n9=float(input('Digite o valor do produto: '))
# desconto=n9*.05
# resultado= n9-desconto
# print(f'O valor do produto com desconte é de {resultado :.2f}')

# #salario
# n10=float(input('Digite seu salário: '))
# print(f'Seu salário com aumento será de: { n10*1.15 :.3f}')

#temperatura
# c=float(input('Informe a temperatura em °c: '))
# # f=((9*c)/5)+32
# # print(f'A temperatura convertida pra °F é {f}')

#aluguel carro
# carro = int(input('Por quantos dias o carro foi alugado?: '))
# km = float(input('Qual foi a quilometragem percorrida?: '))
# valor = (carro * 60) + (km * 0.15)
# print(f'O valor total do aluguel é de : R${valor :.2f}')

a = 4**2
print(f'{a}')