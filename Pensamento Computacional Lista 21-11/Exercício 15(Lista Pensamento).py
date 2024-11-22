import random

def sorte():
    num = 0
    sorteio = random.randint(1, 100)
    print("O jogo de adivinhação começou!")
    print("Tente adivinhar um número de 1 a 100.")

    while True:
        try:
            numSorte = int(input("Digite seu número da sorte: "))
            if numSorte < 1 or numSorte > 100:
                print("Erro. Insira um número de 1 a 100.")
                continue
            if numSorte < sorteio:
                print("Errado. O número é maior!")
            elif numSorte > sorteio:
                print("Errado. O número é menor!")
            else:
                print(f"Parabens! Você acertou o número: {sorteio}")
                break
        except ValueError:
            print("Erro. Insira um número inteiro.")

sorte()

