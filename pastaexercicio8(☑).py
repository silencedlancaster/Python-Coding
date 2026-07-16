#Pedindo o valor das variáveis
deposito_inicial = float(input("Digite o valor do depósito inicial: "))
taxa = float(input("Digite o valor da taxa de juros mensal: "))
valor_inicial = deposito_inicial

#Calculando os juros
for mes in range(1, 25):
    juros = deposito_inicial * (taxa / 100)
    deposito_inicial += juros
    print(f"Mês {mes}: R$ {deposito_inicial:.2f}")

# Calculando o total de juros
total_juros = deposito_inicial - valor_inicial
print(f"Valor total ganho com juros: R$ {total_juros:.2f}")
print(f"Valor final: R$ {deposito_inicial:.2f}")