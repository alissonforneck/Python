precoProduto = int(input('Digite o valor do produto: '));
desconto = int(input('Digite o valor do desconto '));
aplicandoDesconto = ((precoProduto*100)/100)-((desconto*100)/100 )
print('O valor final do produto com o desconto aplicado ficou ', aplicandoDesconto)