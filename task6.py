length = 0.00000
matrix_code = [[6, 1, 9], [5, 2, 8], [4, 3, 7]]
t1 = [0, 0]
t2 = [0, 0]

def IncreaseLength(t1, t2):

    global length

    if t1[0] == t2[0] or t1[1] == t2[1]:
        length = length + 1
    else:
        length = length + 1.41421

def GetCoordinates(digit):
    for i in range(3):
        for j in range(3):
            if matrix_code[i][j] == digit:
                return i, j

def PatternUnlock(N, hits):

    for i in range(N - 1):
        t1 = GetCoordinates(hits[i])
        t2 = GetCoordinates(hits[i + 1])
        IncreaseLength(t1, t2)

    outputLength = ''
    stringLength = str(length)
    integralPart = stringLength.split('.')[0]
    fractionalPart = stringLength.split('.')[1]
    digitsNumberintegralPart = len(str(integralPart))
    digitsNumberfractionalPart = len(str(fractionalPart))

    for i in range(digitsNumberintegralPart): # уберем ноли из целой части
        if integralPart[i] != 0:
            outputLength = outputLength + integralPart[i]

    if digitsNumberfractionalPart <= 5:  # если дробная часть короче пятого знака то избавимся от нолей
        for i in range(digitsNumberfractionalPart):
            if fractionalPart[i] != 0:
                outputLength = outputLength + fractionalPart[i]

    if digitsNumberfractionalPart > 5: # если дробная часть длиннее пятого знака то округлим ее и избавимся от нолей
        for i in range(4): # обработаем дробную часть до предпоследнего знака вкючительно
            if fractionalPart[i] != 0:
                outputLength = outputLength + fractionalPart[i]

        if int(fractionalPart[5]) > 5 and fractionalPart[4] != 9:         # последнююю цифру отдельно обработаем:
            outputLength = outputLength + str(int(fractionalPart[4]) + 1)
        elif int(fractionalPart[5]) <= 5 and fractionalPart[4] != 0:
            outputLength = outputLength + str(fractionalPart[4])

    return outputLength
