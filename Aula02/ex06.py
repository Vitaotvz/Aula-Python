# Entrar via teclado com o valor da cotação do dólar e uma certa quantidade de dólares. Calcular e exibir o valor correspondente em Reais (R$).

c = float(input('Digite o valor da cotação do dólar em R$: '))

d = float(input('Digite o valor da quantidade de dólares US$: '))

r = c * d

print(f'O valor US$ {d:.2f} é equivalente a R$ {r:.2f}, de acordo com a cotação R$ {c:.2f}')