#Exercício 22 - Exibir o seguinte seletor de opções e em função de uma escolha, solicitar os dados necessários para o cálculo da respectiva área. Enviar mensagem de erro se o usuário escolher uma opção inexistente.

while True:
    print('\nMENU')
    print('\n(1) Triângulo')
    print('\n(2) Quadrado')
    print('\n(3) Retângulo')
    print('\n(4) Círculo')
    print('\n(5) Fim do processo')
    m = input('\nNo menu acima digite o número da opção desejada: ')

    if (m == "1"):
        base = int(input('Digite o valor da base: '))
        altura = int(input('Digite o valor da altura: '))
        area = base * altura / 2
        print (f'A aérea do triângulo é de: {area:.2f}')

    elif (m == "2"):
        lado = int(input('Digite o valor do lado do quadrado: '))
        area = lado * lado
        print (f'A área do quadrado é de: {area:.2f}')

    elif (m == "3"):
        base = int(input('Digite o valor da base: '))
        altura = int(input('Digite o valor da altura: '))
        area = base * altura
        print (f'A área do retângulo é de: {area:.2f}')

    elif (m == "3"):
        raio = float(input('Digite o raio do círculo: '))
        area = 3.14 * raio * raio
        print (f'A área do círculo é de: {area:.2f}')

    elif (m == "5"):
        print("Programa encerrado.")
        break
    
    else:
        print("Erro: Opção inválida. Por favor, escolha uma opção válida (1 a 5).")
