def buscaMenor(arr):
    menor = arr[0]
    menor_indice = 0

    for i in range(1, len(arr)):
        if arr[i] < menor:
            menor = arr[i]
            menor_indice = i
    return menor_indice

def ordenacaoporSelecao(arr):
    novoArr = []

    for i in range(len(arr)):
        menor = buscaMenor(arr)
        novoArr.append(arr.pop(menor))
    return novoArr

# exemplo de uso
arr = [5, 4, 1, 2, 0, 3]
print(ordenacaoporSelecao(arr))