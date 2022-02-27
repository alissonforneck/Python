#receber uma frase, e mostrar os dois ultimos caracteres da frase

frase = input('Digite uma frase qualquer: ')
tamanho = len(frase)

frase2 = frase[:int(tamanho/2)]
tamanhoFrase2 = len(frase2)

resultado = frase2[int(tamanhoFrase2-2):]
print(resultado)