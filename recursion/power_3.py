def isPowerOfThree(num):

    if num <= 0:
        return False

    if num == 1:
        return True

    if num % 3 == 0:
        return solution(num//3)

    return False


# isPowerOfThree(1) -> true // 1 == 3^0
# isPowerOfThree(3) -> true  // 3 == 3^1
# isPowerOfThree(5) -> false
# isPowerOfThree(9) -> true // 9 == 3^2
# isPowerOfThree(18) -> false
