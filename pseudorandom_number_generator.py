def generate_random_numbers(quantity):
    """
    Generate pseudo-random numbers using the Linear Congruential Generator (LCG)
    
    Parameters:
    quantity (int): Quantity of random numbers to be generated
    
    Returns:
    list: List with the generated pseudo-random numbers
    """
    a = 1664525
    c = 29381213
    m = 60000000000
    x0 = 522
    
    random_numbers = []
    
    for i in range(quantity):
        x = (a * x0 + c) % m
        uniform = x / m
        random_numbers.append(uniform)
        x0 = x
    
    return random_numbers