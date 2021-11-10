def TrafficLigth(red, green, time):  # функция возвращает задержку, на данном светофоре
    delay = 0
    while (time > red + green):  # вычесть целое количество раз, попадающих на полный цикл смены цветов
        time = time - (red + green)
    if time == 0 or time == red + green:
        delay = red
    elif time < red:
        delay = red - time
    return delay

def Unmanned(L, N, track):

    time = 0  # переменная для хранения времени пути
    roadmap = []  # список будет моделировать дорогу
    output = []

    for i in range(L): # заполнить по длине дороги единицами список
        roadmap.append(0)

    print(roadmap)

    for i in range(N):  # добавить в него данные о светофорах
        roadmap[track[i][0] - 1] = str(track[i][1]) + ' ' + str(track[i][1])

    print(roadmap)

    for i in range(len(roadmap)):   # пройти по массиву и определить, насколько задержит каждый светофор
        if roadmap[i] == 0:
            time = time + 1
            output.append(1)
        else:
            red = int(roadmap[i].split(' ')[0])
            green = int(roadmap[i].split(' ')[1])
            time = time + TrafficLigth(red, green, time)
            output.append(TrafficLigth(red, green, time))

    print('итоговый аутпут выглядит так ', output)

    for i in range(len(output)):
        time = time + output[i]

    return time

print(Unmanned(10, 2, [[3,5,5],[5,2,2]]))
