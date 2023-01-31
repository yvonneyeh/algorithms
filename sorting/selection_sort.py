"""
▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁
✏️ Description
▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔
Q. Given an unsorted array, perform selection sort in ascending order.

Examples:
• Given an array: [1] // returns [1]
• Given an array: [3, 1, 2, 4] // returns [1, 2, 3, 4]

"""

def selectionSort(array):

    size = len(array)
    for i in range(size):
        min_index = i

        for j in range(i + 1, size):
            # select the minimum element in every iteration
            if array[j] < array[min_index]:
                min_index = j
         # swapping the elements to sort the array
        (array[i], array[min_index]) = (array[min_index], array[i])

    return array


def selectionSort(array: [int]) -> [int]:
		for i in range(len(array)):
			current_min = min(array[i:])
			min_index = array[i:].index(current_min)
			array[i + min_index] = array[i]
			array[i] = current_min
		return array



# O(n^2)

# Test Cases
print(selectionSort([])) # []
print(selectionSort([1])) # [1]
print(selectionSort([3, 1, 2, 4])) # [1, 2, 3, 4]
print(selectionSort([-10, 1, 3, 8, -13, 32, 9, 5])) # [-13, -10, 1, 3, 5, 8, 9, 32]
