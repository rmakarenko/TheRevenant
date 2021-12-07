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
    current_sublist = []
    current_list = []

    for i in range(len(unique)):  # put 0 for every unique element
        unique_amount.append(0)

    for i in range(len(s)):
        for j in range(len(unique)):
            if s[i] == unique[j]:
                unique_amount[j] = unique_amount[j] + 1  # now we have the list with amounts of all unique elements

    if len(unique_amount) == 1:
        return True

    if len(unique_amount) == 2 and unique_amount[0] - unique_amount[1] <= 1 and unique_amount[1] - unique_amount[0] >= -1:
        return True
    elif len(unique_amount) == 2 and unique_amount[0] - unique_amount[1] > 1 or unique_amount[1] - unique_amount[0] < -1:
        return False

    unique_amount.sort(reverse=True)

    unique_from_amounts = UniqueList(unique_amount)

    for i in range(len(unique_from_amounts)):  # in this block we will get the lists with unique amounts
        for j in range(len(unique_amount)):
            if unique_from_amounts[i] == unique_amount[j]:
                current_sublist.append(unique_from_amounts[i])
        current_list.append(current_sublist)
        current_sublist = []

    if len(current_list) > 2:
        return False
    elif len(current_list) == 1:
        return True
    elif len(current_list[0]) > 1 and len(current_list[1]) > 1:
        return False
    elif len(current_list[0]) == 1 and (current_list[0][0]) == 1:
        return True
    elif len(current_list[1]) == 1 and (current_list[1][0]) == 1:
        return True
    elif len(current_list[0]) == 1 and (current_list[0][0]) - 1 == current_list[1][0]:
        return True
    elif len(current_list[1]) == 1 and (current_list[1][0]) - 1 == current_list[0][0]:
        return True
