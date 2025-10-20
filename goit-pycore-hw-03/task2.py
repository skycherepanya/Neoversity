import random

def get_numbers_ticket(min_v, max_v, qty):
    if min_v < 1 or max_v > 1000 or min_v > max_v:
        return []
    
    range_size = max_v - min_v + 1
    if qty < 1 or qty > range_size:
        return []
    
    range_v = range(min_v, max_v + 1)
    picked = random.sample(range_v, qty) 
    
    return sorted(picked)   


print(get_numbers_ticket(1, 99, 77))

