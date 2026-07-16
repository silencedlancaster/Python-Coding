#pedindo o valor das variáveis do emprestimo
valor_casa = float(input("Digite o valor da casa desejada: R$"))
salario = float(input("Digite o valor do seu salário: R$"))
anos = int(input("Digite a quantidade de anos á pagar pela casa: "))

#conversão de anos para meses
meses = (anos * 12)
#calculando a prestação da casa
prestacao = valor_casa / meses
#calculando o limite da prestação
maximo = salario * 0.30

#verificando se a prestação é menor que os 30%
if prestacao <= maximo:
    print("Emprestimo aprovado.")
else:
    print("Emprestimo negado.")