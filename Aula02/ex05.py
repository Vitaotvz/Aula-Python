# Entrar via teclado com o valor de uma temperatura em graus Celsius, calcular e exibir sua temperatura equivalente em Fahrenheit.

c = float(input('Digite a temperatura em °C: '))

f = (c * 1.8) + 32

print(f'A temperatura {c}°C é equivalente a {f:.1f}°F')