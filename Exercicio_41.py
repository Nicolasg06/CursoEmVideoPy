# Leia o ano de nascimento de um atleta e mostre a categoria de acordo com sua idade: -Até 9 anos: Mirim/ -Até 14 anos: Infantil/ -Até 19 anos: Junior/ -Até 20 anos: Sênior/ Acima: Master.
import datetime

ano= int(input('Digite seu ano de nascimento:'))
idade= datetime.date.today().year - ano
if idade <= 9:
    print(f'Você tem {idade} anos, sua categoria é a mirim')
elif idade <= 14:
    print(f'Você tem {idade} anos, sua categoria é a infantil.')
elif 15<= idade <=19 :
    print(f'Você tem {idade} anos, sua categoria é a junior')
elif  idade <=25:
    print(f'Você tem {idade} anos, sua categoria é a senior' )
else:
    print(f'Você tem {idade} anos, sua categoria é a Master')