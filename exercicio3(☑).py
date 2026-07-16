#pedindo o valor da variável da velocidade do carro
velocidade = float(input("Digite o valor da velocidade do seu carro: "))

if velocidade > 80:
    excesso_velocidade = velocidade - 80
    multa = excesso_velocidade * 50
    print("Você foi multado por ecesso de velocidade. O valor a ser pago: R$", multa)
else:
    print("Você não foi multado.")