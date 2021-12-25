def maximum(massive, start, finish):
    max = massive[start]
    for i in range(start, finish + 1):
        if massive[i] > max:
            max = massive[i]
    return max

def Transform(A, N):
    B = []
    for i in range(len(A)):
        for j in range(len(A) - i):
            k = i + j
            B.append(maximum(A, j, k))
    return B

def TransformTransform(A, N):

    sum = 0

    B = Transform(A, N)
    B = Transform(B, N)

    for i in range(len(B)):
        sum = sum + B[i]

    if sum % 2 == 0:
        return True
    else:
        return False
