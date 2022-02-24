#quantidad de dias e km do carro percorrido, dia custa 60 e km rodado 0.15
kmpercorrido = float(input('Quantos KMs você percorreu com o carro? '))
dias = float(input('Quantos dias você ficou com o carro? '))
valorFinal = (kmpercorrido*0.15)+ (dias*60)
#print('Voce percorreu {}KM, em {} dias, o que gerou um valor de {} para ser pago'.format(kmpercorrido,dias,valorFinal))
#Segundo o principio do clean code isto esta errado pois passa deu uma linha
#o que torna dificil de visualizar e precisa ser scroolado para o lado
print('KM = {} '.format(kmpercorrido))
print('Dias =  {}'.format())
print('Valor = {} '.format(valorFinal))