def TrafficLigth(red, green, time):  # функция возвращает задержку на данном светофоре
    delay = 1
    while (time > red + green):  # вычесть целое количество раз, попадающих на полный цикл смены цветов (для упрощения рассчетов)
        time = time - (red + green)
    if time == 0 or time == red + green:
        delay = red
    elif time < red:
        delay = red - time
    return delay

def Unmanned(L, N, track):

    time = 0  # переменная для хранения времени пути
    roadmap = []  # список будет моделировать дорогу
    output = []  # в этот список запишем данные о времени движения, включая задержки на светофорах

    for i in range(L):  # заполнить по длине дороги единицами список
        roadmap.append(0)

    for i in range(N):  # добавить в него данные о светофорах
        if (track[i][0] <= L and track[i][0] > 0):
            roadmap[track[i][0] - 1] = str(track[i][1]) + ' ' + str(track[i][1])

    for i in range(len(roadmap)):   # пройти по массиву и определить, насколько задержит каждый светофор
        if roadmap[i] == 0:  # это условие фиксирует отрезки без светофоров
            time = time + 1
            output.append(1)
        else:
            red = int(roadmap[i].split(' ')[0])
            green = int(roadmap[i].split(' ')[1])
            delay = TrafficLigth(red, green, time)
            time = time + delay
            output.append(delay)

    return time
    
