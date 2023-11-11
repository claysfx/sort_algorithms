def merge_sort(elementos):

    if len(elementos) > 1:
        # encontrar meio da lista
        mid = len(elementos) // 2

        # divide a lista
        left_half = elementos[:mid]
        right_half = elementos[mid:]

        # recursividade
        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        # ordenação e intercalação das partes
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                elementos[k] = left_half[i]
                i += 1
            else:
                elementos[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            elementos[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            elementos[k] = right_half[j]
            j += 1
            k += 1

    return elementos
