import random

def valida_int(pergunta, min, max):
    x = int(input(pergunta))
    while ((x < min) or (x > max)):
        x = int(input(pergunta))
    return x

def vencedor(jogador1, jogador2):
    global empate,v1,v2
    if jogador1 == 1: #jogador 1 jogou pedra
        if jogador2 == 1: #jgoador 2 jogou pedra
            empate += 1
        elif jogador2 == 2: #jogador 2 jogou papel
            v2 += 1
        elif jogador2 == 3: #jogador 2 jogou tesoura
            v1 += 1
    elif jogador1 == 2: #jogador 1 jogou papel
        if jogador2 == 1: #jogador 2 jogou pedra
            v1 += 1
        elif jogador2 == 2: #jogador 2 jogou pedra
            empate += 1
        elif jogador2 == 3: #tesoura
            v2 += 1
    elif jogador1 == 3: #jogador 1 jogou tesoura
        if jogador2 == 1: #jogador 2 jogou pedra
            v2 += 1
        elif jogador2 == 2: #jogador 2 jogou papel
            v1 += 1
        elif jogador2 == 3: #jogador 2 jogou tesoura
            empate += 1

            
#programa principal
print('JOKENPO')
print('1 - Pedra')
print('2 - Papel')
print('3 - Tesoura')

resultados = []
jogadas = []
v1 = 0
v2 = 0
empate = 0

while True:
    j1 = valida_int('Escolha um numero: ', 0, 3)
    if not j1:
        break
    j2 = random.randint(1,3)
    jogadas.append([j1, j2])