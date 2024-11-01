#melhore o desafio 61, perguntando se ele quer mostrar mais alguns termos, o programa encerra quando ele dizer 0

primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
     total += mais
     while cont <= total:
        print(f'{termo}->', end='')
        termo += primeiro
        cont += 1
     print('Pausa')
     mais = int(input('Quantos termos você quer ver mais? '))
print(f'Foram mostrado {total} termos')


