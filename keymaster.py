def Keymaker(k):

    doors = []
    returner = ''

    for i in range(k):
        doors.append(0)

    for j in range(k):
        for i in range(j, len(doors), 1 + j):
            if doors[i] == 1:
                doors[i] = 0
            else:
                doors[i] = 1

    for i in range(len(doors)):
        returner = returner + str(doors[i])

    return returner
