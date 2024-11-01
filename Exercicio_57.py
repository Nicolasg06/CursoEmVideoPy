#Faça um programa que leia o sexo de uma pessoa, mas só aceite valores "m" ou "f". caso estea errado peça a digitação novamente ate ter um valor correto.
sexo = str(input('Informe seu sexo: [M/F] ')).upper().strip()
while sexo not in 'MF':
    sexo = str(input('Dados invalidos, informe seu sexo [M/F]')).upper()
print(f'Sexo {sexo} registrado com sucesso!')