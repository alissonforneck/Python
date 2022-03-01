while True:
    valor1 = int(input('Digite o primeiro valor: '))
    valor2 = int(input('Digite o segundo valor: '))
    operacao = input('Qual a operação você deseja? ')
    if operacao == '+':
        print('Resultado: ',valor1 + valor2)
        continue
    elif operacao == '-':
        print('Resultado: ',valor1 - valor2)
        continue
    elif operacao == '*' or operacao == 'x':
        print('Resultado: ',valor1 * valor2)
        continue
    elif operacao == '/' or operacao == 'divisao':
        print('Resultado: ', valor1 / valor2)
        continue
    elif operacao == 'sair':
        print('Voce optou por sair.')
        break