#  программа, реальзующая все ходы ферзя из заданной клетки

def Queen(coords):
    str = coords[-1]                                                        # цифра, координата строки
    row = coords[0].lower()                                                 # буква, координата ряда
    chess_board = [['.']*8 for _ in range(8)]                               # заполняем доску точками
    dict_row = {x: y for x, y in zip('abcdefgh', range(8))}                 # для столбцов
    dict_str = {x: y for x, y in zip('12345678', range(8))}                 # для строк
    for i in range(8):
        for j in range(8):
            if i == dict_str[str] and j == dict_row[row]:                   # место, где стоит королева
                chess_board[i][j] = 'Q'
            elif j == dict_row[row] or i == dict_str[str]:                  # может ходить по ряду, по строке
                chess_board[i][j] = '*'
            elif abs(dict_str[str]-i) == 1 and abs(dict_row[row]-j) == 1:   # может ходить рядом во все клетки (разницы между i,j и местом нахождения равны 1)
                chess_board[i][j] = '*'
            elif abs(dict_str[str]-i) == abs(dict_row[row]-j):              # может ходить по диагоналям (разницы между i,j и местом нахождения равны)
                chess_board[i][j] = '*'
    for i in range(8):
        for j in range(8):
            print (chess_board[i][j], end=' ')
        print()


Queen('d4')
