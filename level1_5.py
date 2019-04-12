def PatternUnlock(N, hits):

    sum_hits = 0.0

    for i in range (N - 1):
        
        if abs(hits[i] - hits[i+1]) == 2 or abs(hits[i] - hits[i+1]) == 7:
        
            sum_hits += 1.41421
        
        if (abs(hits[i] - hits[i+1]) == 1 or abs(hits[i] - hits[i+1]) == 3 or
        abs(hits[i] - hits[i+1]) == 6 or abs(hits[i] - hits[i+1]) == 8):
            
            sum_hits += 1.0
            
        if (hits[i] == 6 and hits[i+1] == 1) or (hits[i] == 1 and hits[i+1] == 6):
            
            sum_hits += 1.0
            
        if (hits[i] == 3 and hits[i+1] == 7) or (hits[i] == 7 and hits[i+1] == 3):
            
            sum_hits += 1.0
            
            
        
        if (hits[i] == 6 and hits[i+1] == 2) or (hits[i] == 2 and hits[i+1] == 6):
            
            sum_hits += 1.41421
        
        if (hits[i] == 2 and hits[i+1] == 7) or (hits[i] == 7 and hits[i+1] == 2):
            
            sum_hits += 1.41421
            
        if (hits[i] == 5 and hits[i+1] == 1) or (hits[i] == 1 and hits[i+1] == 5):
            
            sum_hits += 1.41421
            
        if (hits[i] == 3 and hits[i+1] == 8) or (hits[i] == 8 and hits[i+1] == 3):
            
            sum_hits += 1.41421
            
     
    result = int (sum_hits * 100000) 
    
    return int(str(result).replace(str(0), ''))