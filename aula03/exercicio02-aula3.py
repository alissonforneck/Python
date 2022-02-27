valor1 = int(input('Digite um valor: '))
valor2 = int(input('Digite um valor: '))
print('1 - Soma')
print('2 - Subtração')
print('3 - Multiplicação')
print('4 - Divisão')
operacao = int(input('Escolha qual operação voce deseja '))
if (operacao == 1):
    resultado = valor1 + valor2
elif (operacao == 2):
    resultado = valor1 - valor2
elif (operacao == 3):
    resultado = valor1 * valor2
elif (operacao == 4):
    resultado = valor1 / valor2
print('Resultado: {}'.format(resultado))