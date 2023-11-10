def insertion_sort(elementos):
  for i in range(1, len(elementos)):
      key = elementos[i]  # o elemento que será ordenado
      j = i - 1

      # "empurrando" os elementos para a direita
      while j >= 0 and key < elementos[j]:
          elementos[j + 1] = elementos[j]
          j -= 1

      # inserindo o elemento na posição adequada
      elementos[j + 1] = key

# Exemplo de uso:
elementos = [64, 25, 12, 22, 11]
insertion_sort(elementos)
print("Lista ordenada:")
print(elementos)