# co = float(input('Quanto mede o cateto oposto? '))
# ca = float(input('Quanto mede o cateto adjacente? '))
# hip = (co ** 2 + ca ** 2) ** (1/2)
# print('A hipotenusa vai medir {:.2f}'.format(hip))

from math import hypot
co = float(input('Quanto mede o cateto oposto? '))
ca = float(input('Quanto mede o cateto adjacente? '))
hi = hypot(co, ca)
print('A hipotenusa vai medir {:.2f}'.format(hi))