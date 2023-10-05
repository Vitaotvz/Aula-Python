# Exercício 21 - Entrar via teclado com dois valores quaisquer. Após a digitação, exibir um seletor de opções (“menu”) com as seguintes opções: (Fazer esse exercício utilizando If..Else)

while True:
    n1 = float(input('Digite o primeiro valor:'))
    n2 = float(input('Digite o segundo valor:'))

    print('\nMENU')
    print('\n(1) Multiplicação')
    print('\n(2) Adição')
    print('\n(3) Divisão')
    print('\n(4) Subtração')
    print('\n(5) Fim do processo')

    m = input('\nNo menu acima digite o número da operação lógica a ser realizado: ')

    if (m == "1"):
        resultado = n1 * n2
        print(f"Resultado da multiplicação: {resultado}")

    elif (m == "2"):
        resultado = n1 + n2
        print(f"Resultado da adição: {resultado}")
        
    elif (m == "3"):
        if n2 != 0:
            resultado = n1 / n2
            print(f"Resultado da divisão: {resultado}")
        else:
            print("Erro: Divisão por zero não é permitida.")

    elif (m == "4"):
        resultado = n1 - n2
        print(f"Resultado da subtração: {resultado}")

    elif (m == "5"):
        print("Programa encerrado.")
        break
    
    else:
        print("Erro: Opção inválida. Por favor, escolha uma opção válida (1 a 5).")
