def buscaMenor(arr):
    menor = arr[0]
    menor_indice = 0

    for i in range(1, len(arr)):
        if arr[i] < menor:
            menor = arr[i]
            menor_indice = i
    return menor_indice

def ordenacaoporSelecao(arr):
    newArr = []
    
    for i in range(len(arr)):
        menor = buscaMenor(arr)
        newArr.append(arr.pop(menor))
    return newArr

# Exemplo de uso
arr = [5, 2, 1, 3, 0, 4]
print(ordenacaoporSelecao(arr))

# Reduzir para um única função
# def ordenacaoporSelecao(arr):
#     for i in range(len(arr)):
#         for j in range(i + 1, len(arr)):
#             if arr[j] < arr[i]:
#                 arr[j], arr[i] = arr[i], arr[j]
#     return arr

# Exemplo de uso
# arr = [4, 2, 5, 1, 0, 3]
# print(ordenacaoporSelecao(arr))