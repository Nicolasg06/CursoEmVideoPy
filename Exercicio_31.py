#Desenvolva um programa que pergunta a distância de uma viagem em KM. Calcule o preço da passagem, cobrando R$ 0,50 por km para viagens até 200km e R$ 0,45 para viagens mais longas.

km = float(input('Insira a distancia em KM da sua viagem: '))
if km <= 200:
    var = km * 0.50
    print(f'O valor total da sua viagem é R${var:.2f}')
else:
    var = km * 0.45
    print(f'O valor da sua viagem é R${var:.2f}')