#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$ 1.250,00, calcule um aumento de 10%. Para os inferiores o aumento é de 15%.

salario = float(input('Digite o seu salário: '))
if salario <= 1.250:
    aumento = (salario * 10) / 100
else:
    aumento = (salario * 15) / 100
print(f'O seu salario de R${salario:.2f} aumentou para R${aumento+salario:.2f}.')