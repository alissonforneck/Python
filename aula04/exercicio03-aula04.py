ingresso = 0
quantidadeIngressos = 0
mediaIdade = 0
while True:
    idade=input('Digite a sua idade: ')
    if idade == 'sair':
        break
    idade = int(idade)
    if idade > 3:
        ingresso += 15
    elif idade > 12:
        ingresso += 30
    mediaIdade += idade
    quantidadeIngressos += 1
mediaIdade /= quantidadeIngressos
print('Quantidade de ingressos vendidos: {}'.format(quantidadeIngressos))
print('Dinheiro arrecadado: {}'.format(ingresso))
print('Media de idade das pessoas que compraram os ingressos: {}'.format(mediaIdade))
