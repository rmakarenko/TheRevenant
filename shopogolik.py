def bubble_sort(nums):  # отсортируем список по убыванию
    swapped = True  # Устанавливаем swapped в True, чтобы цикл запустился хотя бы один раз
    while swapped:
        swapped = False
        for i in range(len(nums) - 1):
            if nums[i] < nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]  # Меняем элементы
                swapped = True  # Устанавливаем swapped в True для следующей итерации
    return nums

def MaximumDiscount(N, price):
    if N < 3:
        return 0
    elif N >= 3 and N < 6:
        return bubble_sort(price)[2]
    elif N == 6:
        return bubble_sort(price)[2] + bubble_sort(price)[5]
    elif N >= 7:
        discount = 0
        for i in range(N // 3):
            discount = discount + bubble_sort(price)[i * 3 + 2]
        return discount
