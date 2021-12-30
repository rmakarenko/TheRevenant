def white_walkers(village):

    positions_with_ten_sum = []
    first_digit = - 2
    first_digit_position = 0
    clean_village = []  #  here we ll store the input string without letters

    if len(village) == 0:
        return False

    for i in range(len(village)):
        if village[i] == '0' or village[i] == '1' or village[i] == '2' or village[i] == '3' or village[i] == '4' or village[i] == '5' or village[i] == '6' or village[i] == '7' or village[i] == '8' or village[i] == '9':
            clean_village.append(int(village[i]))  # after this cycle we have only digits and equal signs
        elif village[i] == '=':
            clean_village.append(- 1)

    for i in range(len(clean_village)) :
        if clean_village[i] == - 1:
            continue
        elif first_digit == - 2:  # finding the first time first digit
            first_digit = clean_village[i]
            first_digit_position = i
        elif first_digit + clean_village[i] == 10:
            current_positions = [first_digit_position, i]
            positions_with_ten_sum.append(current_positions)
            first_digit = clean_village[i]
            first_digit_position = i
        else:  # this case occurs when sum != 10
            first_digit = clean_village[i]
            first_digit_position = i

    if len(positions_with_ten_sum) == 0:
        return False

    for i in range(len(positions_with_ten_sum)):
        walkers_count = 0
        for j in range(positions_with_ten_sum[i][0] + 1, positions_with_ten_sum[i][1]):
            if clean_village[j] == - 1:
                walkers_count = walkers_count + 1
        if walkers_count != 3:
            return False

    return True
