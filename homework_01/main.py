"""
Домашнее задание №1
Функции и структуры данных
"""

# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"

def power_numbers(*numbers):
    return [n ** 2 for n in numbers]
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """

def filter_is_odd(n):
    if n % 2 != 0:
        return True 
    return False

def filter_is_even(n):
    if n % 2 == 0:
        return True 
    return False

def filter_is_prime(n):
    if n < 2:
        return False
    for i in range(2, int((n ** 0.5)) + 1):
        if n % i == 0:
            return False
    return True

functions = {
    ODD: filter_is_odd, 
    EVEN: filter_is_even, 
    PRIME: filter_is_prime
}

def filter_numbers(numbers, filter_type):
    return list(filter(functions[filter_type], numbers))
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """
