def valida_valor(pergunta,min = 0, max = 99):
    valor = int(input(pergunta))
    while (valor < min or valor > max):
        valor = int(input(pergunta))
    return valor
def fatorial(numero):
    """
    Função para calcular o fatorial de um número que recebi como parâmetro
    numero: recebe um valor inteiro
    :return:
    """
    fat = 1
    if numero == 0:
        return fat
    for i in range(1, numero+1,1):
        fat *= i
    return fat

valor = valida_valor('Digite um valor para calcular o fatorial: ')
print('{}! = {}'.format(valor,fatorial(valor)))