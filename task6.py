class Coder:

    length = 0
    matrix_code = [[6, 1, 9], [5, 2, 8], [4, 3, 7]]

    def IncreaseLength(t1, t2):
        if t1[0] == t2[0] or t1[1] == t2[1]:
            Coder.length = Coder.length + 1
        else:
            Coder.length = Coder.length + 1.41421

    def GetCoordinates(digit):
        for i in range(3):
            for j in range(3):
                if Coder.matrix_code[i][j] == digit:
                    return i, j

    def PatternUnlock(N, hits):

        t1 = [0, 0]
        t2 = [0, 0]

        for i in range(N - 1):

            t1 = Coder.GetCoordinates(hits[i])

            t2 = Coder.GetCoordinates(hits[i + 1])

            Coder.IncreaseLength(t1, t2)

        outputLength = []

        stringLength = str(Coder.length)

        for i in range(len(stringLength)):
            if ((stringLength[i]) != '0'):

                outputLength.append(stringLength[i])

        return outputLength
