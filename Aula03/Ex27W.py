num=int(input('Digite um número para obter sua tabuada: '))
i=1


while(num<=0):
    print('Erro! Digite apenas números positivos!')
    num=int(input('Digite um número para obter sua tabuada: '))


while(i<=10):
    r = num * i
    print(f'{num} X {i} = {r}')
    i=i+1