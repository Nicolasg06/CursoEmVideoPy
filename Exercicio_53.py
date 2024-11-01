#Leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.

pali = str(input('Digite uma frase: ')).strip().upper()
palavras = pali.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) -1, -1,-1):
    inverso += junto[letra]
if inverso == junto:
    print(f'Temos um palíndromo!\n {pali,inverso} ')
else:
    print(f'A frase "{pali}" não é um palíndromo!')
