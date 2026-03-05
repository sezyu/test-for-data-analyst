def prime_factors_simple(n: int) -> list:

    if n < 2:
        return []
    
    factors = []
    divisor = 2
    
    while n > 1:
        if n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        else:
            divisor += 1
    
    return factors


def test_prime_factors_simple():
    
    test_cases = [
        (1),           
        (13),        
        (12),   
        (56), 
        (100), 
    ]
    
    
    for  n in test_cases:
        result = prime_factors_simple(n)
        print(f"{n} -> {result}")


if __name__ == "__main__":

    test_prime_factors_simple()
