# Exemplo 01 - Fazer um programa que irá receber duas notas e irá calcular a média e verificar se o aluno está aprovado ou reprovado. Para estar aprovado é necessário obter uma média igual ou superior a 5, caso contrário o aluno estará reprovado.

p1 = float(input("Digite a nota da P1: "))
p2 = float(input("Digite a nota da P2: "))


m = (p1 + p2) / 2


if (m >= 5):
    print(f"Sua média foi {m:.2f} e você está aprovado!")
else:
    print("Reprovado!")