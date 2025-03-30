from typing import List, Set


def subsets(s: str) -> List[str]:
    # Base Condition:
    if not s:
        return []
    if len(s) <= 1:
        return [s]
    
    # Recursive Condition:
    final_subsets: Set[str] = {''}
    for i in range(len(s)):
        chosen_char = s[i]
        remaining_str = s[i+1:]
        
        subsets1 = subsets(remaining_str)
        subsets2 = [chosen_char + subset for subset in subsets1]
        subsets2.append(chosen_char)
        
        # Merge these two lists into the set:
        final_subsets.update(subsets1)
        final_subsets.update(subsets2)
    
    return sorted(list(final_subsets))

# Test Cases:
print(subsets("abc"))