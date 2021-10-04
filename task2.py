def odometer(oksana): 
    
    distance = 0
            
    for i in range(len(oksana)):
        
        if i == 1:
            
            distance = distance + oksana[i] * oksana[i-1]
        
        elif i % 2 != 0:
            
            distance = distance + oksana[i-1] * (oksana[i] - oksana[i-2])            
            
    return distance
