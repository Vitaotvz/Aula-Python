num=int(input('Digite um número para obter sua tabuada: '))


while(num<=0):
    print('Erro! Digite apenas números positivos!')
    num=int(input('Digite um número para obter sua tabuada: '))


for i in range(1, 11, 1):
    r = num * i
    print(f'{num} X {i} = {r}')