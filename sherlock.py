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
    delta = 0
    for i in range(len(unique)):  # put 0 for every unique element
        unique_amount.append(0)
    for i in range(len(s)):
        for j in range(len(unique)):
            if s[i] == unique[j]:
                unique_amount[j] = unique_amount[j] + 1  # now we have the list with amounts of all unique elements
    unique_amount.sort(reverse=True)
    if len(unique_amount) == 1:  # f len is 1 it is always true
        return True
    if len(unique_amount) == 2 and (unique_amount[0] == 1 or unique_amount[1] == 1):  # len = 2 and all equal
        return True
    if len(unique_amount) == 2 and (unique_amount[0] - unique_amount[1] <= 1 and unique_amount[0] - unique_amount[1] >= -1):
        return True  # len = 2 and delta less or equal than 1
    elif len(unique_amount) == 2 and (unique_amount[0] - unique_amount[1] > 1 or unique_amount[0] - unique_amount[1] < -1):
        return False # len = 2 and delta more than 1
    for i in range(len(unique_amount) - 2):
        if unique_amount[i] != unique_amount[i + 1]:
            delta = delta + 1
    if delta == 0:
        return True
    if len(unique_amount) > 2 and unique_amount[len(unique_amount) - 1] == 1:  # all equal, one is 1
        for i in range(len(unique_amount) - 2, 1, -1):
            if unique_amount[i] != unique_amount[i - 1]:
                return False
            elif unique_amount[i] == unique_amount[i - 1] and i == 1:
                return True
    if len(unique_amount) > 2 and unique_amount[0] - unique_amount[1] == 1:  # all equal, one is more by 1
        unique_amount[0] = unique_amount[0] - 1
        for i in range(len(unique_amount) - 1):
            if unique_amount[i] != unique_amount[i + 1]:
                return False
            elif unique_amount[i] == unique_amount[i + 1] and i == len(unique_amount) - 2:
                return True
    return False
