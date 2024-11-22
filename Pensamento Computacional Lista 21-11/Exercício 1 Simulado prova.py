"""
Você é um mestre de RPG e quer analisar os atributos de seus jogadores. 
Crie uma função que receba um vetor de valores inteiros representando os atributos de um personagem. 
A função deve identificar:
O maior atributo e sua posição no vetor
O menor atributo e sua posição no vetor
A média dos atributos
Quantos atributos têm valor acima de 100
Quantos atributos são pares e quantos são ímpares
Restrição: Não utilize funções prontas como sort.
"""
def listaAtr():
    atr = []
    tamanhoLista = int(input("Qual o tamanho da lista: "))
    while tamanhoLista <= 0:
        print("O tamanho da lista deve ser maior que 0.")
        tamanhoLista = int(input("Qual o tamanho da lista: "))
    while len(atr) < tamanhoLista:
        valor = int(input("Acrescente um valor na lista: "))
        while valor < 0:
            print("Erro. Não são permitidos valores negativos. Tente novamente.")
            valor = int(input("Acrescente um valor na lista: "))
        atr.append(valor)
    return atr

def analise(atr):
    maior = atr[0]
    menor = atr[0]
    pMaior = 0
    pMenor = 0
    soma = 0
    acimaCem = 0
    pares = 0
    impares = 0
    for i in range(len(atr)):
        valor = atr[i]
        soma += valor
        if valor > maior:
            maior = valor
            pMaior = i
        if valor < menor:
            menor = valor
            pMenor = i
        if valor > 100:
            acimaCem += 1
        if valor % 2 == 0:
            pares += 1
        else:
            impares += 1
    media = soma / len(atr)
    print(f"Maior atributo: {maior}, Posição: {pMaior}")
    print(f"Menor atributo: {menor}, Posição: {pMenor}")
    print(f"Média dos atributos: {media:.2f}")
    print(f"Atributos acima de 100: {acimaCem}")
    print(f"Números pares: {pares}, Números ímpares: {impares}")

def main():
    atributos = listaAtr()
    analise(atributos)

main()
