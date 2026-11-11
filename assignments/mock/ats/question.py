"""
Imagine, I am given input which contains positive integers and they are sorted.
Find longest subarray in this input for which this condition holds true:
2*a > b, where a is the smallest number in subarray and b is the biggest number.

Example:
1 2 3 4 5
output: [3 4 5], 3 {Size}


Brute Force:
n2
i -> 0 to n
j -> i to n
a, b = min(arr[i:j+1]), max(arr[i:j+1])
if 2*a > b:
    max = max(ans, j-i+1)

Sliding Window:
1 2 3 4 5

[1] -> valid answer
[1 2] -> invalid answer
[2] -> valid
[2 3] -> valid
[2 3 4] -> invalid {3}
[3 4] -> valid
[3 4 5] -> valid {3}

O(n)

O(n) validation + O(n)
O(1)


Feedback:
1. Problem solving skills
    - Understand the problem well, and optimal time and space complexity.
    - Should highlight it myself before interviewer should highlight it.
    - Should add test cases.

2. Code Quality:
    - Understand how to production level code.
    - Define interface and contract.
    - There shouldn't be bugs in your code.
    - Keep your name logically correct.

Follow-up problems:
1. Candidates are able to solve upto 2.
    - People can clear the DSA round even after clearing 1.
    - Solving: 1 base + 1 followup problem.
    - Atleast explain the solution.
    
"""

class Solution:

    def max_subarray_size(self, arr: list[int]) -> int:
        # Empty array:
        if not arr:
            return 0
        if len(arr) == 1:
            return 1

        i = 0 # Start of the window:

        is_condition_met = lambda a,b: 2*a > b

        ans = 0

        # j ptr -> right of the subarray / window:
        for j in range(len(arr)):
            a, b = arr[i], arr[j]
            # condition is met then valid answer, do not need 
            # decrease the window
            if is_condition_met(a, b):
                ans = max(ans, j-i+1)

            # else if it not met, decrease the window until it is met:
            else:
                while i <= j and not is_condition_met(arr[i], arr[j]):
                    i += 1
                if is_condition_met(arr[i], arr[j]):
                    ans = max(ans, j-i+1)


        return ans



if __name__ == "__main__":
    driver = Solution()
    assert(driver.max_subarray_size([1, 2, 3, 4, 5]) == 3)
    assert(driver.max_subarray_size([1]) == 1)
    assert(driver.max_subarray_size([1, 1, 1, 1, 1]) == 5)

    print('Test passed!')
