# Maximum Common Prefix Amongst an Array of Strings
# Given a large list of strings find the longest common prefix shared by all the strings.
#  Example:
# Input: ["appleairpods", "appleipod", "apples", "applewatch"]
# Output: "apple"
# (All strings start with "apple")
# Preference : Trie for a larger data set.

inputs = ["appleairpods", "appleipod", "apples", "applewatch"]
inputs = sorted(inputs)
max_substring_so_far_len = 0
max_substring_so_far: str = ''
cur_substring_len = 0
cur_substring: str = ''
for c1, c2, c3, c4 in zip(inputs[0], inputs[1], inputs[2], inputs[3]):
    if c1 == c2 == c3 == c4:
        cur_substring_len += 1
        cur_substring += c1
        max_substring_so_far_len = max(max_substring_so_far_len, cur_substring_len)
        if max_substring_so_far_len > len(max_substring_so_far):
            max_substring_so_far = cur_substring
    else:
        break

print(max_substring_so_far, max_substring_so_far_len)

# O(n x m)
# n: length of the smallest string
# m: number of input strings
# Space: O(1)


# KMP Algorithm



# appleairpods
# appleipod
# apples
# applewatch

# I'll find the smallest string:
# apples
# start = 0, end = 5, mid = 2
# substring = app
def is_valid(inputs, substring, start, mid) -> bool:
    for string in inputs:
        if not string[start:mid+1] == substring:
            return False
    return True

start = 0
end = 5
smallest_string = 'apples'
answer = -1
while start <= end:
    mid = start + (end-start) // 2
    substring = smallest_string[:mid+1]
    
    if is_valid(inputs, smallest_string, start, mid):
        answer = mid
        start = mid + 1
    else:
        end = mid - 1

# 1st iteration: "app" in all the strings
# 2nd iteration: I'll be only computing "pl" in all the string
# 3rd iteration: "es" in all the string
# 4th iteration: "e" in all the strings
answer = 5

prefix_string = smallest_string[:answer + 1] # apple
# Time complexity: mxlog(n)