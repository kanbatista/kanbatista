# Calcúlo de IMC
peso = int(input("Por favor digite seu peso: "))
altura = float(input("Por favor digite sua altura: "))
print("Esse é o seu índice de massa corporea: {:3}".format(peso / (altura ** 2)))