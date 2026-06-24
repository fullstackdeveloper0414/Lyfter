"""
Ejercicios de Iterables y Listas
Jaime C Smith
05/22/2026
"""
# ============================================================
# 1) Iterate two lists of the same size and print their values
#    at the same time
# ============================================================

# Example lists
first_list = ['Hay', 'en', 'que', 'iteracion', 'indices', 'muy']
second_list = ['casos', 'los', 'la', 'por', 'es', 'util']

# Both lists have the same size, so we can use range and len (index-based iteration)
for index in range(0, len(first_list)):
    word1 = first_list[index]
    word2 = second_list[index]
    print(word1, word2)

