"""
Unit Testing Exercises
Jaime C Smith
08/07/2026
"""

from functions_exercises import (
    count_uppercase_and_lowercase,
    get_prime_numbers,
    reverse_string,
    sort_hyphen_separated_words,
    sum_list_numbers,
)

# -------------------------------------------------------------
# Section 4 – Unit Tests for Functions Exercises 3 Through 7
# -------------------------------------------------------------
# The requirement is three successful test cases for each function.
# Exercises 1 and 2 are intentionally not tested.
# -------------------------------------------------------------


# -------------------------------------------------------------
# Exercise 3 – Tests for sum_list_numbers
# -------------------------------------------------------------

def test_sum_list_numbers_with_positive_values():
    # Arrange
    input_list = [4, 6, 2, 29]

    # Act
    result = sum_list_numbers(input_list)

    # Assert
    assert result == 41


def test_sum_list_numbers_with_negative_values():
    # Arrange
    input_list = [-5, 10, -2, 7]

    # Act
    result = sum_list_numbers(input_list)

    # Assert
    assert result == 10


def test_sum_list_numbers_with_empty_list():
    # Arrange
    input_list = []

    # Act
    result = sum_list_numbers(input_list)

    # Assert
    assert result == 0


# -------------------------------------------------------------
# Exercise 4 – Tests for reverse_string
# -------------------------------------------------------------

def test_reverse_string_with_regular_text():
    # Arrange
    text = "Hello world"

    # Act
    result = reverse_string(text)

    # Assert
    assert result == "dlrow olleH"


def test_reverse_string_with_one_character():
    # Arrange
    text = "A"

    # Act
    result = reverse_string(text)

    # Assert
    assert result == "A"


def test_reverse_string_with_empty_text():
    # Arrange
    text = ""

    # Act
    result = reverse_string(text)

    # Assert
    assert result == ""


# -------------------------------------------------------------
# Exercise 5 – Tests for count_uppercase_and_lowercase
# -------------------------------------------------------------

def test_count_uppercase_and_lowercase_with_mixed_text():
    # Arrange
    text = "I love Nación Sushi"

    # Act
    result = count_uppercase_and_lowercase(text)

    # Assert
    assert result == (3, 13)


def test_count_uppercase_and_lowercase_with_uppercase_only():
    # Arrange
    text = "HELLO"

    # Act
    result = count_uppercase_and_lowercase(text)

    # Assert
    assert result == (5, 0)


def test_count_uppercase_and_lowercase_with_lowercase_only():
    # Arrange
    text = "python"

    # Act
    result = count_uppercase_and_lowercase(text)

    # Assert
    assert result == (0, 6)


# -------------------------------------------------------------
# Exercise 6 – Tests for sort_hyphen_separated_words
# -------------------------------------------------------------

def test_sort_hyphen_separated_words_with_five_words():
    # Arrange
    text = "python-variable-function-computer-monitor"

    # Act
    result = sort_hyphen_separated_words(text)

    # Assert
    assert result == "computer-function-monitor-python-variable"


def test_sort_hyphen_separated_words_with_three_words():
    # Arrange
    text = "zebra-apple-monkey"

    # Act
    result = sort_hyphen_separated_words(text)

    # Assert
    assert result == "apple-monkey-zebra"


def test_sort_hyphen_separated_words_with_one_word():
    # Arrange
    text = "python"

    # Act
    result = sort_hyphen_separated_words(text)

    # Assert
    assert result == "python"


# -------------------------------------------------------------
# Exercise 7 – Tests for get_prime_numbers
# -------------------------------------------------------------

def test_get_prime_numbers_with_mixed_numbers():
    # Arrange
    input_list = [1, 4, 6, 7, 13, 9, 67]

    # Act
    result = get_prime_numbers(input_list)

    # Assert
    assert result == [7, 13, 67]


def test_get_prime_numbers_with_no_prime_numbers():
    # Arrange
    input_list = [1, 4, 6, 8, 9, 10]

    # Act
    result = get_prime_numbers(input_list)

    # Assert
    assert result == []


def test_get_prime_numbers_with_all_prime_numbers():
    # Arrange
    input_list = [2, 3, 5, 7, 11]

    # Act
    result = get_prime_numbers(input_list)

    # Assert
    assert result == [2, 3, 5, 7, 11]