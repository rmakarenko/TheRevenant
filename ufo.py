def octality(number):
    converted = 0
    length = len(str(number))
    for i in range(length):
        converted = converted + (8 ** (length - 1 - i)) * int(str(number)[i])
    return converted

def hexality(number):
    # пройти по длине числа и сохранить его как список из чисел, чтобы избавиться от букв ABCDEF 10 11 12 13 14 15
    converted = 0
    length = len(str(number))
    for i in range(length):
        if str(number)[i] == 'A':
            x = 10
            converted = converted + (16 ** (length - 1 - i)) * x
        elif str(number)[i] == 'B':
            x = 11
            converted = converted + (16 ** (length - 1 - i)) * x
        elif str(number)[i] == 'C':
            x = 12
            converted = converted + (16 ** (length - 1 - i)) * x
        elif str(number)[i] == 'D':
            x = 13
            converted = converted + (16 ** (length - 1 - i)) * x
        elif str(number)[i] == 'E':
            x = 14
            converted = converted + (16 ** (length - 1 - i)) * x
        elif str(number)[i] == 'F':
            x = 15
            converted = converted + (16 ** i) * x
        else:
            converted = converted + (16 ** (length - 1 - i)) * int(str(number)[i])
    return converted

def UFO(N, data, octal):
    converted = []
    for i in range(N):
        if octal:
            converted.append(octality(data[i]))
        else:
            converted.append(hexality(data[i]))
    return converted

