"""
Pop: Utiliza o índice da lista como base para remover e retornar o elemento no array. Se não tiver um índice
especificado, o último elemento da lista é removido. Deve ser utilizado quando se tem consciência da posição
do elemento na lista ou quando for necessário remover apenas o último elemento.

Remove: Remove o primeiro elemento de um array correspondente ao valor fornecido. Se o valor não estiver na
lista, ocorre um erro. Deve ser usado quando você deseja remover um valor específico da lista, mas
não necessariamente afetar seu índice.

"""

def popIndex():
    lista = [10, 20, 30, 40, 50, 10]
    print(f"Lista Inicial: {lista}")
    indexPop = lista.pop(2)  
    print(f"Lista após uso do pop: {lista}")
    print(f"Elemento removido: {indexPop}")

def remover():
    lista = [10, 20, 30, 40, 50, 20]
    print(f"Lista Inicial: {lista}")
    lista.remove(20)  
    print(f"Lista após remover valor 20: {lista}")

def main():
    popIndex()
    remover()

main()