def rotation(input_matrix, circuits):

    current_matrix = []
    rotated_matrix = []
    N = len(input_matrix[0])
    M = len(input_matrix)

    for i in range(M):  # copy the input matrix to the current matrix and rotated matrix
        current_list = []
        for j in range(N):
            current_list.append(input_matrix[i][j])
        current_matrix.append(current_list)
        rotated_matrix.append(current_list)

    for i in range(circuits):  # last curcuit will be handled in the next cycle

        for j in range(N - 1 - i, i, - 1):  # upper horizontal line
            rotated_matrix[i][j] = current_matrix[i][j - 1]

        for j in range(i + 1, M - 2 * i):  # right vertical line
            rotated_matrix[j][M - 1 - i] = current_matrix[j - 1][M - 1 - i]

        for j in range(i, N - 1 - i):  # down horizontal line
            rotated_matrix[M - 1 - i][j] = current_matrix[M - 1 - i][j + 1]

        for j in range(i, M - 2 * i - 1):  # left vertical line
            rotated_matrix[j][i] = current_matrix[j + 1][i]

        for m in range(M):  # copy the rotated matrix to the current matrix in order to keep it actual
            current_list = []
            for n in range(N):
                current_list.append(rotated_matrix[m][n])
            current_matrix.append(current_list)

    return rotated_matrix

def MatrixTurn(Matrix, M, N, T):

    listed_matrix = []

    if M >= N: # define the amount of circuits
        circuits = N // 2
    else:
        circuits = M // 2

    for i in range(M):  # transform input matrix into the list
        current_list = []
        for j in range(N):
            current_list.append(Matrix[i][j])
        listed_matrix.append(current_list)

    for i in range(T):
        listed_matrix = rotation(listed_matrix, circuits)

    Matrix = listed_matrix
