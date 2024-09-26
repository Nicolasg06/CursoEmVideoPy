# for c in range(0,3):
#     passo
#     pula
# passo
# pega
#
# for c in range(0,3):
#     if moeda:
#         pega
#     passo
#     pula
# passo
# pega


#printa oi 6 vezes
for c in range(0,6):
    print('oi')
print('fim')

#printa c e faz uma contagem de 1 a 6
for c in range(1,7):
    print(c)
print('fim')

#printa c de traz para frente
for c in range(6,0,-1):
     print(c)
print('fim')

#printa a contagem de 2 em 2
for c in range(0,7,2):
     print(c)
print('fim')

# faz a contagem a partir de 0 e soma +1 no número que foi digitado
n = int(input('Digite um número: '))
for c in range(0, n+1):
     print(c)
print('Fim')

#faz a contagem do (inicio), pede onde será o (fim) e de quantos em quantos sera contado(passo)
i = int(input('Inicio: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range(i, f+1, p):
    print(c)
print('fim')

s = 0
for c in range(0,3):
    n = int(input('Digite um número: '))
    s += n
print(f'O somatorio de todos foi {s}')