# Lógica Dedutiva

def maiorIdade():
    idade = int(input('Digite uma idade: '))
    if idade >= 18:
        print(f'A pessoa é maior de idade. Idade: {idade}')
    else:
        print(f'A pessoa é menor de idade. Idade: {idade}')

maiorIdade()


# Logica Indutiva

def mediaTemp():
    temperaturas = [30, 32, 29, 28, 31, 33, 30]
    mediaTemperatura = sum(temperaturas) / len(temperaturas)
    if mediaTemperatura > 25:
        print('Com base nas temperaturas, o clima está quente.')
    else:
        print('Com base nas temperaturas, o clima está frio.')

mediaTemp()