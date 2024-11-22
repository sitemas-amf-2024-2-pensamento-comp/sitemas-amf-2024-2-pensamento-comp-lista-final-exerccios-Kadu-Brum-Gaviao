
"""
Descreva os tipos de variáveis que estudamos e escreva um script que exemplifique o uso de cada um, 
incluindo int, float, str, e bool.
"""

# int: valores inteiros. Ex: 0, 1, 2, 3, etcs
def numeros():
    soma = 0
    for i in range(5):
        num = int(input('Digite um número: '))
        soma += num
    print(f'Resultado = {soma}')

# float: valores com ponto flutuante, números quebrados. Ex: 1.0; 0.4;5,5; etc.
def alturaPeso():
    altura = float(input('Qual a sua altura: '))
    peso = float(input('Qual seu peso: '))
    imc = peso / (altura * 2)
    print(f'Seu imc é: {imc:.2f}')

# string: uma cadeia de caracteres ou texto. Ex: 'Olá', 'Python', '000-000-00', etc.
def saudacaoString():
    nome = input('Qual seu nome: ')
    saudacao = f'Olá, meu nome é {nome}!'
    print(saudacao)

# booleano: funciona em um sistema de True ou False
def maiorIdade():
    idade = int(input('Qual a sua idade: '))
    if idade > 0 and idade >= 18:
        print(f'Maior de idade. Idade: {idade}')
    elif idade < 18 and idade > 0: 
        print(f'Menor de idade: {idade}')
  
def main():
    print('\nExemplo int:')
    numeros()

    print('\nExemplo float:')
    alturaPeso()

    print('\nExemplo string:')
    saudacaoString()

    print('\nExemplo booleano:')
    maiorIdade()

main()