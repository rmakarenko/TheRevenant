def positions_checker(F):

    right_positions = []  # walkthrough the massive and find the elements, that are not sorted, create the massive with booleans
    false_counter = 0
    false_positions = []

    for i in range(len(F) - 1):  # handle all elements, except last
        if F[i] < F[i + 1]:
            right_positions.append(True)
        else:
            right_positions.append(False)
            false_positions.append(i)
            false_counter = false_counter + 1

    if F[len(F) - 1] > F[len(F) - 2]:  # handling the last element
        right_positions.append(True)
    else:
        right_positions.append(False)
        false_positions.append(len(F) - 1)
        false_counter = false_counter + 1

    return right_positions, false_counter, false_positions


def Football(F, N):

    false_counter = positions_checker(F)[1]
    false_positions = positions_checker(F)[2]

    if false_counter == 2:  # in case, if there are only 2 False in right positions - change that elements
        F[false_positions[0]], F[false_positions[1]] = F[false_positions[1]], F[false_positions[0]]

    if positions_checker(F)[1] == 0:  # if changing two elements helped - return True
        return True
    else:  # in case it did not - return the initial order
        F[false_positions[0]], F[false_positions[1]] = F[false_positions[1]], F[false_positions[0]]

    for i in range(len(false_positions) - 1):  # check, that all False elements are neighbours
        if false_positions[i + 1] - false_positions[i] > 1:
            return False

    # all false elements are neighbours, sort them and return back sorted

    unsorted_elements = []

    for i in range(len(false_positions)):
        unsorted_elements.append(F[false_positions[i]])

    unsorted_elements.sort()

    for i in range(len(false_positions)):
        F[false_positions[i]] = unsorted_elements[i]

    if positions_checker(F)[1] == 0:  # if changing two elements helped - return True
        return True

    return False
