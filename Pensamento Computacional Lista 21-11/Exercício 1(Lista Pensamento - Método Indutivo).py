"""
Método Indutivo: Ao observarmos exemplos específicos, podemos generalizar 
uma regra ou padrão para a realização de uma tarefa.
"""

def imparPar():
    for i in range(1, 101):
        if i % 2 != 0:
            print(f"Números impares: {i}")

imparPar()
