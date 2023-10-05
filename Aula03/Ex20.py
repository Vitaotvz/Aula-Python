# Exercício 20 - Uma escola com cursos em regime semestral realiza duas avaliações durante o semestre e calcula a média do aluno, da seguinte maneira:

# Entrada da nota da primeira avaliação
P1 = float(input("Digite a nota da primeira avaliação (P1): "))

# Média de aprovação
media_aprovacao = 5.0

# Cálculo da nota mínima na segunda avaliação (P2) para aprovação
P2_minima = (3 * media_aprovacao - P1) / 2

# Verifica se a nota mínima é menor que zero (impossível ser negativa)
if P2_minima < 0:
    print("O aluno já está aprovado, pois a nota mínima necessária é negativa.")
else:
    print(f"O aluno precisa tirar pelo menos {P2_minima:.2f} na segunda avaliação (P2) para ser aprovado.")
