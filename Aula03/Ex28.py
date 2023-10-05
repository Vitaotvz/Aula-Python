x = int(input('Digite um número para obter a tabuada: '))

while(x<=0):
        print('Erro! Digite apenas números positivos!')
        x=int(input('Digite um número para obter sua tabuada: '))

a = int(input('Digite o intervalo inicial da tabuada: '))
while(a<=0):
        print('Erro! Digite apenas números positivos!')
        int(input('Digite o intervalo inicial da tabuada: '))
        
b = int(input('Digite o segundo intervalor da tabuada: '))
while(b<=a):
       print('Erro! O intervalo final deve ser maior que o inicial!')
       b=int(input('Digite o intervalo final da tabuada: ')) 

for i in range(b, a-1, -1):
    r = x * i
    print (f'{x} X {i} = {r}')