#programa principal
cadastro = {}
listadeNomes = []
listaNascimento = []
listaSexo = []
cont = 0
idade = 0
mediaIdade = 0

while True:
    listadeNomes.append(input('Digite um nome para o cadastro: '))
    listaNascimento.append(int(input('Digite o ano do nascimento: ')))
    listaSexo.append(input('Digite o sexo dessa pessoa: '))
    continuacao = input('Quer continuar? ')
    idade = 2022 - listaNascimento[-1]
    mediaIdade += idade
    cont += 1
    if continuacao != 'sim':
        break
cadastro['nomes'] = listadeNomes
cadastro['nascimento'] = listaNascimento
cadastro['sexo'] = listaSexo
for i in listaNascimento:
    
mediaIdade /= cont
print(cadastro)
print('Total de pessoas cadastradas: {}'.format(cont))
print('Media de idade das pessoas: {}'.format(mediaIdade))


