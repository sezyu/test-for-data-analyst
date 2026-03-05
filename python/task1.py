def is_isomorphic(s: str, t: str) -> bool:
    """
    Проверяет, являются ли строки s и t изоморфными
    
    Время: O(n), Память: O(n)
    где n - длина строки
    """
    if len(s) != len(t):
        return False
    
    s_to_t = {}
    t_to_s = {}
    
    for c1, c2 in zip(s, t):
        if c1 in s_to_t:
            if s_to_t[c1] != c2:
                return False
        else:
            s_to_t[c1] = c2
        
        if c2 in t_to_s:
            if t_to_s[c2] != c1:
                return False
        else:
            t_to_s[c2] = c1
    
    return True


if __name__ == "__main__":    

    test_pairs = [
        ('МАМА', 'ПАПА'),
        ('МАМА', 'ПАРА'),
        ('paper', 'title')
    ]
    
    for s, t in test_pairs:
        print(f"is_isomorphic('{s}', '{t}') = {is_isomorphic(s, t)}")
