# Test cases for is_palindrom(s: str)
# Each test case is a tuple: (input_string, expected_output)

test_cases = [
    # Simple palindromes
    ("madam", True),
    ("racecar", True),
    ("12321", True),
    ("A1B2B1a", True),

    # Mixed case palindromes
    ("Madam", True),
    ("RaceCar", True),
    ("Noon", True),

    # Palindromic phrases with spaces and punctuation
    ("A man, a plan, a canal:?><><>< Panama", True),
    ("Was it a car or a cat I saw?", True),
    ("No 'x' in Nixon", True),
    ("Eva, can I see bees in a cave?", True),

    # Non-palindromes
    ("hello", False),
    ("palindrome", False),
    ("abc123", False),
    ("Not a palindrome!", False),

    # Edge cases
    ("", True),  # Empty string is a palindrome
    ("a", True), # Single character
    (" ", True), # Only space
    ("!!!", True), # Only punctuation
    ("A.", True), # Single letter and punctuation

    # Long palindrome
    ("Able was I ere I saw Elba", True),
    ("1" * 1500 + "2" + "1" * 1500, True),  # 3001 chars, palindrome

    # Long non-palindrome
    ("1" * 1500 + "2" + "3" * 1500, False),

    # Digits and letters mixed
    ("1a2b2a1", True),
    ("1a2b3a1", False),
]
