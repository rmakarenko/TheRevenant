def belochka(n):
    
    if (n == 0 or n ==1): # в случае 0 или 1 на входе сразу же вернем 1
        return 1  
    
    f = 1 # в этом блоке найдем факториал числа
    for i in range(1, n + 1):
        f = f * n
        n = n - 1
        
    while f > 9: # найдем первую цифру факториала
        f = f // 10
        
    if (n - int(n) == 0 and n >= 0):
        return f 
