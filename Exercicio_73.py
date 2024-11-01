#Exercício Python 73: Crie uma tupla preenchida com os 20 primeiros colocados da
# Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
#a) Os 5 primeiros times.
#b) Os últimos 4 colocados.
#c) Times em ordem alfabética.
#d) Em que posição está o time do Galo.

times = ('Botafogo','Palmeiras','Fortaleza','Flamengo','São Paulo','Internacional','Bahia','Cruzeiro','Atlético-MG','Vasco','Criciúma','Grêmio','Red Bull Bragantino','Juventude','Fluminense','Vitória','Corinthians','Athletico','Cuiabá','Atlético-GO')

print(f'Os cinco primeiros times são: {times[0:5]}')
print('-='*60)
print(f'Os 4 últimos times são: {times[16:20]}')
print('-='*60)
print(f'Esses são os times em ordem alfabética{sorted(times)}')
print('-='*60)
print(f'O GALO está na {times.index("Atlético-MG")+1}° posição.')
