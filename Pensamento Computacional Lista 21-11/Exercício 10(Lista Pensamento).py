def calcularRenda():
    renda = float(input("Digite a sua renda mensal (Em R$): "))
    despesas = float(input("Digite suas despesas mensais (Em R$): "))
    pontuacaoCredito = int(input("Digite sua pontuação no crédito: "))
    parcelaMensal = float(input("Digite o valor da parcela mensal do empréstimo (Em R$): "))

    rendaLiquida = renda - despesas
    print(f"Sua renda líquida é: R$ {rendaLiquida:.2f}")

    return rendaLiquida, pontuacaoCredito, parcelaMensal

def elegibilidade(rendaLiquida, pontuacaoCredito):
    if pontuacaoCredito >= 650 and rendaLiquida >= 2000:
        return True
    return False

def verificarParcela(rendaLiquida, parcelaMensal):
    limiteParcela = 0.3 * rendaLiquida
    return parcelaMensal <= limiteParcela, limiteParcela

def emprestimo():
    rendaLiquida, pontuacaoCredito, parcelaMensal = calcularRenda()
    elegivel = elegibilidade(rendaLiquida, pontuacaoCredito)
    if elegivel:
        print("Você é elegível para o empréstimo.")
    else:
        print("Desculpe, você não atende aos critérios para o empréstimo.")
        return

    parcelaAceitavel, limiteParcela = verificarParcela(rendaLiquida, parcelaMensal)
    if parcelaAceitavel:
        print(f"A parcela mensal de R$ {parcelaMensal:.2f} está dentro do limite de R$ {limiteParcela:.2f}.")
    else:
        print(f"A parcela mensal de R$ {parcelaMensal:.2f} excede o limite permitido de R$ {limiteParcela:.2f}.")

emprestimo()
