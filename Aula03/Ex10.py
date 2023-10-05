# Exercício 10 - Entrar com dois valores quaisquer. Exibir o maior deles, se existir, caso contrário, enviar mensagem avisando que os números são idênticos.

print(f"\nDigite dois valores quaisquer e irei descobrir qual número é o maior, menor ou idêntico!")

n1 = float(input('\nDigite o primeiro valor: '))

n2 = float(input('\nDigite o segundo valor: '))

if (n1 == n2):
    print(f"\nOs valores {n1}, e {n2} são idênticos")

elif (n1 > n2):
    print(f"\nO maior número é: {n1}")

else:
    print(f"\nO menor número é:{n2}")

print("\n FIM DO PROGRAMA !")

