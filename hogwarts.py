def BiggerGreater(input_string):  #получаем исходную строку параметром функции

    rest_of_the_string = []
    listed_string = list(input_string)   #разбиваем ее на список
    outerBreakerFlag = False
    output = ''
    lastUnsorted = 0

    for i in range(len(listed_string) - 2, -1, -1):
        for j in range(len(listed_string) - 1, i, -1):
            if listed_string[j] > listed_string[i]:
                lastUnsorted = i
                listed_string[i], listed_string[j] = listed_string[j], listed_string[i]
                outerBreakerFlag = True
                break
        if (outerBreakerFlag):
            break

    if not outerBreakerFlag:
        return ''

    if outerBreakerFlag:
        for i in range(lastUnsorted + 1, len(listed_string)):  # the rest of the string with change
            rest_of_the_string.append(listed_string[i])
        rest_of_the_string.sort()
        for j in range(0, lastUnsorted + 1):  # add to output string part of the listed string
            output = output + str(listed_string[j])
        for k in range(0, len(rest_of_the_string)):
            output = output + str(rest_of_the_string[k])
        return output
