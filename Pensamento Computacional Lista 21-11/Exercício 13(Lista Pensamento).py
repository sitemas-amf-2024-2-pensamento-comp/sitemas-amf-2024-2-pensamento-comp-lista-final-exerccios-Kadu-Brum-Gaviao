"""
Continue: Pula de uma iteração designda no codigo, seguindo para a proxima iteração. Deve ser usada
quando você quer ignorar certas condições e continuar para iteração seguinte do laço.

Break: Interrompe o laço atual imediatamente, parando a execução do loop. O programa continua a ser executado
se tiver algo após o laço. Deve ser usada quando uma condição específica e deseja encerrar o loop naturalmente.

"""

def iterar():
    for numero in range(1, 11):
        if numero == 3:
            continue
        if numero == 5:
            break
        print(numero)

iterar()