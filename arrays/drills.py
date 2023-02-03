"""
Most frequent element in array
Follow-up: In the case of a tie-breaker, pick the largest value.
"""
def find_most_frequent_element(arr):
    if not arr:
        return None

    num_count = {}
    max_item = None
    max_count = float("-inf")

    for num in arr:
        num_count[num] = num_count.get(num, 0) + 1
        if num_count[num] > max_count:
            max_item = num
            max_count = num_count[num]

    return max_item

print(find_most_frequent_element([1,2,3,1,2,3,1]))
print(find_most_frequent_element([]))


"""
Least frequent element in array
Follow-up: In the case of a tie-breaker, pick the largest value.
"""

def find_least_frequent_element(arr):
    if not arr:
        return None

    arr.sort()

    num_count = {}
    min_item = None
    min_count = float("inf")

    for num in arr:
        num_count[num] = num_count.get(num, 0) + 1
        if num_count[num] <= min_count:
            min_count = num_count[num]
            min_item = num

    # print(min_items)

    return min_item

print(find_least_frequent_element([1,2,3,1,2,3,1]))
print(find_least_frequent_element([1,2,3,1,2,3,1,3]))
print(find_least_frequent_element([]))



"""
Count the number of elements with exactly N occurrences
([8, 9, 8, 3, 9, 4], 2) returns 2
"""

def count_elements_matching_occurences(arr, n):
    num_count = {}
    matches = []

    for num in arr:
        num_count[num] = num_count.get(num, 0) + 1

    for num, count in num_count.items():
        if count == n:
            matches.append(key)

    return len(matches)

def count_elements_matching_occurences(arr, n):

    if not arr:
        return None

    num_count = {}
    result = 0

    for num in arr:
        num_count[num] = num_count.get(num, 0) + 1

    for num, count in num_count.items():
        if count == n:
            result += 1

    return result

print(count_elements_matching_occurences([8, 9, 8, 3, 9, 4], 2))
print(count_elements_matching_occurences([8, 9, 8, 3, 9, 4], 0))
print(count_elements_matching_occurences([1,2,3,1,2,3,1,3], 1))
print(count_elements_matching_occurences([], 2))

"""
Given an array with all number appearing 2 times and one number appearing 3 times, find the number that shows up 3 times.
Follow-up: Use a set instead of a hashmap/dictionary
Follow-up: Given an array with all numbers appearing 3 times and one number appearing only twice, find the number that only shows up twice. You must use hashsets.
"""

def find_triplet(arr):
    if not arr:
        return None

    num_count = {}

    for num in arr:
        num_count[num] = num_count.get(num, 0) + 1

    for num, count in num_count.items():
        if count == 3:
            return num
        else:
            return None

print(find_triplet([1,2,1,2,1]))
print(find_triplet([1,2,1,2]))


def find_triplet_with_set(arr):
    if not arr:
        return None

    num_count = set()

    for num in arr:
        if num in num_count:
            num_count.remove(num)
        else:
            num_count.add(num)

    if not num_count:
        return None

    return num_count.pop()

print(find_triplet_with_set([1,2,1,2,1]))
print(find_triplet_with_set([1,2,1,2]))
