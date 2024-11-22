def magia():
    magico1 = []
    magico2 = []
    magico3 = []
    somaValor1 = 0
    somaValor2 = 0

    for i in range(3500):
        valor1 = int(input(f"Mago 1 - Feitiço {i + 1}: "))
        while valor1 <= 0:
            valor1 = int(input(f"Mago 1 - Feitiço {i + 1}: "))
        somaValor1 += valor1
        magico1.append(valor1)

        valor2 = int(input(f"Mago 2 - Feitiço {i + 1}: "))
        while valor2 <= 0:
            valor2 = int(input(f"Mago 2 - Feitiço {i + 1}: "))
        somaValor2 += valor2
        magico2.append(valor2)

        magico3.append(valor1 + valor2)

    print("\nPoder combinado dos feitiços (exibindo os primeiros 10 resultados):")
    for i in range(10):
        print(f"Feitiço {i + 1}: {magico3[i]}")

    print(f"\nSoma total dos pontos mágicos do Mago 1: {somaValor1}")
    print(f"Soma total dos pontos mágicos do Mago 2: {somaValor2}")
    print(f"Soma total dos pontos mágicos combinados: {somaValor1 + somaValor2}")

magia()
