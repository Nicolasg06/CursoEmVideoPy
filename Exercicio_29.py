#Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$ 7,00 por cada KM acima do limite.

vel = float(input('Informe a velocidade do carro: '))
lim = 80
mul = (vel-80) * 7
if vel > lim:
    print(f'Você ultrapassou o limite de velocidade de 80KM/h e vai pagar R${mul} de multa.')
else:
    print('Velocidade normal da via!')