#Faça um programa que mostre a tabuada de vários números, um de cada vez para cada
# valor digitado pelo usuário.O programa será interrompido quando o número
# solicitado for negativo

while True:
    num = int(input('Quer ver a tabuada de outro valor? '))
    if num< 0:
        break
    for c in range (1,11):
        mult = num * c
        print(f'{num} x {c} = {mult}')

print(f'O {num} é negativo e assim encerramos o programa!')
