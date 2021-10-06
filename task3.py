def ConquestCampaign(n, m, l, battalion):

    matrix = []  # основной список
    days_to_conquer = 1
    left_to_conquer = n * m   # эту переменную используем для остановки выполнения программы в момент, когда все поля будут заняты десантом

    # построить матрицу большего размера и заполнить ее -1
    for i in range(n + 2):  # цикл по строкам
        matrix_inner = []  # готовим очередной вложенный подсписок
        for j in range(m + 2):  # цикл по столбцам
            new_element = - 1
            matrix_inner.append(new_element)  # заполняем подсписок
        matrix.append(matrix_inner)  # добавляем подсписок к основному списку

    # вставить в матрицу из -1 матрицу из нолей
    for i in range(n):
        for j in range(m):
            matrix[i + 1][j + 1] = 0

    # расставить единицы десанта
    for i in range(0, len(battalion), 2):
        matrix[battalion[i] + 1][battalion[i + 1] + 1] = 1

    # вычесть десант из left_to_conquer
    for i in range(n):
        for j in range(m):
            if matrix[i + 1][j + 1] == 1:
                left_to_conquer = left_to_conquer - 1

    while left_to_conquer > 0:

        for i in range(1, n + 1):
            for j in range(1, m + 1): # если элемент равен нолю и есть сосед равный days_to_conquer то запишем туда число, на единицу большее, чем days_to_conquer
                    if matrix[i][j] == 0 and (matrix[i + 1][j] == days_to_conquer or matrix[i - 1][j] == days_to_conquer):
                        matrix[i][j] = days_to_conquer + 1
                        left_to_conquer = left_to_conquer - 1
                    elif matrix[i][j] == 0 and (matrix[i][j + 1] == days_to_conquer or matrix[i][j - 1] == days_to_conquer):
                        matrix[i][j] = days_to_conquer + 1
                        left_to_conquer = left_to_conquer - 1
                    elif matrix[i][j] == 0 and (matrix[i - 1][j - 1] == days_to_conquer or matrix[i - 1][j + 1] == days_to_conquer):
                        matrix[i][j] = days_to_conquer + 1
                        left_to_conquer = left_to_conquer - 1
                    elif matrix[i][j] == 0 and (matrix[i + 1][j - 1] == days_to_conquer or matrix[i + 1][j + 1] == days_to_conquer):
                        matrix[i][j] = days_to_conquer + 1
                        left_to_conquer = left_to_conquer - 1

                    if (i == n) and (j == m):
                        days_to_conquer = days_to_conquer + 1

    return days_to_conquer
