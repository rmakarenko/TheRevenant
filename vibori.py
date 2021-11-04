def Rounder3(number):  # в этой функции округлим до третьего знака дробную часть числа

    rounded = str(int(number)) + '.'
    fractional = str(number).split('.')[1]

    if len(fractional) > 3:
        for i in range(3):
            if i == 2 and int(fractional[3]) > 5:
                rounded = rounded + str(fractional[2] + '1')
            if i == 2 and int(fractional[3]) <= 5:
                rounded = rounded + str(fractional[2])
            else:
                rounded = rounded + str(fractional[i])

    return float(rounded)


def Max1Max2(Votes):
    first = 0
    second = 0
    first_i = 0
    second_i = 0

    for i in range(len(Votes)):  # проходим по массиву и сравниваем текущий элемент с максимумом и вторым числом
        if (Votes[i] > first):
            second = first
            first = Votes[i]
            second_i = first_i
            first_i = i
        elif (Votes[i] > second):
            second = Votes[i]
            second_i = i

    return first, first_i, second, second_i  # а выход отдаем значения и номера первого и второго максимальных кандидатов


def MassVote(N, Votes):
    if len(Votes) == 1:
        return "majority winner 1"

    total_votes = 0  # посчитаем общее количество голосов
    for i in range(N):
        total_votes = total_votes + Votes[i]

    # найдем кандидата, который получил больше всех голосов, кандидата на втором месте и их порядковые номера с помощью функции
    first_votes = Max1Max2(Votes)[0]
    second_votes = Max1Max2(Votes)[2]
    first_number = Max1Max2(Votes)[1]

    # вычислим и округлим до третьего знака значения их процентов
    first_percents = first_votes * 100 / total_votes
    second_percents = second_votes * 100 / total_votes
    rounded_first_percents = Rounder3(first_percents)
    rounded_second_percents = Rounder3(second_percents)

    # проверим, какое из условий выполняется

    if rounded_first_percents == rounded_second_percents:

        return "no winner"

    elif (rounded_first_percents > 50):

        return "majority winner" + ' ' + str(first_number + 1)

    else:

        return "minority winner" + ' ' + str(first_number + 1)
