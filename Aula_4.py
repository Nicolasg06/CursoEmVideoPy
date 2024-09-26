#condicoes

# nome = str(input('Qual seu nome? ')).strip()
# if nome == 'Nicolas':
#     print('Que nome lindo!')
#     print(f'Bom dia,{nome}!')
# else:
#     print('Seu nome é tão normal.')
#     print(f'Bom dia,{nome}!')

n1 = float(input('Digite a primeiria nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1+n2)/2
print(f'A sua nota média foi {m:.1f}')
if m >= 6.0:
    print('Sua média foi boa! PARABÉNS')
else:
    print('Sua média foi ruim! ESTUDE MAIS')
