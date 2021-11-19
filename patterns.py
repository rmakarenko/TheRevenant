def convert_to_list(line, row_len, i): # i - это количество элементов в строке
    converted_row = []
    converted_list = []
    for i in range(i):  # соберем массив из строки, разбив его на элементы, длиной row_len
        for j in range(row_len):
            converted_row.append(line[j + i * row_len])
        converted_list.append(converted_row)
        converted_row = []
    return converted_list  # длина возвращаемого массива равна i

def CheckPatternsEquality(line_2):
    patterns_are_equal = []
    length_of_the_line = len(line_2)
    limit = length_of_the_line / 2 + 1

    for i in range(2, int(limit), 2):  # если длина входной строки четная то определим, насколько она делится нацело и для соответственных длин элементов произведем проверку
        patterns_are_equal = True
        list_of_elements = convert_to_list(line_2, int(length_of_the_line / i), i)
        for j in range(len(list_of_elements) - 1):
            if i == int(limit) - 2 and j == len(list_of_elements) - 2 and list_of_elements[j] != list_of_elements[j + 1]:
                return False
            elif patterns_are_equal and j == len(list_of_elements) - 2 and list_of_elements[j] == list_of_elements[j + 1]:
                return True
            elif list_of_elements[j] == list_of_elements[j + 1]:
                continue
            elif list_of_elements[j] != list_of_elements[j + 1]:
                patterns_are_equal = False
                break
    return patterns_are_equal

def LineAnalysis(line):

    listed_line = []  # входная строка превращенная в список
    without_asterix = ''  # listed line с удаленными с концов звездочками

    for i in range(len(line)):  # в случае паттерна, в котором первый или последний символ не звездочка - вернем False
        if line[0] != '*' or line[len(line) - 1] != '*':
            return False

    for i in range(len(line)):  # в случае паттерна, в котором присутствуют только звездочки (в любом количестве) - вернем True
        if line[i] != '*':
            break
        elif i == len(line) - 1 and line[len(line) - 1] == '*':
            return True

    for i in range(len(line)):  # получим список из символов входной строки
        listed_line.append(line[i])

    if len(line) > 1:  # создадим новый список, удалив первую и последнюю звезды
        for i in range(1, len(line) - 1):
            without_asterix = without_asterix + line[i]

    for i in range(len(without_asterix)):  # в случае паттерна, в котором присутствуют только точки (в любом количестве), кроме концевых звездочек - вернем True
        if i == len(without_asterix) - 1 and without_asterix[len(without_asterix) - 1] == '.':
            return True
        elif line[i] != '.':
            break

    if len(line) % 2 != 0:  # если длина входной строки нечетная то для нее должен быть свой метод, его нужно написать? или я ошибаюсь?
        line_without_last_asterix = ''
        for i in range(len(line) - 1):
            line_without_last_asterix = line_without_last_asterix + line[i]
        return CheckPatternsEquality(line_without_last_asterix)
    elif len(line) % 2 == 0:  # если длина входной строки четная  то определить насколько она делится нацело и для соответственных длин элементов произвести проверку
        return CheckPatternsEquality(line)
