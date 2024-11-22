# <, significa menor que. Ex: 7 < 10

def menor():
    num1 = int(input('Digite o primeiro número: '))
    num2 = int(input('Digite o segundo número: '))
    if num1 < num2:
        print(f'{num1} é menor que {num2}.')
    elif num2 < num1:
        print(f'{num2} é menor que {num1}.')



# >, significa maior que. Ex: 10 > 5
def maior():
    num1 = int(input('Digite o primeiro número: '))
    num2 = int(input('Digite o segundo número: '))
    if num1 > num2:
        print(f'{num1} é maior que {num2}.')
    elif num2 > num1:
        print(f'{num2} é maior que {num1}.')


# =, significa recebe. Ex: idade = 18(idade recebe 18)
def recebe():
    nome = 'Pedro'
    idade = 18
    peso = 64.5
    altura = 1.65
    print(f'nome: {nome}, idade = {idade}, peso = {peso}, altura = {altura}')

# >=, significa maior igual. Ex: if num1 >= num2
# <=, significa menor igual. Ex: len(lista1) < len(lista2)
def maiorMenorIgual():
    idade =  int(input('Cadastre uma idade: '))
    if idade >= 18:
        print(f'Maior de idade, idade = {idade}')
    elif idade <= 0:
        print('Erro no cadastro. Tente novamente.')


# ==, significa igual. Ex: idade1 == idade2
# !=, significa diferente. Ex: peso1 != peso2
def igualDiferente():
    nome1 = input('Cadastre um nome: ')
    nome2 = input('Cadastre um nome: ')
    if nome1 == nome2:
        print(f'As duas pessoas cadastradas se chamam {nome1}')
    elif nome1 != nome2:
        print(f'O primeiro nome cadastrado é: {nome1}. O segundo nome cadastrado é {nome2}.')


# and, significa 'e'. Ex: if num > and num < 5
def numerosPositivos():
    num1 = int(input('Digite um número: '))
    num2 = int(input('Digite um número: '))
    num3 = int(input('Digite um número: '))
    if num1 > num2 and num1 > num3:
        print(f'O maior número é: {num1}')
    elif num2 > num1 and num2 > num3:
        print(f'O maior número é: {num2}')
    elif num3 > num1 and num3 > num2:
        print(f'O maior número é: {num3}')


# not, significa não. Ex: if 2 not in listaNumeros
def nao():
    membros = ['JORGE', 'CARLOS', 'ROBERTA', 'CLARA', 'JOSÉ']
    pessoa = input('Digite um nome: ').upper()
    if pessoa in membros:
        print(f'{pessoa} é um membro do clube.')
    elif pessoa not in membros:
        print(f'{pessoa} não é membro do clube.')

# or, significa 'ou'. Ex: if len(lista1) == len(lista2) or len(lista1) == len(lista3)
def ou(idade, temPermissao, estaAcompanhado):
    if idade >= 18 or temPermissao or estaAcompanhado:
        print('A pessoa pode entrar na festa.')
    else:
        print('A pessoa não pode entrar na festa.')


def main():
    menor()
    maior()
    recebe()
    maiorMenorIgual()
    igualDiferente()
    numerosPositivos()
    ou(20, False, False)


main()


