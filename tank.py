def substring_search(string, substring):
    for j in range(len(string) - len(substring) + 1):  # позиции дальше не вместят подстроку по длине
        for k in range(len(substring)):
            if (string[j + k] == substring[k] and k == len(substring) - 1):
                return True
            elif (string[j + k] != substring[k]):
                break
    return False

def string_to_massive(H1, W1, string):  # эта функция превратит строку в двумерный массив
    total_list = []
    current_list = []
    for i in range(H1):
        for j in range(W1):
            current_list.append(string[j + i * W1])
        total_list.append(current_list)
        current_list = []
    return total_list

def TankRush(H1, W1, S1, H2, W2, S2):

    TwoDMap = string_to_massive(H1, W1, S1)  # на входе программы подаются строки, поэтому сначала превратим их в двумерные массивы
    TwoDTanks = string_to_massive(H2, W2, S2)

    length_map = len(S1)  # определим длины масиивов в символах, не во вложенных массивах
    length_tanks = len(S2)
    amount_of_entries = []   # в этом массиве сохраним количество вхождений для каждого элемента S2, в виде числа
    for i in range(len(TwoDTanks)):
        amount_of_entries.append(0)  # заполним нолями массив

    if length_tanks > length_map:  # ecли массив для поиска больше карты - сразу вернем False
        return False

    for i in range(H1):
        for j in range(H2):
            if substring_search(TwoDMap[i], TwoDTanks[j]):
                amount_of_entries[j] = amount_of_entries[j] + 1

    for i in range(W2):
        if amount_of_entries[i] == 0:
            return False

    return True


