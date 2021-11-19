def MisterRobot(N, data):
    
    position_max = 0  # в этих переменных сохраним позиции трех максимальных чисел массива
    position_mid = 0
    position_min = 0

    for i in range(N):  # определим порядок трех наибольших элементов входного массива
        if data[i] == N:
            position_max = i
            continue
        elif data[i] == N - 1:
            position_mid = i
            continue
        elif data[i] == N - 2:
            position_min = i
            continue

    if position_max > position_mid and position_mid > position_min:
        return True
    elif position_mid > position_min and position_mid > position_max:
        return True
    elif position_min > position_max and position_max > position_mid:
        return True
    else:
        return False
