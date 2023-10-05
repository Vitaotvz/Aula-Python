#Exercício 16 - Verificar se três valores quaisquer (A, B, C) que serão digitados formam ou não um triângulo retângulo. Lembre-se que o quadrado da hipotenusa é igual a soma dos quadrados dos catetos.

a = int(input('Digite o primeiro lado do triângulo: '))
b = int(input('Digite o segundo lado do triângulo: '))
c = int(input('Digite o terceiro lado do triângulo: '))

if ( (a*a) == ((b*b) + (c*c)) ):
    print("O triângulo é retângulo!")

else:
    print("O triângulo não é retângulo")