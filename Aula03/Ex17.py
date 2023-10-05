# Exercício 17 - 

p = float(input('Digite a sua altura: '))
a = float(input('Digite o seu peso: '))
s = input('Digite o seu sexo:\n  (M)masculino  (F) feminino ')

imc = p / (a *a)

if (s.upper == M) :
    if (imc < 20):
        print('Abaixo do peso')
    elif (imc < 25):
        print('Peso ideal!')
    else:
        print('Acima do peso')
elif (s.upper == F) :
    if (imc < 19):
        print('Abaixo do peso')
    elif (imc < 24):
        print('Peso ideal!')
    else:
        print('Acima do peso')

else:
    print('sexo inválido!')