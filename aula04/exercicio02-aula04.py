valor = int(input('Digite um valor: '))
nota100 = 0
nota50 = 0
nota20 = 0
nota10 = 0
nota5 = 0
nota1 = 0
while valor > 0:
    if valor >= 100:
        valor -= 100
        nota100 +=1
    elif valor >= 50:
        valor -= 50
        nota50 += 1
    elif valor >= 20:
        valor -= 20
        nota20 += 1
    elif valor >= 10:
        valor -= 10
        nota10 = 1
    elif valor >= 5:
        valor -= 5
        nota5 += 1
    elif valor >= 1:
        valor -= 1
        nota1 += 1
print('Notas de 100: {}'.format(nota100))
print('Notas de 50: {}'.format(nota50))
print('Notas de 20: {}'.format(nota20))
print('Notas de 10: {}'.format(nota10))
print('Notas de 5: {}'.format(nota5))
print('Notas de 1: {}'.format(nota1))