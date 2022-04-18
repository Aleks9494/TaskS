# функция, реализующая поиск дубликатов в последовательности, и упаковку их в список списков

def function(letters):
    letters = letters.split()
    result_list = list()
    temp = list()
    for c in letters:
        if c in temp:                       # если символ есть в подсписке, добавляем туда такой же
            temp.append(c)
        else:                               # если нет такого сивола в подсписке
            if temp:                        # если подсписок не пустой (как в первой итерации)
                result_list.append(temp)    # добавляем подсписок одинаковых символов в результат
            temp = [c]                      # обнуляем подсписок и заносим туда символ данной итерации

    result_list.append(temp)                # в конце цикла обновляем результат, если что то есть в подсписке
    return result_list

print (function ('w w w o r l d g g g g r e a t t e c c h e m g g p w w'))
print (function ('a a a b c d e e e e f f g i k l m n o o o o'))