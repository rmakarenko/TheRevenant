def SynchronizingTables(N, ids, salary):

    sorted_ids = []
    ids_numbers = []        # поскольку по заданию изменять исходный список ids не полагается - создадим дополнительный список
    salary_to_return = []
    for i in range (N):
        sorted_ids.append(ids[i])

    m = N - 1
    while m > 0:
        for i in range(m):
            if (sorted_ids[i] > sorted_ids[i + 1]):
                x = sorted_ids[i]
                sorted_ids[i] = sorted_ids[i + 1]
                sorted_ids[i + 1] = x
        m = m - 1

    # создать список, который отображает порядковые номера зарплат в порядке изначальной расстановки списка айдишников

    for i in range(N):
        for j in range(N):
            if ids[i] == sorted_ids[j]:
                ids_numbers.append(j)
    m = N - 1
    while m > 0:
        for i in range(m):
            if (salary[i] > salary[i + 1]):
                x = salary[i]
                salary[i] = salary[i + 1]
                salary[i + 1] = x
        m = m - 1

    # теперь заполним список, который пойдет на возврат - расставим зарплаты в требуемом порядке
    for i in range(N):
        salary_to_return.append(salary[ids_numbers[i]])

    return salary_to_return
