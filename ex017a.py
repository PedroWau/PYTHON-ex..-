import math

op = float(input('Digite o comprimento do cateto oposto do triângulo: '))
adj = float(input('Digite o comprimento do caceto adjacente do triângulo: '))
hip = (op**2) + (adj**2)
print('O comprimento da hipotenusa é {:.2f}'.format(math.sqrt(hip)))