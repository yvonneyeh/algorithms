def fruits_into_baskets(fruits):
    start = 0
    max_fruit = 0
    fruit_frequency = {}

    for end in range(len(fruits)):
        right_fruit = fruits[end]
        if right_fruit not in fruit_frequency:
            fruit_frequency[right_fruit] = 0
        fruit_frequency[right_fruit] += 1

        while len(fruit_frequency) > 2:
            left_fruit = fruits[start]
            fruit_frequency[left_fruit] -= 1
            if fruit_frequency[left_fruit] == 0:
                del fruit_frequency[left_fruit]
            start += 1

        max_fruit = max(max_fruit, end - start + 1)

    return max_fruit

def main():
    print("['A', 'B', 'C', 'A', 'C'] ->", (fruits_into_baskets(['A', 'B', 'C', 'A', 'C'])))
    print("['A', 'B', 'C', 'B', 'B', 'C'] ->",(fruits_into_baskets(['A', 'B', 'C', 'B', 'B', 'C'])))


main()
