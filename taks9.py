def Encoder(s):
    row = []
    matrix = []

    without_spacebars = []  # входная строка с удаленными пробелами помещается сюда
    for i in range(len(s)):
        if s[i] != ' ':
            without_spacebars.append(s[i])

    sqrt = len(without_spacebars) ** 0.5
    rows = int(sqrt)  # определим размеры матрицы
    columns = rows + 1  # определим размеры матрицы
    last_string = len(without_spacebars) - rows * columns  # на случай присутствия строки нестандартной длины

    if len(without_spacebars) > rows * columns:  # в случае необходимости добавим еще одну строку
        rows = rows + 1

    if rows * columns > len(without_spacebars):  # этот блок заполняет матрицу исходной строкой
        for i in range(rows - 1):
            for j in range(columns):
                row.append(without_spacebars[j + i * columns])
            matrix.append(row)
            row = []
        for k in range(len(without_spacebars) - (rows - 1) * columns):
            row.append(without_spacebars[k + (rows - 1) * columns])
        matrix.append(row)
    elif rows * columns == len(without_spacebars):
        for i in range(rows):
            for j in range(columns):
                row.append(without_spacebars[j + i * columns])
            matrix.append(row)
            row = []

    transponned = []  # транспонированная матрица:
    transponned_row = []

    for i in range(last_string):
        for j in range(rows):
            transponned_row.append(matrix[j][i])
        transponned.append(transponned_row)
        transponned_row = []

    for i in range(columns - last_string):
        for j in range(rows - 1):
            transponned_row.append(matrix[j][i + last_string])
        transponned.append(transponned_row)
        transponned_row = []

    encoded = ''

    for i in range(len(transponned)):
        for j in range(len(transponned[i])):
            encoded = encoded + transponned[i][j]
        if i != len(transponned) - 1:
            encoded = encoded + ' '

    return encoded

def Decoder(s):

    row = []
    matrix = []
    list1 = s.split()
    last_column = 0
    decoded = ''

    without_spacebars = []  # входная строка с удаленными пробелами помещается сюда
    for i in range(len(s)):
        if s[i] != ' ':
            without_spacebars.append(s[i])

    rows = len(list1)
    columns = (len(without_spacebars) // rows) + 1

    for i in range(len(list1) - 1):
        if len(list1[i]) != len(list1[i + 1]):
            last_column = last_column + 1

    for i in range(len(list1)):  # этот блок заполняет матрицу исходной строкой
        for j in range(len(list1[i])):
            row.append((list(list1[i]))[j])
        matrix.append(row)
        row = []

    transponned = []  # транспонированная матрица:
    transponned_row = []

    for i in range(rows - 1):
        for j in range(columns):
            transponned_row.append(matrix[j][i])
        transponned.append(transponned_row)
        transponned_row = []

    for i in range(last_column):
        transponned_row.append(matrix[i][len(list1[0]) - 1])
    transponned.append(transponned_row)

    for i in range(rows - 1):  # считать по столбцам матрицу и сформировать строку на возврат
        for j in range(columns):
            decoded = decoded + (transponned[i][j])

    for k in range(last_column):  # последний столбец добавить
        decoded = decoded + transponned[rows - 1][k]

    return decoded

def TheRabbitsFoot(s, encode):

    if encode:
        encoded = Encoder(s)
        return encoded
    else:
        decoded = Decoder(s)
        return decoded
