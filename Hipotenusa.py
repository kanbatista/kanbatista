# Cáculo de Hipotenusa
from math import sqrt

a = int(input("Digite o Valor do cateto oposto: "))
b = int(input("Digite o valor do cateto adjacente: "))
print("O valor da hipotenusa é: {:.2f} ".format(sqrt(((a ** 2) + (b ** 2)))))