#pedindo o valor das variáveis dos carros alugados
percorrido_km = float(input("Digite a quantidade de km percorrido: "))
alugado_dias = int(input("Digite a quantidade de dias que o carro foi alugado: "))

#tabela de preços
carro_preco = 120
km_rodado = 0.15

#os calculos do preço
pagar_dias = (carro_preco * alugado_dias) 
pagar_km = (km_rodado * 0.15)
total = pagar_dias + pagar_km

#resultado mostrado na tela
print("O valor final a pagar: R$", f"{total:.2f}")