# Exercício 18 - Criar um programa para analisar a velocidade de um automóvel. Solicitar via teclado os valores da aceleração (a em m/s2), velocidade inicial (v0 em m/s) e o tempo de percurso (t em s). Calcular e exibir a velocidade final do automóvel em km/h. 

a = float(input('Digite a aceleração (m/s): '))
v0 = float(input('Digite a velocidade inicial (m/s): '))
t = float(input('Digite o tempo de percurso em (s): '))


v = (v0 + (a * t)) * 3.6


if (v <= 40):
    print('Veículo muito lento')
elif (v <= 60):
    print('Velocidade permitida')
elif (v <= 80):
    print('Velocidade de cruzeiro')
elif (v <= 120):
    print('Veículo rápido')
else:
    print('Veículo muito rápido')