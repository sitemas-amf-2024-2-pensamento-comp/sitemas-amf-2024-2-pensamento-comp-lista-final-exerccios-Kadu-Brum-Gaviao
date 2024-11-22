def numeros():
    listaNum = []
    for i in range(3):
        while True:
            try:
                num = int(input("Digite um número: "))
                listaNum.append(num)
                break
            except ValueError:
                print("Erro. É obrigatorio digitar um número inteiro.")
    maior = max(listaNum)
    print(f"O maior número é: {maior}")

numeros()