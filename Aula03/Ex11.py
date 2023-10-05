# Exercício 11 - Calcular e exibir a área de um retângulo, a partir dos valores da base e altura que serão digitados. Se a área for maior que 100, exibir a mensagem “Terreno grande”.

b = int(input('Digite o valor da base do retângulo: '))
a = int(input('Digite o valor da altura do retângulo: '))

area = b * a

print(f'A área do retângulo é {area}')

if (area >= 100):
    print('Terreno Grande!')

