alunos = {}

def registrarNotas(nome, notas):
    alunos[nome] = notas

def calcularMedia(notas):
    return sum(notas) / len(notas)
    

def exibirEstatisticas():
    mediaTurma = 0
    totalAlunos = 0
    maior_nota = float('-inf')
    menor_nota = float('inf')

    print('\nResumo das Notas dos Alunos:')
    for nome, notas in alunos.items():
        mediaAluno = calcularMedia(notas)
        print(f'Aluno: {nome}, Notas: {notas}, Média: {mediaAluno:.2f}')
        mediaTurma += mediaAluno
        totalAlunos += 1
        maior_nota = max(maior_nota, max(notas))
        menor_nota = min(menor_nota, min(notas))
    
    mediaTurma = mediaTurma / totalAlunos if totalAlunos > 0 else 0
    print(f'\nMédia da Turma: {mediaTurma:.2f}')
    print(f'Maior nota da turma: {maior_nota}')
    print(f'Menor nota da turma: {menor_nota}')

registrarNotas('João', [7.5, 8.0, 9.0])
registrarNotas('Maria', [6.0, 7.0, 8.5])
registrarNotas('Pedro', [5.5, 6.0, 7.5])

exibirEstatisticas()
