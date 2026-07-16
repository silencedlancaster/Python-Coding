#pedindo os valores das variáveis de valor da mercadoria e desconto
mercadoria = float(input("Digite o valor da mercadoria: R$"))
desconto = float(input("Digite o valor do desconto: "))

#fazendo o valor do desconto ficar certo para a conta
percentual_desconto = (desconto / 100)

preco_total = mercadoria - percentual_desconto

print("O preço final á pagar é: ", preco_total)
