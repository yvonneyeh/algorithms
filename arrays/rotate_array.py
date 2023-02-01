'''
Rotate all elements in an array by k positions. This isn't a difficult problem, but the in-place O(1) space solution isn't apparent. It's the kind of thing that once you see it, it's obvious and trivial to code, but getting there might take a bit of an ah-ha moment.

[Writup on HackerRank](https://www.hackerrank.com/challenges/ctci-array-left-rotation/problem)


EXAMPLE(S)
[1,2,3,4,5] k = 0 -> [1,2,3,4,5]
[1,2,3,4,5] k = 5 -> [1,2,3,4,5] (same as above, % k to get remainder)
[1,2,3,4,5] k = 2 -> [3,4,5,1,2]
[1,2,3,4,5] k = 7 -> [3,4,5,1,2]
[], k = 3 -> []
[1], k = 3 -> [1]

[0,0,0,0,0]

Approach 1: Create a new pre-sized array and move each element over to the rotated postion.
Time = O(n) Linear time because we are doing one pass over out input and doing constant work (copy to new array) each iteration.
Space = O(n) For this approach we are relying on a copy of the original array equal in size.

Approach 2:

[1,2,3,4,5] 1,2,3,4,5-> [3,4,5,1,2]
[5,4,3,2,1] k = 2

5,4,3 -> 3,4,5
2,1 -> 1,2

- reverse array in place
- mod k, so that it isn't longer than the length of the array
- k becomes pivot number to split reversed array in half
-
[1,2,3,4,5]
[1,2,5,4,3]
[3,4,1,2,3]

arr[a], arr[b] = arr[b], arr[a]

[1,2,3,4,5]
[4,2,3,1,5]
[4,5,3,1,2]
[3,5,4,1,2]
[3,1,4,5,2]
[3,1,2,5,4]

Time: O(n)
Space: O(1) - in place


FUNCTION SIGNATURE
func rotate(input: [Int], by k: Int) -> [Int]
'''

arr = [1,2,3,4,5]
k = 2
result = [4,5,1,2,3]
def rotate(arr, k):
    if len(arr) < 2:
        return arr

    k = k % len(arr)
    if k == 0: return arr

    l = 0
    r = len(arr) - 1

    print(f"start: {arr}")

    # reverse array in place [5,4,3,2,1]
    while l < r:
        arr[l], arr[r] = arr[r], arr[l]
        l += 1
        r -= 1

    print(f"reversed: {arr}")

    # reverse first half of the array [5,4,3] -> [3,4,5]
    l = 0
    r = k - 1 # len(arr) - k - 1
    while l < r:
        arr[l], arr[r] = arr[r], arr[l]
        l += 1
        r -= 1

    print(f"first half: {arr}")

     # reverse second half of the array [2,1] -> [1,2]
    l = k
    r = len(arr) - 1
    while l < r:
        arr[l], arr[r] = arr[r], arr[l]
        l += 1
        r -= 1

    print(f"second half: {arr}")

    return arr


# rotate([1,2,3,4,5], 2)


print(rotate([1,2,3,4,5], 0))
print(rotate([1,2,3,4,5], 1))
print(rotate([1,2,3,4,5], 2))
print(rotate([1,2,3,4,5], 5))
print(rotate([1,2,3,4,5], 7))
print(rotate([], 2))
print(rotate([1], 2))
