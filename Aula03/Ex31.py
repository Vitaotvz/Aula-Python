soma = 0
for i in range(1, 11, 1):
    num = int(input(f'Digite o {i}° número: '))


    while(num <= 0):
        print('Erro! Número negativo!')
        num = int(input(f'Digite o {i}° número: '))


    if (i == 1):
        maior = num
    elif (num > maior):
        maior = num
   
    soma = soma + num


media = soma / 10


print(f'O maior número é: {maior}')
print(f'A soma dos valores é: {soma}')
print(f'A média é: {media}')



    