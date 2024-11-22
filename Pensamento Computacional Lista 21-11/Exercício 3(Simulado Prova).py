def menu():
    print("1. Sacar ouro")
    print("2. Depositar ouro")
    print("3. Exibir extrato")
    print("4. Sair do programa")
    opc = int(input("Selecione uma opção: "))
    return opc

def sacarOuro(ouro, transacoes):
    saque = float(input("Digite o valor a ser sacado: "))
    if saque <= ouro:
        ouro -= saque
        transacoes.append(saque * -1)
    else:
        print("Saldo insuficiente!")
    return ouro, transacoes

def depositar(ouro, transacoes):
    deposito = float(input("Digite o valor a ser depositado: "))
    ouro += deposito
    transacoes.append(deposito)
    return ouro, transacoes

def apresentarExtrato(transacoes):
    print("Transações: ")
    for i in transacoes:
        if i > 0:
            print(f"Depósito: {i}")
        else:
            print(f"Saque: {i}")

def main():
    ouro = -1
    opc = 0
    transacoes = []
    while ouro < 0:
        ouro = float(input("Digite o ouro inicial: "))
    while opc != 4:
        opc = menu()
        if opc == 1:
            ouro, transacoes = sacarOuro(ouro, transacoes)
        elif opc == 2:
            ouro, transacoes = depositar(ouro, transacoes)
        elif opc == 3:
            apresentarExtrato(transacoes)
        elif opc == 4:
            print("Saindo do programa...")
            break

main()


