# Exercício 14 - Entrar com o peso e a altura de uma determinada pessoa. Após a digitação, exibir se esta pessoa está ou não com seu peso ideal. Fórmula: peso/altura².

peso = float(input('Digite o seu peso: '))
altura = float(input('Digite a sua altura: '))

imc = peso / (altura *altura)

if (imc <20):
    print('Abaixo do peso')
elif (imc <25):
    print('Peso ideal!')