def MadMax(N, Tele):

    back = []
    for i in range(N):
        back.append(0)

    # считать входной массив отсортировать его по возрастанию
    for i in range((len(Tele) - 1)):
        for j in range((len(Tele) - 1)):
            if Tele[j] > Tele[j + 1]:
                Tele[j],Tele[j + 1] = Tele[j + 1],Tele[j]

    # записать первую половину в первую половину выходного сигнала
    fulfilled = int(len(Tele)/2)
    for i in range(fulfilled):
        back[i] = Tele[i]

    left_to_fulfill = len(Tele) - int(len(Tele)/2)

    for i in range(left_to_fulfill): # заполним вторую половину
        back[fulfilled + i] = Tele[len(Tele) - i - 1]

    return back
