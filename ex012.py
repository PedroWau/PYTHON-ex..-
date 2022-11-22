preço = float(input('Digite o preço de um produto: €'))
print('Irá ser descontado uma percentagem de 5% de desconto a {}'.format(preço))
desconto = preço * 0.05
print('O preço final ficou em {:.2f}'.format(preço - desconto))