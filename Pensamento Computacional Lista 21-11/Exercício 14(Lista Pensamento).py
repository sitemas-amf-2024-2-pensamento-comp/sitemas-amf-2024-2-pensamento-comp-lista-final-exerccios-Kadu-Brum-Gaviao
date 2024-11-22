def listaDuplicada():
    lista = [10, 20, 30, 40, 50, 20, 10, 40]
    return lista

def removerDuplicados(lista):
    listaUnica = []
    i = 0
    while i < len(lista):
        if lista[i] not in listaUnica:
            listaUnica.append(lista[i])
        i += 1
    return listaUnica

def main():
    lista = listaDuplicada()
    print(f"Lista Original: {lista}")
    listaUnica = removerDuplicados(lista)
    print(f"Lista sem duplicados: {listaUnica}")

main()
