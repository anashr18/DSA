import pytest
from palindrome.validpalindrome import is_palindrom
from palindrome.validpalindrome_cases import test_cases

@pytest.mark.parametrize("input_str,expected", test_cases)
def test_is_palindrom(input_str, expected):
    assert is_palindrom(input_str) == expected
