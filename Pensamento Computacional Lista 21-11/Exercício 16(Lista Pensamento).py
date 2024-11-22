# To-do list, lista de tarefas em python

# Função adicionarTarefa
def adicionarTarefa(lista, tarefa):
    lista.append(tarefa)
    print(f"Tarefa: '{tarefa}' adicionada com sucesso!")

# Função concluir uma tarefa
def concluirTarefa(lista, indice):
    if 0 <= indice < len(lista):
        print(f"Tarefa '{lista.pop(indice)}' concluida e removida!")
    else:
        print("Índice inválido. Tente novamente!")

# Função para exibir todas as tarefas
def exibirTarefas(lista):
    print("\nTarefas Atuais: ")

    for i, tarefa in enumerate(lista):
        print(f"{i}: {tarefa}")

# Função com o menu da lista de tarefas
tarefas = []

while True: 
    print("\n1. Adicionar tarefa")
    print("\n2. Concuir tarefa")
    print("\n3. Exibir tarefas")
    print("\n4. Sair")

    opcao = int(input("Digite uma opção: "))

    if opcao == 1:
        novaTarefa = input("Digite a nova tarefa: ")
        adicionarTarefa(tarefas, novaTarefa)
    elif opcao == 2:
        exibirTarefas(tarefas)
        indice = int(input("Digite o índice da tarefa concluida: "))
        concluirTarefa(tarefas, indice)
    elif opcao == 3: 
        exibirTarefas(tarefas)
    elif opcao == 4:
        print("Encerrando o programa. Até mais!")
        break
    else: 
        print("Opção inválida! Tente novamente!")
    