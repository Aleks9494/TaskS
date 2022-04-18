# функция, реализующая разбиение списка на чанки заданной длины

def function(letters, n):
    letters = letters.split()
    result_list = list()
    for i in range(len(letters)):
        if i == 0:                              # если первая итерация, создаем пустой подсписок, добавляем туда первый символ
            temp = list()
            temp.append(letters[i])
        elif i % n == 0:                        # если итерация равна длине чанки (т.е.чанку надо добавить в результирующий список)
            result_list.append(temp)            # добавляем ее в результат
            temp = [letters[i]]                 # обнуляем temp и добавляем туда i-тый элемент
        else:                                   # если еще не достигли длины чанки, добавляем элемент в подсписок
            temp.append(letters[i])

    result_list.append (temp)                   # в конце цикла обновляем результат, если что то есть в подсписке
    return result_list

print (function ('a b c d e f g', 3))
print (function ('a b c d e f g i k l m n o', 7))