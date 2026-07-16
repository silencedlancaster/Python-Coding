#declarando um valor ou caractere para as variáveis
corretor = str(input("Digite o nome do corretor: "))
moveis_vendidos = int(input("Digite o quantidade de imóveis vendidos: "))
vendas = float(input("Digite o valor de vendas: "))


#o valor base do salário dos funcionários
salario = 2500
#comissão dos imoveis
imoveis_comissao = int(input("Digite o quantidade de imóveis vendidos: "))
comissao_vendas = (vendas * 0.05)

#calculando o salário final dos funcionários
salario_final = salario + imoveis_comissao + comissao_vendas

#o resultado será mostrado na tela
print(" Corretor: ", corretor)
print("Salário final: ", salario_final)
