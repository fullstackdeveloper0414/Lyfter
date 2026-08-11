"""
Unit Testing Exercises
Jaime C Smith
08/07/2026
"""

import pytest
from bubble_sort import bubble_sort

# -------------------------------------------------------------
# Section 2 – Unit Tests for Bubble Sort
# -------------------------------------------------------------
# Required tests:
# - Works with a small list.
# - Works with a large list containing more than 100 elements.
# - Works with an empty list.
# - Does not work with parameters that are not lists.
# -------------------------------------------------------------


def test_bubble_sort_sorts_a_small_list():
    """
    Test that bubble_sort correctly sorts a small unsorted list.

    Expected outcome:
    [5, 2, 4, 1, 3] becomes [1, 2, 3, 4, 5].
    """
    # Arrange
    input_list = [5, 2, 4, 1, 3]

    # Act
    result = bubble_sort(input_list)

    # Assert
    assert result == [1, 2, 3, 4, 5]


def test_bubble_sort_sorts_a_large_list_over_100_elements():
    """
    Test that bubble_sort correctly sorts a list with more than 100 elements.

    Expected outcome:
    A descending list from 150 to 1 becomes a list from 1 to 150.
    """
    # Arrange
    input_list = list(range(150, 0, -1))
    expected_result = list(range(1, 151))

    # Act
    result = bubble_sort(input_list)

    # Assert
    assert result == expected_result


def test_bubble_sort_returns_an_empty_list_for_empty_input():
    """
    Test that bubble_sort returns an empty list when it receives one.

    Expected outcome:
    [] remains [].
    """
    # Arrange
    input_list = []

    # Act
    result = bubble_sort(input_list)

    # Assert
    assert result == []


def test_bubble_sort_raises_type_error_for_non_list_input():
    """
    Test that bubble_sort raises TypeError for a non-list parameter.

    Expected outcome:
    Passing a string raises TypeError.
    """
    # Arrange
    invalid_input = "not a list"

    # Act and Assert
    with pytest.raises(TypeError):
        bubble_sort(invalid_input)