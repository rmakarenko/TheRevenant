def massive_search(i, j):  # функция принимает на вход координаты карты, где располагается элемент, совпадающий с первым элементом танков
    current_list = []
    total_karta = []
    for i in range(H2):  # создадим отдельный массив чтобы не использовать всю карту
        for j in range(W2):
            current_list.append(karta[i][j])
        total_karta.append(current_list)
        current_list = []
    for i in range(H2):
        for j in range(W2):
            if total_karta[i][j] != tanks[i][j]:
                return False
    return True

def string_to_massive(H1, string):  # эта функция превратит строку в двумерный массив
    total_list = []
    for i in range(H1):
        current_list = string.split(' ')[i]
        total_list.append(current_list)
    return total_list

def TankRush(h1, w1, S1, h2, w2, S2):

    global H1
    H1 = h1
    global H2
    H2 = h2
    global W1
    W1 = w1
    global W2
    W2 = w2

    global karta
    karta = string_to_massive(H1, S1)  # превратим входные строки в двумерные массивы для удобства операций с ними
    global tanks
    tanks = string_to_massive(H2, S2)
    for i in range(H1 - H2 + 1):  # позиции дальше не вместят искомый массив по количеству строк
        for j in range(W1 - W2 + 1):  # позиции дальше не вместят искомый массив по количеству строк
            if karta[i][j] == tanks[0][0] and massive_search(i, j):  # если текущий элемент карты равен первому элементу танков то вызовем функцию, которая проверит равенство массива, лежащего за этой точкой с искомым
                return True
    return False

