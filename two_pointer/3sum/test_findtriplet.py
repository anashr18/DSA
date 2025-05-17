import pytest
from findtriplet import three_sum

@pytest.mark.parametrize("nums,expected", [
    # Basic test with multiple triplets
    ([-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]]),
    # No triplets
    ([1, 2, 3, 4, 5], []),
    # All zeros
    ([0, 0, 0, 0], [[0, 0, 0]]),
    # Duplicates in input, only unique triplets
    ([0, 0, 0, 0, 0], [[0, 0, 0]]),
    # Negative and positive numbers
    ([-2, 0, 1, 1, 2], [[-2, 0, 2], [-2, 1, 1]]),
    # Minimum length input, no triplet
    ([1, 2, -3], [[-3, 1, 2]]),
    # No solution, minimum length
    ([1, 2, 3], []),
    # Large numbers
    ([1000, -1000, 0, 0], [[-1000, 0, 1000]]),
    # Multiple valid triplets, unordered input
    ([3, -2, 1, 0, -1, 2, -1], [[-2, -1, 3], [-2, 1, 1], [-1, 0, 1], [-1, -1, 2]]),
])
def test_three_sum(nums, expected):
    result = three_sum(nums)
    # Convert lists to sets of tuples for unordered comparison
    result_set = {tuple(sorted(triplet)) for triplet in result}
    expected_set = {tuple(sorted(triplet)) for triplet in expected}
    assert result_set == expected_set
