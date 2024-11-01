#TUPLAS

#lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')
#for c in lanche:
 #   print(c)
#for cont in range(0,len(lanche)):
  #  print(f'Eu vou comer {lanche[cont]}')
#for pos,comida in enumerate(lanche):
 #   print(f'Eu vou comer {comida} na posição {pos}')

#LISTAS
num = [2,5,9,1]
num[2] = 3 #Troca o valor da posição 2 por  "3"
num.append(7) #Adciciona o valor 7
num.sort() #coloca em ordem
#num.sort(reverse=True) #coloca na ordem reversa
num.insert(2,2) #insere o numero 0 na posição 2
num.pop() #Elimina o ultimo numero com () vazia ou escolha a posição que deseja
# excluir
if 5 in num:
    num.remove(5)
else:
    print('Nao achei o numero')

print(num)
print(f'Essa lista tem {len(num)} numeros')

valores = []
valores.append(5)
valores.append(9)
valores.append(4)
for cont in range(0,5):
    valores.append(int(input('Digite um valor: ')))
for c, v in enumerate(valores): #o enumarete mostra a posição de cada elemento
    print(f'Na posição {c} encontrei o valor {v} !')

a = [2,3,4,7]
b = a[:] #faz uma copia da lista a, mas altera apenas a lista b
b[2] = 8
print(f'lista A: {a}\nLista B: {b}')

dados = list()
dados.append('Pedro')
dados.append(25)
print(dados[0])
print(dados[1])
pessoas = list()
pessoas.append(dados[:])
print(pessoas)