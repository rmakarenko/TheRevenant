def ShopOLAP(N, items_input):

    if len(items_input) == 1:
        return items_input

    items = items_input
    dublicates = []
    dublicates_sales = []
    dublicates_numbers = []
    unique_from_dublicates = []
    unique_sales_from_dublicates = []
    names = []
    sales = []
    unique = []
    unique_sales = []
    unique_numbers = []  # при поиске уникальных элементов в этом списке сохраним их индексы для дальнейшего применения
    final_sorted = []
    final_transformed = []
    string_sorted = []
    final_items_string = []
    final_items = []
    final_sales = []
    final_together = []

    for i in range(N):  # пройдем по всему входному массиву и сформируем из него два массива - с наименованиями и продажами

        element = items[i].split(' ')
        names.append(element[0])  # now we have 2 lists - with items names and with number of sales names = [] and sales = []
        sales.append(element[1])

    for i in range(N):  # walktrough the names and find the unique ones. remember the index, save them with sales to the separate list and then delete them from the items list
        element = names[i]
        for j in range(N):
            if names[j] == element and j == N - 1 and j == i:   # случай, когда уникальный элемент последний в списке
                unique.append(element)
                unique_sales.append(sales[i])
                unique_numbers.append(i)  # и соответствующие индексы в unique_numbers
            elif i == j:  # in case of coincidence of the i and indexes skip the j iteration
                continue
            elif names[j] == element:  # если элемент совпал с любым другим из массива - он не уникален, переходим к следующей итерации цикла i
                break
            elif names[j] != element and j == N - 1:   # в случае нахождения уникальных элементов добавим их в массив unique и соответствующие продажи в unique_sales
                unique.append(element)
                unique_sales.append(sales[i])
                unique_numbers.append(i)  # и соответствующие индексы в unique_numbers

    # now we have 3 more lists, filled in with the data about unique items
    if len(unique) > 0:

        for i in range(len(names)):  # find all duplicate items in the list, save them in another lists like has been done with the unique items
            for j in range(len(unique)):
                if names[i] == unique[j]:
                    break
                elif names[i] != unique[j] and j == len(unique) - 1:
                    dublicates.append(names[i])
                    dublicates_sales.append(sales[i])
                    dublicates_numbers.append(i)
    else:
        for i in range(len(items)):
            dublicates.append(names[i])
            dublicates_sales.append(sales[i])
            dublicates_numbers.append(i)

    if len(dublicates) > 1:
        unique_from_dublicates.append(dublicates[0])

    for i in range(1,len(dublicates)):  # walkthrough the list of dublicates and find all unique elements, write them to the separate list
        for j in range(len(unique_from_dublicates)):
            if dublicates[i] == unique_from_dublicates[j]:
                break
            elif dublicates[i] != unique_from_dublicates[j] and j == len(unique_from_dublicates) - 1:
                unique_from_dublicates.append(dublicates[i])

    # print('уникальные среди дубликатов', unique_from_dublicates)

    for i in range(len(unique_from_dublicates)):  # count the sum of sales for unique from dublicates
        sum_sales = 0
        for j in range(len(dublicates)):
            if unique_from_dublicates[i] == dublicates[j]:
                sum_sales = sum_sales + int(dublicates_sales[j])
        unique_sales_from_dublicates.append(sum_sales)

    for i in range(len(unique)):  # gather the data to ungrouped lists
        final_items.append(unique[i])
        final_sales.append(unique_sales[i])

    for j in range(len(unique_from_dublicates)):
        final_items.append(unique_from_dublicates[j])
        final_sales.append(unique_sales_from_dublicates[j])

    for i in range(len(final_items)):
        final_together.append(final_items[i])
        final_together.append(final_sales[i])

    if len(final_together) == 2:
        standalone = []
        standalone.append(str(final_together[0] + ' ' + str(final_together[1])))
        return standalone

    for i in range(len(final_items)):  # create a string list
        buffer_string = ''
        buffer_string = buffer_string + str(final_items[i]) + ' ' + str(final_sales[i])
        final_items_string.append(buffer_string)

    N = len(final_items_string)  # sort them by the sales amount
    for i in range(N - 1):
        for j in range(N - i - 1):
            if int(final_items_string[j].split(' ')[1]) < int(final_items_string[j + 1].split(' ')[1]):
                final_items_string[j], final_items_string[j + 1] = final_items_string[j + 1], final_items_string[j]

    for i in range(len(final_items_string) - 1):   # handle same sales with lexicography order
        if final_items_string[i].split(' ')[1] != final_items_string[i + 1].split(' ')[1] and i != len(final_items_string) - 2:
            string_sorted.append(final_items_string[i])
            string_sorted.sort()
            final_sorted.append(string_sorted)
            string_sorted = []
        elif final_items_string[i].split(' ')[1] == final_items_string[i + 1].split(' ')[1] and i != len(final_items_string) - 2:
            string_sorted.append(final_items_string[i])
        elif final_items_string[i].split(' ')[1] == final_items_string[i + 1].split(' ')[1] and i == len(final_items_string) - 2:
            string_sorted.append(final_items_string[i])
            string_sorted.append(final_items_string[i + 1])
            string_sorted.sort()
            final_sorted.append(string_sorted)
        elif final_items_string[i].split(' ')[1] != final_items_string[i + 1].split(' ')[1] and i == len(final_items_string) - 2:
            string_sorted.append(final_items_string[i])
            string_sorted.sort()
            final_sorted.append(string_sorted)
            string_sorted = []
            string_sorted.append(final_items_string[i + 1])
            final_sorted.append(string_sorted)

    for i in range(len(final_sorted)):
        for j in range(len(final_sorted[i])):
            final_transformed.append(final_sorted[i][j])

    return final_transformed
