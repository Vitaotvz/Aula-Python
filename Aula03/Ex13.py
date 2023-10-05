#Exercício 13 - Entrar via teclado com três valores distintos. Exibir o maior deles.

n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
n3 = int(input('Digite o terceiro valor: '))

if ((n1 > n2) and (n1 > n3)):
    print('O primeiro valor é o maior!')

elif ((n2 > n1) and (n2 > n3)):
    print('O segundo valor é o maior!')

else:
    print('o terceiro valor é o maior!')