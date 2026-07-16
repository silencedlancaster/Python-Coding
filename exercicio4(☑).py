#pedindo o valor das variáveis da distância a percorrer
percorrido = float(input("Digite a distância que deseja ir (km): "))

#condição de preços por kilometro
if percorrido > 200: 
    por_km = 0.50
else:
    por_km = 0.45

#o calculo do kilometro á percorrer
total_percorrer = (percorrido * por_km)

#resultado na tela
print("O valor da corrida: R$", total_percorrer)

