def missing_number(nums):
    """
    Реализовать функцию (или тело функции), которая находит единственное отсутствующее число из последовательности натуральных чисел 1,2,…,n.
    
    Время: O(n), Память: O(1)
    """
    n = len(nums) + 1
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    return expected_sum - actual_sum


def test():
    test_cases = [
        [1, 2, 3, 4, 5, 6, 8, 9, 10, 11],
        [1, 2, 3, 5],
        [2, 3, 4, 5],
        [1, 2, 3, 4],
        [1]
    ]
    
    for nums in test_cases:
        result = missing_number(nums)
        print(f"{nums} -> {result}")


if __name__ == "__main__":
    test()
