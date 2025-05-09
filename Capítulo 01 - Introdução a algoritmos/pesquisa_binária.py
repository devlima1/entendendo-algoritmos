def pesquisa_binária(lista, target):
    l = 0
    r = len(lista) - 1

    while (l <= r):
        mid = (l + r) // 2

        if target == lista[mid]:
            return mid
        elif target > lista[mid]:
            l = mid + 1
        else:
            r = mid - 1
    return -1