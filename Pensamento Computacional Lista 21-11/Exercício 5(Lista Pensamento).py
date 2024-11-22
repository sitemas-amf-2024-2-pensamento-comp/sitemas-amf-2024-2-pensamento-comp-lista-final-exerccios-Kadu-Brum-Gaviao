"""
Considere um trecho de código semelhante ao das questões, onde o programa toma decisões com base na idade e sexo. 
Codifique o exemplo e avalie se as afirmações dadas são verdadeiras ou falsas.

Afirmativa 1: O programa diferencia as idades por categorias (menor de idade, maior de idade, idoso). 

Verdadeiro: O codigo separa as categorias usando if, elif, else. Cada faixa etária apresenta uma mensagem própria.

Afirmativa 2: O programa impede entradas inválidas de idade. Ex: Negar a entrada de números negativos ou textos.

Verdadeiro: 
- Caso a idade seja negativa, o programa exibe uma mensagem de erro e reincia.
- O try-except previne erros de entrada de não numéricos e reinicia o processo.

Afirmativa 3: O programa impede entradas de genêro inválidas. Ex: Qualquer uma que não seja 'M' ou 'F'.

Verdadeiro: if sexo not in ['M', 'F'] faz a verificação do gênero, entradas inválidas fazem o programa
recomeçar.

Afirmativa 4: Qualquer combinação válida de idade e gênero faz o programa funcionar corretamente.

Verdadeiro: Sim, o programa é funcional para qualquer combinação de entrada válida e exibe mensagens
conforme o que foi digitado.

Afirmativa 5: O programa apresenta erro ao receber uma entrada não numérica para a idade.

Falso: O código utiliza try-except para previnir erros de entrada que não sejam numéricos (strings, caracteres especiais, etc) 
e lida com isso exibindo uma mensagem de erro, reiniciando o processo sem quebrar o programa.


"""

def verificarIdadeSexo():
    while True:
        try:
            idade = int(input("Digite sua idade: "))
            if idade < 0:
                print("Erro: Idade não pode ser negativa. Tente novamente.")
                continue

            sexo = input("Digite seu gênero (M/F): ").strip().upper()
            if sexo not in ['M', 'F']:
                print("Erro: Gênero inválido. Digite 'M' para Masculino ou 'F' para Feminino.")
                continue
            break
        except ValueError:
            print("Erro: Por favor, insira um número válido para a idade.")

    if idade < 18:
        print("Menor de idade.")
    elif idade < 60:
        print("Maior de idade.")
    elif idade >= 60:
        print("Idoso.")
    
    if sexo == 'M':
        print("Gênero Registrado: Masculino.")
    elif sexo == 'F':
        print("Gênero Registrado: Feminino.")

verificarIdadeSexo()
