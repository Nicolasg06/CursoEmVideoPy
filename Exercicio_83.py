expr = str(input('Digite sua expressão: '))
pilha =[]
for simb in expr:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        pilha.append(')')
if len(pilha) % 2 == 0:
    print('Sua expressão está correta!')
else:
    print('Sua expressão está incorreta!')