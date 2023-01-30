"""
Given an array of positive integers, find the first element that occurs k number of times.


"""


"""
Given an array of positive integers, find the first element that occurs k number of times.

Approach #1
map / dictionary to keep track of counts
iterate through array:
    increment the count for the curr item
    check count for curr item
        return early if k

time o(n)
space o(n)

havent found it

Approach #2
iterate through array:
    keep count var
    iterate through every other item:
        incr count if ===
        check if count is k

time o(n^2)
space o(1)


1, 1, 1, 2, 2, 3

time: n log n
space: o(1)
"""

def find_first_element_with_count_k(arr, k):

    element_count = {}

    for element in arr:
        element_count[element] = element_count.get(element, 0) + 1

        # if element not in element_count:
        #     element_count[element] = 1
        # else:
        #     element_count[element] += 1

        # element_count.setdefault(element, 0)
        # element_count[element] += 1

        if element_count[element] == k:
            return element

    return -1


def first_element_to_k(arr, k):
    for i in range(0,len(arr)):
        count = 1
        for j in range(i+1,len(arr)):
            if arr[i] == arr[j]:
                count += 1
        if count >= k:
            return arr[i]
    return -1

# print(first_element_to_k([], 1))
# print(first_element_to_k([1,1,1,1,1],6))
print(first_element_to_k([1,1,1,1,1],3))
                        #     i
                        #         j
# print(first_element_to_k([1,2,3,4,5,6,],88))
# print(first_element_to_k([1, 2, 3, 4], 1))
print(first_element_to_k([1], 1))

# J
function element_found_k_times(arr,k){
    let sortedArr = arr.sort((a,b)) => b-a) # a-b or b - a
    let temp = sortedArr[0]
    let count = 0
    for(let i = 0; i < arr.length; i++){
        if(arr[i] === temp){
            count++
        } else {
            temp = arr[i]
            count = 1
        }
        if(count === k){
            return arr[i]
        }
    }
    return -1
}
console.log(element_found_k_times([],))


# N
function kTimes(arr, k){
    if(k === 1) return arr[0];
    let count = 0;
    arr.sort((a,b) => b-a)
    for(let i of arr){

    }
}
console.log(kTimes([1,2,3,4,4],2))

# S
def first_element_with_count_k_sort_approach(array, k):
    cur_num = -1
    count = -1
    for index, value in enumerate(sorted(array)):
        if value != cur_num:
            count = 1
            cur_num = value
        else:
            count += 1

        if count >= k:
            return cur_num

    return -1
