def selection_sort(elementos):
  n = len(elementos)

  for i in range(n - 1):
    # o índice da iteração será o menor índice da lista que ainda não foi preenchido
      min_index = i

          # seleção do menor elemento ainda não preenchido na lista ordenada 
      for j in range(i + 1, n):
          if elementos[j] < elementos[min_index]:
              min_index = j

      # troca do elemento atual com o menor elemento encontrado
      elementos[i], elementos[min_index] = elementos[min_index], elementos[i]

# Exemplo de uso:
elementos = [64, 25, 12, 22, 11]
selection_sort(elementos)
print("Lista ordenada:")
print(elementos)