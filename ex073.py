times = ('Atlético-MG', 'Internacional', 'São Paulo', 'Palmeiras', 'Vasco da Gama', 'Flamengo', 'Santos', 'Fortaleza', 'Fluminense', 'Sport Recife', 'Ceará SC', 'Grêmio', 'Corinthians', 'Atlético-PR', 'Coritiba', 'Bragantino-SP', 'Botafogo', 'Bahia', 'Goiás')
print(f"Os cinco primeiros colocados são: \n{times[:5]}")
print('=-='*20)
print(f"Os cinco últimos colocados são: \n{times[-5:]}")
print('=-='*20)
print(f"Os times em ordem alfabética: {sorted(times)}")
print('=-='*20)
print(f"O Flamengo está na {times.index('Flamengo')}º posição")
