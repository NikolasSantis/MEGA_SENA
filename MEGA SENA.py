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
    for k in range(0,6):
        t.append(randint(0,60))
    t.sort()
    jogos.append(t[:])
    t.clear()
    print(f'Jogo {c+1}: {jogos[c]}')
print('--'*21)
print(f'{"  BOA SORTE!  ":=^42}')
