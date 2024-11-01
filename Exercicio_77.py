#Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
# Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
cont=0
palavras =  ('aranha','quinze','definir','dureza','oriental','caravana','caricatura','lábios','demente','nota')
for vogais in palavras:
    print(f'\nNa palavra {vogais} temos: ', end='')
    for letra in vogais:
        if letra.lower() in 'aeiou':
            print(f'{letra}', end=',')
