def SmallestToTheLeft (data, delta, position_input):
    current_list = data
    # buffer_variable = 0
    position = position_input
    while delta >= 2:
        buffer_variable = current_list[position]
        current_list[position] = current_list[position - 1]  # смещаем влево на 2
        current_list[position - 1] = current_list[position -2]
        current_list[position - 2] = buffer_variable
        position = position - 2
        delta = delta - 2
    if delta == 1:  # если дельта станет единицей - сместим на единицу влево
        buffer_variable = current_list[position]
        current_list[position] = current_list[position + 1]  # смещаем влево на 1
        current_list[position + 1] = current_list[position - 1]
        current_list[position - 1] = buffer_variable
    return current_list

def MisterRobot(N, data_input):

    data = data_input
    minimum = 1  # для наглядности будем хранить в переменных и текущий искомый минимум и его позицию
    minimum_position = 0
    delta = 0  # сохраним здесь разницу между текущей позицией и

    for i in range(N - 3):  # пройдем по части массива, переставляя минимальные числа влево
        for j in range(N):
            if data[j] != minimum:  # если элемент не равен текущему минимуму - перейдем к следующей итерации цикла j
                continue
            elif data[j] == minimum and j == minimum_position:  # найдем элемент = текущему минимуму и проведем проверку, на своем ли он месте
                minimum = minimum + 1  # если элемент на своем месте - то увеличиваем искомый минимум и его позицию и идем дальше по итерации цикла i
                minimum_position = minimum_position + 1
                break
            elif data[j] == minimum and j > minimum_position:  # элемент равен текущему минимуму и находится не на своем месте
                delta = j - minimum_position
                data = SmallestToTheLeft(data, delta, j)  # вызовем функцию перестановщик c параметром delta, чтобы сместить элемент на позицию минимума
                minimum = minimum + 1  # если элемент на своем месте - то оставляем все, как есть и идем дальше по итерации цикла i
                minimum_position = minimum_position + 1  # увеличение текущего минимума, переход к следующей итерации

    if data[N - 1] > data[N - 2] and data[N - 1] > data[N - 3]:  # на данном этапе выполнения программы в массиве data содержится входной массив, отсортированный кроме трех последних элементов
        return True
    elif data[N - 2] > data[N - 3] and data[N - 3] > data[N - 1]:
        return True
    elif data[N - 3] > data[N - 2] and positiondata[N - 1] > data[N - 2]:
        return True
    else:
        return False
