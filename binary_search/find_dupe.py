# Write a function which finds an integer that appears more than once in our list. Don't modify the input! (If there are multiple duplicates, you only need to find one of them.)


# Naive:
def find_repeat(numbers):
    numbers_seen = set()
    for number in numbers:
        if number in numbers_seen:
            return number
        else:
            numbers_seen.add(number)

    # Whoops--no duplicate
    raise Exception('no duplicate!')

# O(n) time
# O(n) space

# Brute force: take each number in the range 1...n,
# for each, Walk through the list to see if it appears twice.

def find_repeat_brute_force(numbers):
    for needle in range(1, len(numbers)):
        has_been_seen = False
        for number in numbers:
            if number == needle:
                if has_been_seen:
                    return number
                else:
                    has_been_seen = True

    # Whoops--no duplicate
    raise Exception('no duplicate!')

# O(1) space
# O(n^2) time

# Sort the input list in place! ↴
    # 1. Do an in-place sort of the list (for example an in-place merge sort).
    # 2. Walk through the now-sorted list from left to right.
    # 3. Return as soon as we find two adjacent numbers which are the same.
    # 4. This'll keep us at O(1)O(1) space and bring us down to O(n\lg{n})O(nlgn) time.
# If we do this recursively, we'll incur a space cost in the call stack! Do it iteratively instead.

# Solution
# Our approach is similar to a binary search, except we divide the range of possible answers in half at each step, rather than dividing the list in half.

# 1. Find the number of integers in our input list which lie within the range 1... n/2
# 2. Compare that to the number of possible unique integers in the same range.
# 3. If the number of actual integers is greater than the number of possible integers, we know there’s a duplicate in the range 1... n/2, so we iteratively use the same approach on that range.
# 4. If the number of actual integers is not greater than the number of possible integers, we know there must be duplicate in the range n/2+1...n, so we iteratively use the same approach on that range.
# 5. At some point, our range will contain just 1 integer, which will be our answer.


def find_repeat(numbers):
    floor = 1
    ceiling = len(numbers) - 1

    while floor < ceiling:
        # Divide our range 1..n into an upper range and lower range
        # (such that they don't overlap)
        # Lower range is floor..midpoint
        # Upper range is midpoint+1..ceiling
        midpoint = floor + ((ceiling - floor) // 2)
        lower_range_floor, lower_range_ceiling = floor, midpoint
        upper_range_floor, upper_range_ceiling = midpoint+1, ceiling

        # Count number of items in lower range
        items_in_lower_range = 0
        for item in numbers:
            # Is it in the lower range?
            if item >= lower_range_floor and item <= lower_range_ceiling:
                items_in_lower_range += 1

        distinct_possible_integers_in_lower_range = (
            lower_range_ceiling
            - lower_range_floor
            + 1
        )
        if items_in_lower_range > distinct_possible_integers_in_lower_range:
            # There must be a duplicate in the lower range
            # so use the same approach iteratively on that range
            floor, ceiling = lower_range_floor, lower_range_ceiling
        else:
            # There must be a duplicate in the upper range
            # so use the same approach iteratively on that range
            floor, ceiling = upper_range_floor, upper_range_ceiling

    # Floor and ceiling have converged
    # We found a number that repeats!
    return floor

# Complexity
# O(1) space
# O(n log n) time
