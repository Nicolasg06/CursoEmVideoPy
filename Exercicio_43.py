#Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com à tabela: -Abaixo de 18.55: Abaixo do peso/ -Entre 18,5 e 25: peso ideal/-25 até 30: sobrepeso/-30 até 40: obesidade/ -Acima de 40: obesidade mórbida

peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso /(altura ** 2)
print(f'O seu imc é de: {imc:.2f}')
if imc < 18.5:
    print('Abaixo do peso!')
elif imc <= 25:
    print('Peso ideal!')
elif imc <= 30:
    print('Sobrepeso!')
elif imc <= 40:
    print('Obesidade!')
else:
    print('Obesidade morbida!')
