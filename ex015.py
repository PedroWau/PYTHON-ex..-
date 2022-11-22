dias = int(input('Quantos dias alugado? '))
km = float(input('Quantos km percorridos? '))
total = (60 * dias) + (0.15 * km)
print('O total a pagar é de {:.2f}€.'.format(total))
