"""
Em python, estruturas condicionais são instruções dadas através 
do codigo para tomarem decisões e realizarem condições especificas dentro do programa.

if: Executa um condição se ela for verdadeira.
Ex: if num >= 18

elif: Uma abreviação de 'Else if', feita para verificar outra condição caso a primeira seja falsa.
Ex: elif num < 18 and num > 0

else: Executa o codigo caso todas as condições anteriores sejam falsas.
Ex: else:
        print('Erro na numeração. Tente novamente.')
"""
def registro():
    while True:
        try:
            idade = int(input('Cadastre sua idade: '))
            if idade < 0:
                print('Erro: Idade não pode ser negativa. Tente novamente.')
            else:
                break
        except ValueError:
            print('Erro: Por favor, insira um número válido.')
    
    while True:
        sexo = input('Qual seu gênero (M/F): ').strip().upper()
        if sexo in ['M', 'F']:
            break
        else:
            print('Erro: Entrada inválida. Digite "M" para Masculino ou "F" para Feminino.')
    
    return idade, sexo


def registroResultados(idade, sexo):
    if idade < 18:
        print(f'Idade = {idade}. Menor de idade.')
    elif 18 <= idade < 60:
        print(f'Idade = {idade}. Maior de idade.')
    else:
        print(f'Idade = {idade}. Idoso.')

    genero = 'Masculino' if sexo == 'M' else 'Feminino'
    print(f'Gênero registrado: {genero} ({sexo})')


def main():
    idade, sexo = registro()
    registroResultados(idade, sexo)


main()
