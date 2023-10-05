#Exercício 15 - A partir de três valores que serão digitados, verificar se formam ou não um triângulo. Em caso positivo, exibir sua classificação: “Isósceles, escaleno ou eqüilátero”. Um triângulo escaleno possui todos os lados diferentes, o isósceles, dois lados iguais e o eqüilátero, todos os lados iguais. Para existir triângulo é necessário que a soma de dois lados quaisquer seja maior que o outro, isto, para os três lados.

a = int(input('Digite o valor de um lado do triangulo: '))
b = int(input('Digite o valor do segundo lado do triangulo: '))
c = int(input('Digite o valor do terceiro lado do triangulo: '))

if ((a + b) > c) and ((a + c) > b) and ((b + c ) > a):
    if (a != b) and (a != c) and (b != c):
        print ('Esse triangulo é escaleno')
    elif (a == b) or (a == c) and (b != c):
        print('Esse triangulo é isósceles')
    else:
        print('Esse triangulo é equilátero')        
else:
    print('Não é um triângulo')
