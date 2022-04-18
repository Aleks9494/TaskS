# функция выводит все подсписки заданного списка

def function (words):
    str = words.split()
    result_list = list()
    result_list.append([])
    for i in range(len(str) + 1):
            for j in range(i):
                result_list.append(str[j:i])

    result_list.sort(key=len)
    return result_list


print(function('a b c d v'))