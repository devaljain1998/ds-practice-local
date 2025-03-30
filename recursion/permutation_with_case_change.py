from typing import List, Set

def permutations(s: str) -> List[str]:
    # Base Condition:
    if not s:
        return []
    if len(s) <= 1:
        return [s]
    
    # Recursive Condition:
    final_permutations: Set[str] = {''}
    for i in range(len(s)):
        chosen_char = s[i]
        remaining_str = s[i+1:]
        
        permutations1 = permutations(remaining_str)
        permutations_with_lower_case = [chosen_char.lower()]
        permutations_with_upper_case = [chosen_char.upper()]
        permutations_with_lower_case += [chosen_char.lower() + permutation for permutation in permutations1]
        permutations_with_upper_case += [chosen_char.upper() + permutation for permutation in permutations1]

        # Merge these lists into the set:
        final_permutations.update(permutations1)
        final_permutations.update(permutations_with_lower_case)
        final_permutations.update(permutations_with_upper_case)        
    
    return sorted(list(final_permutations))

# Test Cases:
print(permutations("ab"))
print(permutations("abc"))
print(permutations("a1b2"))