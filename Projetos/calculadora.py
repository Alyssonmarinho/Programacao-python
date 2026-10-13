def ler_numero(mensagem):
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print("Entrada inválida! Digite apenas números.")

continuar = True
while continuar:

    primeiro_numero = ler_numero("Digite o primeiro número: ")
    operacao = input("Escolha a operação (+, -, *, /, raiz, potencia, porcentagem): ").lower().strip()

    if operacao == "potencia":
        expoente = ler_numero("Digite o expoente: ")
        resultado = primeiro_numero ** expoente
        print(f"O resultado da potenciação é: {resultado}")

    elif operacao == "raiz":
        indice = ler_numero("Digite o índice da raiz (ex: 2 para quadrada, 3 para cúbica): ")
        if indice != int(indice):
            print("Erro: O índice da raiz deve ser um número inteiro.")
        elif indice == 0:
            print("Erro: Não existe raiz de índice zero.")
        elif primeiro_numero < 0 and indice % 2 == 0:
            print("Erro: Não é possível calcular a raiz de índice par de um número negativo.")
        elif primeiro_numero < 0:
            resultado = -(abs(primeiro_numero) ** (1 / indice))
            print(f"O resultado da raiz é: {resultado}")
        else:
            resultado = primeiro_numero ** (1 / indice)
            print(f"O resultado da raiz é: {resultado}")

    elif operacao == "porcentagem":
        porcentagem = ler_numero("Quantos porcento do primeiro número você deseja calcular? ")
        resultado = (primeiro_numero * porcentagem) / 100
        print(f"{porcentagem}% de {primeiro_numero} é: {resultado}")    

    else:
        segundo_numero = ler_numero("Digite o segundo número: ")

        if operacao == "+":
            resultado = primeiro_numero + segundo_numero
            print(f"O resultado da soma é: {resultado}")

        elif operacao == "-":
            resultado = primeiro_numero - segundo_numero
            print(f"O resultado da subtração é: {resultado}")

        elif operacao == "*":
            resultado = primeiro_numero * segundo_numero
            print(f"O resultado da multiplicação é: {resultado}")

        elif operacao == "/":
            if segundo_numero != 0:
                resultado = primeiro_numero / segundo_numero
                print(f"O resultado da divisão é: {resultado}")
            else:
                print("Erro: Divisão por zero não é permitida.")

        else:
            print("Operação inválida. Por favor, escolha uma operação válida (+, -, *, /, raiz, potencia).")

    continuar = input("Deseja realizar outra operação? (s/n): ").lower().strip() 
    if continuar != "s":
        continuar = False