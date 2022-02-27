quantidade = float(input('Quantos kWh você consumiu? '))
print('Existem 3 tipos de instalções de energia.')
print('Tipo R : para instalações residenciais')
print('Tipo I: para instalações indústriais')
print('Tipo C: para instalaçoes comerciais')
tipo = input('Qual o tipo de instalação você utiliza? ')
if(tipo == 'R' or tipo == 'r'):
    if (quantidade <= 500):
        preco = quantidade * 0.40
    elif(quantidade > 500):
        preco = quantidade * 0.65
elif(tipo == 'C' or tipo == 'c'):
    if(quantidade <= 1000):
        preco = quantidade * 0.55
    elif(quantidade <= 5000):
        preco = quantidade * 0.60
elif(tipo == 'I' or tipo == 'i'):
    if(quantidade <= 5000):
        preco = quantidade * 0.55
    else:
        preco = quantidade * 0.60
else:
    print('Instalação invalida')
print('Voce utiliza a instalação do tipo {} e por isso precisa pagar {}'.format(tipo,preco))