"""
Ejercicios Extra de Unit Testing
Jaime C Smith
08/11/2026
"""

import unittest
from unittest.mock import mock_open, patch

from file_reader import read_lines

# -------------------------------------------------------------
# Section 6 – Tests for File Reading with unittest.mock
# -------------------------------------------------------------
# Purpose:
# Test read_lines without creating a real file.
#
# Required test cases:
# - Simulate file content with unittest.mock.
# - Verify the expected lines are returned.
# - Verify FileNotFoundError is raised for a missing file.
# -------------------------------------------------------------


class TestReadLines(unittest.TestCase):
    """
    Test the read_lines function using simulated file operations.
    """

    @patch(
        "builtins.open",
        new_callable=mock_open,
        read_data="First line\nSecond line\nThird line\n",
    )
    def test_read_lines_returns_expected_mocked_lines(self, mocked_open):
        """
        Test read_lines with simulated file content.

        Expected result:
        The function returns three expected lines without creating
        or reading a real file.
        """
        # Arrange
        fake_path = "sample_file.txt"

        # Act
        result = read_lines(fake_path)

        # Assert
        self.assertEqual(
            result,
            ["First line\n", "Second line\n", "Third line\n"],
        )
        mocked_open.assert_called_once_with(fake_path, "r")

    @patch("builtins.open", side_effect=FileNotFoundError)
    def test_read_lines_raises_file_not_found_error(self, mocked_open):
        """
        Test reading a file that does not exist.

        Expected result:
        read_lines raises FileNotFoundError.
        """
        # Arrange
        missing_path = "missing_file.txt"

        # Act and Assert
        with self.assertRaises(FileNotFoundError):
            read_lines(missing_path)

        mocked_open.assert_called_once_with(missing_path, "r")


if __name__ == "__main__":
    unittest.main()