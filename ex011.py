larg = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))
área = larg * alt
print('Sua parede tem de dimensão de {}x{} e sua área é de {}m quadrados.'.format(larg, alt, área))
tinta = área / 2
print('Para pintar esta parede, você precisará de {}l de tinta.'.format(tinta))