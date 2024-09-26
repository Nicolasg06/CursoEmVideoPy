#Crie um programa que leia duas notes de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com à média atingida: -média abaixo de 5,0:Reprovado./ -Média entre 5,0 e 6,9:Recuperação./ -Média 7,0 ou superior:Aprovado.

n1 = float(input('Digite a primeira nota: ' ))
n2 = float(input('Digite sua segunda nota: '))
media =  (n1 + n2 ) / 2

if media < 5.0:
    print(f'Reprovado, sua média foi {media}')
elif 7 > media >=5:
    print(f'Recuperação, sua media foi {media}')
else:
    print(f'Aprovado, sua media foi {media}')