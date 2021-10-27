def BigMinus(s1, s2):

    result = []  # здесь сохраним результат исполнения программы
    max = ''  # это промежуточная строка, большая из входных
    min = ''  # это промежуточная строка, большая из входных
    zeros = ''
    minimum = ''
    element = 0
    list_max = []
    list_min = []

    if len(s1) > len(s2):  # определим, число в какой строке больше
        max = s1
        min = s2
    elif len(s1) < len(s2):
            max = s2
            min = s1
    else:
        for i in range(len(s1)):
            if int(s1[i]) > int(s2[i]):
                max = s1
                min = s2
            elif int(s1[i]) < int(s2[i]):
                max = s2
                min = s1
            elif i == len(s1) - 1 and int(s1[i]) == int(s2[i]):  # если строки по длине и по содержанию одинаковые - сразу вернем ноль
                return '0'

    difference = len(max) - len(min)  # разницу заполним нолями

    if difference > 0:  # меньшую строку заполним нолями с начала до длины большой
        for i in range(difference):
            zeros = zeros + '0'
        minimum = zeros + min
    else:
        minimum = min

    # на данном этапе есть две строки одинаковой длины, одна из них больше в цифровом эквиваленте

    for i in range(len(max)):  # обе строки превратим в интовые списки, меньшую заполнить нолями по длине до большей

        list_max.append(int(max[i]))
        list_min.append(int(minimum[i]))

    delta = 0  # здесь будем фиксировать необходимость заимствования единицы из старшего разряда

    for i in range(len(list_max)):  # по длине строки проход циклом с условиями на вычитание

        if list_max[len(list_max) - 1 - i] - delta >= list_min[len(list_max) - 1 - i]:  # если значение в большей строке минус дельта больше или равно чем в меньшей - то произведем вычитание не трогая старшие разряды
            element = list_max[len(max) - 1 - i] - delta - list_min[len(max) - 1 - i]
            result.append(element)
            delta = 0

        elif list_max[len(list_max) - 1 - i] == 0 and delta == 1:  # если значение в большей нолевое и есть заимствование из этого разряда
            element = 9 - list_min[len(max) - 1 - i]
            result.append(element)
            delta = 0

        elif list_max[len(list_max) - 1 - i] - delta < list_min[len(list_max) - 1 - i]:  # если значение в большей строке строго меньше чем в меньшей
            delta = 1
            element = 10 + list_max[len(max) - 1 - i] - list_min[len(max) - 1 - i]
            result.append(element)

    result_string = ''
    already_been_not_null = 0

    for i in range(len(result)):
        if result[len(result) - 1 - i] == 0 and already_been_not_null == 1:
            result_string = result_string + str(result[len(result) - 1 - i])
        elif result[len(result) - 1 - i] == 0 and already_been_not_null == 0:
            result_string = result_string + str(result[len(result) - 1 - i])
        elif result[len(result) - 1 - i] != 0:
            already_been_not_null = 1
            result_string = result_string + str(result[len(result) - 1 - i])

    return result_string
