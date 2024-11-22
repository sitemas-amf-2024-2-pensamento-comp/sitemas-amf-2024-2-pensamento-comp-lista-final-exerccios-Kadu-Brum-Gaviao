"""
Método Dedutivo: É uma forma de raciocínio lógico que segue um conceito/premissa/regra 
universal para chegar a uma conclusão geral ou caso particular.

Pontos principais:

Premissa Geral: Uma afirmação/regra que é considerada verdadeira para todos os casos.

Premissa Específica: Uma observação/fato do caso que está sendo analisado.

Conclusão: A partir das premissas, podemos chegar a conclusão.
"""

def parImpar():
    num = int(input('Escolha um número: '))
    if num % 2 == 0:
        print(f'{num} é par')
    else: 
        print(f'{num} é impar')
