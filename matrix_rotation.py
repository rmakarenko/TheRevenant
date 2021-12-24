def MatrixTurn(data, h, w, t):

    cycles = []
    for l in range(min(h, w) // 2):
        line = []
        for i in range(l, w - l - 1):
            line.append(data[l][i])
        for i in range(l, h - l - 1):
            line.append(data[i][-l - 1])
        for i in range(w - l - 1, l, -1):
            line.append(data[-l - 1][i])
        for i in range(h - l - 1, l, -1):
            line.append(data[i][l])
        cycles.append(line)

    matrix = [[''] * w for x in range(h)]
    for l in range(min(h, w) // 2):
        c = - t
        cycle_size = len(cycles[l])
        for i in range(l, w - l - 1):
            matrix[l][i] = cycles[l][c % cycle_size]
            c += 1
        for i in range(l, h - l - 1):
            matrix[i][-l - 1] = cycles[l][c % cycle_size]
            c += 1
        for i in range(w - l - 1, l, -1):
            matrix[-l - 1][i] = cycles[l][c % cycle_size]
            c += 1
        for i in range(h - l - 1, l, -1):
            matrix[i][l] = cycles[l][c % cycle_size]
            c += 1

    for index, line in enumerate(matrix):
        line = "".join(matrix[index])
        data[index] = line
