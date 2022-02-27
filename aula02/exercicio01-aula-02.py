precoProduto = float(input('Digite o valor do produto: '));
desconto = float(input('Digite o valor do desconto '));
aplicandoDesconto = ((precoProduto*100)/100)-((desconto*100)/100 )
print('O valor do produto é {}, e com o desconto de {}, você pode pagar apenas {}'.format(precoProduto,desconto,aplicandoDesconto))