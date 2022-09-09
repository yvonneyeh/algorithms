"""
Award Budget Cuts
The awards committee of your alma mater (i.e. your college/university) asked for your assistance with a budget allocation problem they’re facing. Originally, the committee planned to give N research grants this year. However, due to spending cutbacks, the budget was reduced to newBudget dollars and now they need to reallocate the grants. The committee made a decision that they’d like to impact as few grant recipients as possible by applying a maximum cap on all grants. Every grant initially planned to be higher than cap will now be exactly cap dollars. Grants less or equal to cap, obviously, won’t be impacted.

Given an array grantsArray of the original grants and the reduced budget newBudget, write a function findGrantsCap that finds in the most efficient manner a cap such that the least number of recipients is impacted and that the new budget constraint is met (i.e. sum of the N reallocated grants equals to newBudget).

Analyze the time and space complexities of your solution.

Example:

input:  grantsArray = [2, 100, 50, 120, 1000], newBudget = 190

output: 47 # and given this cap the new grants array would be
           # [2, 47, 47, 47, 47]. Notice that the sum of the
           # new grants is indeed 190
Constraints:

[time limit] 5000ms

[input] array.double grantsArray

0 ≤ grantsArray.length ≤ 20
0 ≤ grantsArray[i]
[input] double newBudget

[output] double
"""

"""
function findGrantsCap(grantsArray, newBudget):
    n = grantsArray.length

    # sort the array in a descending order.
    grantsArray.sort(reverse=true)

    # pad the array with a zero at the end to
    # cover the case where 0 <= cap <= grantsArray[i]
    grantsArray.push(0)

    # calculate the total amount we need to
    # cut back to meet the reduced budget
    surplus = sum(grantsArray) - newBudget

    # if there is nothing to cut, simply return
    # the highest grant as the cap. Recall that
    # the grants array is sorted in a descending
    # order, so the highest grant is positioned
    # at index 0
    if (surplus <= 0):
        return grantsArray[0]

    # start subtracting from surplus the
    # differences (“deltas”) between consecutive
    # grants until surplus is less or equal to zero.
    # Basically, we are testing out, in order, each
    # of the grants as potential lower bound for
    # the cap. Once we find the first value that
    # brings us below zero we break
    for i from 0 to n-1:
        surplus -= (i+1) * (grantsArray[i] - grantsArray[i+1]):
        if (surplus <= 0):
            break

    # since grantsArray[i+1] is a lower bound
    # to our cap, i.e. grantsArray[i+1] <= cap,
    # we  need to add to grantsArray[i+1] the
    # difference: (-total / float(i+1), so the
    # returned value equals exactly to cap.
    return grantsArray[i+1] + (-surplus / float(i+1))
"""

def get_salary_cap(salaries, budget):
    salaries.sort()
    cap = budget / len(salaries)

    for i, salary in enumerate(salaries):
        if salary <= cap:
            excess = cap - salary
            remaining = (len(salaries) - 1 ) - i
            cap += (excess / remaining)


    return cap

    # Time Complexity: O(N⋅log(N))
    # Space Complexity: O(1)

# Sort salaries
# Calculate a cap by dividing the budget by the number of grants.
# For all salaries which are less or equal to the cap calculate a difference between the current cap and salary. Increase the cap on the difference / rest salaries.
# If curr salary is greater than the cap we should return the cap. Cause there are no more salaries that can share their stock up to the cap.



salaries = [100, 300, 200, 400]
budget = 800
# Output: 250
# Explanation: k should be 250, so the total salary after the reduction 100 + 250 + 200 + 250 is exactly equal to 800.

print(get_salary_cap(salaries, budget))
