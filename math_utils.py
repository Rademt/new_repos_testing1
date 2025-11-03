def factorial(n):
    """Обчислення факторіалу нашого числа"""
    if n < 0:
        raise ValueError("Факторіал не визначений для від’ємних наших чисел")
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def average(numbers):
    """Повертає середнє арифметичне списку наших чисел"""
    if not numbers:
        raise ValueError("Список не може бути порожнім!")
    return sum(numbers) / len(numbers)
