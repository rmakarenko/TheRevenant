matrix_listed = []
matrix = []  # matrix plus size and with frame from 0

def aging():  # - в "первый" (чётный) год все ветки стареют на один год, и все пустые клетки заполняются новыми корнями с возрастом 1 год (визуально всё заполнено символами "+");

    for i in range(len(matrix) - 2):  # walkthrough the matrix
        for j in range(len(matrix[0]) - 2):
                matrix[i + 1][j + 1] = matrix[i + 1][j + 1] + 1  # increasing numbers by 1

def destroying():

    for i in range(len(matrix) - 2):  # walkthrough all branches and deleting only the young neighbours of old branches
        for j in range(len(matrix[0]) - 2):
            if (matrix[i + 1][j + 1] < 3) and (matrix[i + 2][j + 1] >= 3 or matrix[i][j + 1] >= 3 or matrix[i + 1][j + 2] >= 3 or matrix[i + 1][j] >= 3):  # if one of 4 neighbours is old - delete the young
                matrix[i + 1][j + 1] = 0  # delete the young
    for i in range(len(matrix) - 2):  # walkthrough all branches and deleting only the young neighbours of old branches
        for j in range(len(matrix[0]) - 2):
            if matrix[i + 1][j + 1] >= 3:
                matrix[i + 1][j + 1] = 0  # delete the old

def TreeOfLife(H, W, N, tree):

    matrix_listed = []
    return_strings = []
    rest_of_repeat_cycle = 0
    repeat_cycle = 0

    for m in range(len(tree)):  # this block changes list of strings to list of symbols
        current_list = []
        for n in range(len(tree[0])):
            current_list.append(tree[m][n])
        matrix_listed.append(current_list)

    for i in range(len(matrix_listed)):  # change all '.' and '+' to 0 and 1
        for j in range(len(matrix_listed[0])):
            if matrix_listed[i][j] == '.':
                matrix_listed[i][j] = 0
            elif matrix_listed[i][j] == '+':
                matrix_listed[i][j] = 1

    for i in range(H + 2):  # block creates the bigger matrix with frame from 0
        matrix_inner = []
        for j in range(W + 2):
            new_element = 0
            matrix_inner.append(new_element)
        matrix.append(matrix_inner)

    for m in range(len(matrix_listed)):  # insert matrix_listed into matrix with 0
        for n in range(len(matrix_listed[0])):
            matrix[m + 1][n + 1] = matrix_listed[m][n]

    if N % 2 != 0 and N > 1:  # count the future call of the functions
        repeat_cycle = int(N // 2)
        rest_of_repeat_cycle = N - repeat_cycle
    elif N == 1:
        rest_of_repeat_cycle = 1
    else:
        repeat_cycle = int(N // 2)

    for i in range(repeat_cycle):

        aging()  # this stands for first year
        aging()  # this stands for second year
        destroying()  # this stands for second year

    if rest_of_repeat_cycle > 0:
        aging()  # this stands for first year

    for m in range(len(matrix) - 2):
        current_string = ''
        for n in range(len(matrix[0]) - 2):
            if matrix[m + 1][n + 1] > 0:
                current_string = current_string + ('+')
            else:
                current_string = current_string + ('.')
        return_strings.append(current_string)  # now input matrix from strings is transformed to list

    return return_strings
