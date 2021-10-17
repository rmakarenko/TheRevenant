def SumOfThe(N, data):

    sum1 = 0  # в этих переменных будем хранить числа, проверяемые на бытность суммой
    sum2 = 0
    is_there_a_sum = False

    for i in range(N):
        sum1 = data[i]
        for j in range(N):
            if j != i:
                sum2 = sum2 + data[j]
        if sum1 == sum2:
            is_there_a_sum = True
            break
        sum2 = 0

    if is_there_a_sum:

        return sum1
