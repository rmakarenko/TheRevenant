def UniqueList(s):

    unique = [s[0]]
    for i in range(len(s)):  #  this block creates the list of the unique elements of the string
        for j in range(len(unique)):
                if s[i] != unique[j] and j == len(unique) - 1:
                    unique.append(s[i])
    return unique

def SherlockValidString(s):

    unique = UniqueList(s)
    unique_amount = []
    current_list = []
    delta_one = 0

    for i in range(len(unique)):  # put 0 for every unique element
        unique_amount.append(0)

    for i in range(len(s)):
        for j in range(len(unique)):
            if s[i] == unique[j]:
                unique_amount[j] = unique_amount[j] + 1  # now we have the list with amounts of all unique elements

    if len(unique_amount) == 1:
        return True

    if len(unique_amount) == 2 and unique_amount[0] - unique_amount[1] <= 1 and unique_amount[0] - unique_amount[1] >= -1:
        return True
    elif len(unique_amount) == 2 and unique_amount[0] - unique_amount[1] > 1 or unique_amount[0] - unique_amount[1] < -1:
        return False

    unique_amount.sort(reverse=True)

    unique_from_amounts = UniqueList(unique_amount)

    for i in range(len(unique_from_amounts)):  # in this block we will get the lists with unique amounts
        for j in range(len(unique_amount)):
            if unique_from_amounts[i] == unique_amount[j]:
                current_list.append(unique_from_amounts[i])

    current_list.sort(reverse=True)

    for i in range(len(current_list) - 2):
        if current_list[i] - current_list[i + 1] > 1:
            return False
        elif current_list[i] - current_list[i + 1] == 1:
            delta_one = delta_one + 1

    if delta_one < 2:
        return True
