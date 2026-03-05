def prime_factors_simple(n: int) -> list:
    """
    Реализовать функцию (или тело функции), которая при введении натурального числа n разбивает его на простые множители (представить его в виде простых чисел).
    
    Время: O(√n), Память: O(log n)
    """
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
