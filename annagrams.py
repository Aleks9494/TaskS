
def Annagrams (words_list):
    for i in range (len(words_list)):                       # цикл по всем словам списка
        for j in range (i+1, len(words_list)):              # цикл по всем словам списка, кроме i-ого и раньше
            word_i = words_list[i]
            word_j = words_list[j]
            for c in words_list[i]:                         # цикл по буквам в i-ом слове
                if len(words_list[i]) == len(words_list[j]):
                    if c in word_j:
                        word_i = word_i.replace(c,'_', 1)   # заменяем найденную букву символом, чтобы избежать повторений, максимум 1 раз
                        word_j = word_j.replace(c,'_', 1)
                        print(word_i, word_j)
            if word_j == word_i:
                print (f'{words_list[i]} и {words_list[j]} являются аннаграммами!!')

Annagrams (input().split())