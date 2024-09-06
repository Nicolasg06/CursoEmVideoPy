num=float(input("Insira um número:"))
num2=float(input("Insira um número:"))
resp=input("Qual operação deseja realizar? (+,-,*,/)")
if resp=='+':
    resultado=num + num2
elif resp == '-':
    resultado = num - num2
elif resp == '*':
    resultado = num * num2
elif resp == '/':
    if num2!= 0:
     resultado=num/num2
    else:
     resultado="Erro: Impossivel realizar divisão por zero!"
else:
    resultado="operação invalida"
print(f"O resultado é= {resultado}")
