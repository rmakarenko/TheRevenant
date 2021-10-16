def Cutter(string, length):

    cutted_string = []
    current = ''
    starting_point = 0

    for i in range(len(string)//length):  # в этом блоке нарежем на целые части строку, останется обрезок, меньше ширины
        starting_point = i * length
        for j in range(starting_point, length + starting_point):  # проходим по части длинной строки, и отправляем эту часть в выходной результат
            current = current + string[j]
        cutted_string.append(current)
        current = ''  # обнулим текущую строку

    starting_point_of_leftover = starting_point + length  # на этой позиции расположится начало остаточной строки

    if len(string) % length > 0:
        for k in range(starting_point_of_leftover, len(string)):  # проходим по обрезку строки, и отправляем эту часть в выходной результат
            current = current + string[k]
        cutted_string.append(current)

    return cutted_string

def substring_search(string, substring):
    for j in range(len(string) - len(substring) + 1):  # позиции дальше не вместят подстроку по длине
        for k in range(len(substring)):
            if (string[j + k] == substring[k] and k == len(substring) - 1):
                return True
            elif (string[j + k] != substring[k]):
                break
    return False

def WordSearch(length, s, subs):

    output_list = []
    lst = s.split()
    free_cells_counter = length
    words_in_string = 0
    current_working_string = ''
    output_list2 = []
    output_list3 = []  # сюда запишем последовательность из единиц и нолей

    for i in range(len(lst)):  # проходим по входной строке, разбивая ее сплитом на составляющие слова, их записываем в список
        if len(lst[i]) <= length:     # если слово короче ширины - включаем его в выходной список
            output_list.append(lst[i])
        else:         # если длиннее - то разбивает вызванным методом на части и их включаем в выходной список
            for j in range(len(Cutter(lst[i], length))):
                output_list.append(Cutter(lst[i], length)[j])  # по итогу получаем список слов, разбитых по длине

    for i in range(len(output_list)):  # теперь пройдем по списку из нарезанных слов и расположим помещающиеся слова в общие строки
        if len(output_list[i]) > free_cells_counter:  # слово не помещается - переходим на следующую строку
            free_cells_counter = length   # обнуляем счетчик свободных ячеек, так как предполагается переход на следующую строку
            words_in_string = 0  # так как переходим на новую строку - то обнулим счетчик слов
            output_list2.append(current_working_string)  # запишем в результат то, что уже находится в текущей строке
            current_working_string = ''  # обнуляем текущую рабочую строку, так как предполагается переход на следующую строку
            current_working_string = current_working_string + output_list[i] + ' '  # запишем текущее слово и пробел в рабочую строку
            free_cells_counter = free_cells_counter - len(output_list[i]) - 1 # уменьшим счетчик свободных ячеек на длину записанного слова и на один пробел
            words_in_string = 1
        elif len(output_list[i]) < free_cells_counter and words_in_string == 0: # первое слово в строке, по длине меньше строки и строка влезает
            current_working_string = output_list[i] + ' ' # тогда запишем текущее слово в рабочую строку
            free_cells_counter = free_cells_counter - len(output_list[i]) - 1 # уменьшим счетчик слов на длину записанного слова и еще один пробел после него
            words_in_string = words_in_string + 1
        elif len(output_list[i]) == free_cells_counter and words_in_string == 0:  # первое слово в строке и строка влезает впритык
            current_working_string = output_list[i]  # тогда запишем текущее слово в рабочую строку
            output_list2.append(current_working_string)  # добавим в результирующий список текущую строку
            free_cells_counter = length  # уменьшим счетчик слов на длину записанного слова и еще один пробел после него
            words_in_string = 0
        elif len(output_list[i]) <= free_cells_counter and words_in_string > 0:   # слово влезает, но оно в строке не первое - добавляем пробелы в условие
            current_working_string = current_working_string + output_list[i] + ' '
            words_in_string = words_in_string + 1
            free_cells_counter = free_cells_counter - len(output_list[i]) - words_in_string + 1

    for i in range(len(output_list2)):
        Contains = 0
        substrings = output_list2[i].split()  # каждый элемент разобьем на подстроки
        for j in range(len(substrings)):
            if substrings[j] == subs:
                Contains = 1
                break
        output_list3.append(Contains)

    return output_list3
