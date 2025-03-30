from lcs import lcs

def transform_string(a: str, b: str) -> tuple[int, int]:
    lcs_len = lcs(a, b)
    deletions = len(a) - lcs_len
    insertions = len(b) - lcs_len
    return deletions, insertions

# Test cases
print(transform_string("heap", "pea"))  # Output: (2, 1) (2 deletions, 1 insertion)
print(transform_string("geeksforgeeks", "geeks"))  # Output: (8, 0) (8 deletions, 0 insertions)
print(transform_string("abc", "def"))  # Output: (3, 3) (3 deletions, 3 insertions)
print(transform_string("abcd", "abcd"))  # Output: (0, 0) (no operations needed)