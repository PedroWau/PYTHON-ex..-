from random import shuffle
n1 = str(input('Nome do aluno do primeiro trabalho: '))
n2 = str(input('Nome do aluno do segundo trabalho: '))
n3 = str(input('Nome do aluno do terceiro trabalho: '))
n4 = str(input('Nome do aluno do quarto trabalho: '))
lista = [n1, n2, n3, n4]
shuffle(lista)
print('A ordem de apresentacão será: ')
print(lista)