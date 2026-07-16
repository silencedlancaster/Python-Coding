#pedindo o valor das variáveis de kWh
kwh = float(input("Digite o valor de kWh consumido: "))
tipo_instalacao = input("Digite o tipo de instalaçõa (R para terias, C para comércios e I para industria): ").upper()

#vendo o tipo de instalação entre R, C ou I
#Residencia
if tipo_instalacao == "R" and kwh <= 500:
    valor = kwh * 0.40
    print("Valor a pagar: " f"{valor:.2f}")
elif tipo_instalacao == "R" and kwh > 500:
    valor = kwh * 0.65
    print("Valor a pagar: " f"{valor:.2f}")

#comercio
elif tipo_instalacao == "C" and kwh <= 1000:
    valor = kwh * 0.55
    print("Valor a pagar: " f"{valor:.2f}")
elif tipo_instalacao == "C" and kwh > 1000:
    valor = kwh * 0.60
    print("Valor a pagar: " f"{valor:.2f}")
#industria
elif tipo_instalacao == "I" and kwh <= 5000:
    valor = kwh * 0.55
    print("Valor a pagar: " f"{valor:.2f}")
elif tipo_instalacao == "I" and kwh > 5000:
    valor = kwh * 0.60
    print("Valor a pagar: " f"{valor:.2f}")

#condição de erro
else:
    print("Valor inválido.")