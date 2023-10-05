# Exercício 09 - Entrar via teclado, com dois valores distintos. Exibir o menor deles.

n1 = float (input('Digite o primeiro valor: '))

n2 = float (input('Digite o segundo valor: '))

if (n1 < n2):
    print(f"O menor número é: {n1}")

else:
    print(f"O menor número é: {n2}")