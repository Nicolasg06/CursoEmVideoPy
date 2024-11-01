#Leia vario numeros inteiros, o programa so vai parar qando o ususario digitar 999, no final mostre quantos numeros foram digitados e qual foi a soma entre eles.
op = 0
cont = 0
soma = 0
op = int(input('Digite um número [999 encerra]: '))
while op != 999:
    cont +=1
    soma += op
    op = int(input('Digite um número [999 encerra]: '))

print(f'Foram digitados {cont} e a soma entre eles é: {soma}')
