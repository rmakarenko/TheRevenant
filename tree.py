def aging(input):
    output_list = []
    for i in range(len(input)):  # walkthrough the matrix
        current_list = []
        for j in range(len(input[0])):
                current_list.append(input[i][j] + 1)  # increasing numbers by 1
        output_list.append(current_list)
    return output_list

def destroying(input):
    output_list = []
    matrix = []
    for i in range(len(input) + 2):  # block creates the bigger matrix with frame from 0
        matrix_inner = []
        for j in range(len(input[0]) + 2):
            new_element = 0
            matrix_inner.append(new_element)
        matrix.append(matrix_inner)
    for m in range(len(input)):  # insert input into matrix with 0
        for n in range(len(input[0])):
            matrix[m + 1][n + 1] = input[m][n]
    for i in range(len(matrix) - 2):  # walkthrough all branches and deleting only the young neighbours of old branches
        for j in range(len(matrix[0]) - 2):
            if (matrix[i + 1][j + 1] < 3) and (matrix[i + 2][j + 1] >= 3 or matrix[i][j + 1] >= 3 or matrix[i + 1][j + 2] >= 3 or matrix[i + 1][j] >= 3):  # if one of 4 neighbours is old - delete the young
                matrix[i + 1][j + 1] = 0  # delete the young
    for i in range(len(matrix) - 2):  # walkthrough all branches and deleting only the young neighbours of old branches
        for j in range(len(matrix[0]) - 2):
            if matrix[i + 1][j + 1] >= 3:
                matrix[i + 1][j + 1] = 0  # delete the old
    for m in range(len(input)):  # insert input into matrix with 0
        current_list = []
        for n in range(len(input[0])):
            current_list.append(matrix[m + 1][n + 1])
        output_list.append(current_list)
    return output_list

def TreeOfLife(H, W, N, tree):
    matrix_listed = []
    return_strings = []
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
    for i in range(N):
        matrix_listed = aging(matrix_listed)
        if i % 2 != 0:
            matrix_listed = destroying(matrix_listed)  # this stands for second year
    for m in range(len(matrix_listed)):
        current_string = ''
        for n in range(len(matrix_listed[0])):
            if matrix_listed[m][n] > 0:
                current_string = current_string + ('+')
            else:
                current_string = current_string + ('.')
        return_strings.append(current_string)  # now input matrix from strings is transformed to list
    return return_strings
