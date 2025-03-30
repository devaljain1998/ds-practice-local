#                   Original Number (k swaps left)
#                      /        |         \
#            Swap(start, i1)  Swap(start, i2)  Swap(start, i3) ...
#                  /   \          /   \          /   \
#    Swap(start+1, j1) ...  Swap(start+1, j2)  Swap(start+1, j3) ...


def is_valid(num: str, start: int, i: int, max_digit: int) -> bool:
    current_digit: int = int(num[start])
    choice: int = int(num[i])
    
    return choice > current_digit and choice == max_digit

def swap_digits(num: str, i: int, j: int) -> str:
    num_list = list(num)
    num_list[i], num_list[j] = num_list[j], num_list[i]
    return ''.join(num_list)


def solve(num: str, k: int, start: int, num_of_digits: int) -> int:
    # Base condition -> if k == 0, or if start == len(num) - 1 then return the num:
    if k == 0 or start == num_of_digits - 1:
        return int(num)
    
    # Current best choice:
    max_num: int = int(num)
    
    # Recursive choices:
    # Only swap with nodes which is greater than in the remaining arr:
    max_digit: int = int(max(num[start:]))
    
    # Iterate through all the digits and try only to swap the current digit (start)
    # with the max_digit:
    for i in range(start, len(num)):
        if is_valid(num, start, i, max_digit):
            swapped_num: str = swap_digits(num, start, i)
            # Call for the next digit:
            result: int = solve(swapped_num, k - 1, start + 1, num_of_digits)
            max_num = max(max_num, result) # Update max_num
            
            # Again swap back the number:
            swapped_num: str = swap_digits(swapped_num, i, start)
    
    # Condition where we don't swap but go to the next digit:
    max_num = max(solve(num, k, start + 1, num_of_digits), max_num)
    
    return int(max_num)

def find_maximum_num(s: str, k: int) -> int:
    return solve(s, k, 0, len(s))

print('s = "1234567", k = 4: ', find_maximum_num("1234567", 4))
print('s = "3435335", k = 3: ', find_maximum_num("3435335", 3))
print('s = "1034", k = 2: ', find_maximum_num("1034", 2))

# Examples :
# Input: s = "1234567", k = 4
# Output: 7654321
# Explanation: Three swaps can make the input 1234567 to 7654321, swapping 1 with 7, 2 with 6 and finally 3 with 5
# 
# Input: s = "3435335", k = 3
# Output: 5543333
# Explanation: Three swaps can make the input 3435335 to 5543333, swapping 3 with 5, 4 with 5 and finally 3 with 4 
# 
# Input: s = "1034", k = 2
# Output: 4301
# 
# Constraints:
# 1 ≤ s.length ≤ 25
# 1 ≤ k ≤ 7