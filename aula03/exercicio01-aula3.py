lado1 = int(input('Digite um valor para o lado 1: '))
lado2 = int(input('Digite um valor para o lado 2: '))
lado3 = int(input('Digite um valor para o lado 3: '))
if (lado1 > 0 and lado2 > 0 and lado3 > 0):
    if (lado1 <= lado2 + lado3 and lado2 <= lado1 + lado3 and lado3 <= lado2 + lado1 ):
        if (lado1 == lado2 and lado2 == lado3 and lado1 == lado3):
            print('Triangulo Equilátero')
        elif (lado1 != lado2 and lado1 != lado3 and lado2 != lado3):
            print('Triangulo Escaleno')
        else:
            print('Triangulo Isóceles')
    else:
        print('Um dos lados é maior que os outros somados.')
else:
    print('Valores invalidos!')