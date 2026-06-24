"""
Ejercicios de Funciones
Jaime C Smith
05/25/2026
"""

# 6) Create a function that accepts a list of numbers and returns a list
#    with only the prime numbers.
#
#    Example:
#    [1, 4, 6, 7, 13, 9, 67] -> [7, 13, 67]
#
#    Tip 1: Think about the mathematical logic to check if a number is prime,
#           then convert that logic into code.
#    Tip 2: Use a helper function to check if a number is prime.
#           The main function will:
#           - iterate over the list,
#           - check if each number is prime,
#           - and add it to a new list if it is.


def is_prime(number):
    """
    Return True if 'number' is a prime number, False otherwise.

    Prime definition used:
    - A prime is greater than 1.
    - It has no positive divisors other than 1 and itself.
    """
    # 0, 1 and negative numbers are not prime
    if number <= 1:
        return False

    # We only need to check divisors up to the square root of number,
    # but to keep it simple for class, we can check up to number - 1.
    # (You can optimize later to use int(math.sqrt(number)) if desired.)
    for divisor in range(2, number):
        if number % divisor == 0:
            # If divisible by any number other than 1 and itself,
            # it is not prime
            return False

    # If no divisor divides the number evenly, it is prime
    return True


def get_prime_numbers(numbers):
    """
    Given a list of integers 'numbers', return a new list containing
    only the prime numbers.
    """
    prime_list = []

    for number in numbers:
        if is_prime(number):
            prime_list.append(number)

    return prime_list


# Example usage
example_numbers = [1, 4, 6, 7, 13, 9, 67]
primes = get_prime_numbers(example_numbers)
print("Original list:", example_numbers)
print("Prime numbers:", primes)