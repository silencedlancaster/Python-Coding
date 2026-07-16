# Pedindo os valores das variáveis
deposito_inicial = float(input("Digite o valor do depósito inicial: "))
taxa = float(input("Digite a taxa de juros mensal (%): "))
deposito_mensal = float(input("Digite o valor do depósito mensal: "))

saldo = deposito_inicial
total_depositado = deposito_inicial

#calculo dos 24 meses, caluclo de juros e o depósito
for mes in range(1, 25):
    saldo += deposito_mensal        
    total_depositado += deposito_mensal
    juros = saldo * (taxa / 100)    
    saldo += juros
    print(f"Mês {mes}: R$ {saldo:.2f}")

total_juros = saldo - total_depositado

print(f"Valor total ganho com juros: R$ {total_juros:.2f}")
print(f"Valor total acumulado: R$ {saldo:.2f}")