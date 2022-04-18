
def MagicSquare(n):
    flag1, flag2, flag3, flag4 = False, False, False, False
    matrix = []
    for _ in range(n):
        row = [int(j) for j in input().split()]
        matrix.append(row)

    # проверка: состоит из чисел от 1 до n в квадрате, не повторяющихся
    new_matrix = sorted(sum(matrix, []))
    if len(new_matrix) == len(set(new_matrix)) and new_matrix[0] == 1 and new_matrix[-1] == n**2:
        flag1 = True

    # проверка: суммы элементов всех строк равны
    for i in range(1, n):
        if sum(matrix[i]) == sum(matrix[i-1]):
            flag2 = True
        else:
            flag2 = False
            break

    # проверка: суммы элементов всех столбцов равны
    new_matrix = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(matrix[j][i])    # переворачиваем матрицу
        new_matrix.append(row)
    for i in range(1, n):
        if sum(new_matrix[i]) == sum(new_matrix[i-1]):
            flag3 = True
        else:
            flag3 = False
            break

    # проверка: суммы диагоналей равны
    sum1, sum2 = 0, 0
    for i in range(n):
        for j in range(n):
            if i == j:    # главная диагональ
                sum1 += matrix[i][j]
            if i + j + 1 == n:    # побочная диагональ
                sum2 += matrix[i][n - i - 1]
    if sum1 == sum2:
        flag4 = True

    if flag1 and flag2 and flag3 and flag4:
        print("YES")
    else:
        print("NO")

MagicSquare(6)
