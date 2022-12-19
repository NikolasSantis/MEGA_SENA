from random import randint
from time import sleep
print('--'*21)
print(f'{"JOGO DA MEGA SENA":^42}')
print('--'*21)
tot = int(input('Jogos a seres feitos: '))
print(f'\n {"SORTEANDO NUMEROS":-^42}')
jogos = []
t = [] 
for c in range(0, tot):
    while len(t) <= 5:
        aju = randint(0,60)
        if aju not in t:
            t.append(aju)
    t.sort()
    jogos.append(t[:])
    t.clear()
    sleep(0.7)
    print(f'Jogo {c+1}: {jogos[c]}')
print('--'*21)
print(f'{"  BOA SORTE!  ":=^42}')