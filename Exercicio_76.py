lista = ('Lapis', 1.70,'borracha', 1.50, 'Caderno', 15, 'Papel A4', 7.90,
         'Mochila',120)
print('-'*40)
print(f'{"LISTAGEM DE PREÇO":^40}')
print('-'*40)
for pos in range(0, len(lista)):
    if pos % 2 == 0:
        print(f'{lista[pos]:.<32}', end='')
    else:
        print(f'R$ {lista[pos]:>7.2f}')