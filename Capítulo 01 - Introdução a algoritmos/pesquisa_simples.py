def pesquisa_simples(lista, target):
    length = len(lista)

    for i in range(length):
        if lista[i] == target:
            return i
    return -1