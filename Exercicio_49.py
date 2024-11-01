#Refaça o exercício 9, mostrando a tabuada de um número que o usuário escolher, so que agora utilizando um laço for.

num = int(input('Digite um número: '))
for c in range(1,11):
    print(f'{num} x {num:2} = {num*c}')
