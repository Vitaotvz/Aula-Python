# Entrar via teclado com o valor de cinco produtos. Após as entradas, digitar um valor referente ao pagamento da somatória destes valores. Calcular e exibir o troco que deverá ser devolvido.

prod1 = float(input('Digite o valor do produto 01 R$: '))
prod2 = float(input('Digite o valor do produto 02 R$: '))
prod3 = float(input('Digite o valor do produto 03 R$: '))
prod4 = float(input('Digite o valor do produto 04 R$: '))
prod5 = float(input('Digite o valor do produto 05 R$: '))

pag  = float(input('Digite o valor total para o pagamento R$: '))

troco  = pag - (prod1 + prod2 + prod3 + prod4 + prod5)

print(f'O troco é de R$ {troco}')
