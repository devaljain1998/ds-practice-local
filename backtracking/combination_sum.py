from typing import List


def solve(candidates, start, target, result, temp):
    # Base cases:
    if target == 0:
        result.add(tuple(temp[:]))
        return
    elif start == len(candidates):
        return

    if candidates[start] <= target:
        # Include:
        temp.append(candidates[start])
        solve(candidates, start, target-candidates[start], result, temp)
        temp.pop()

        # Exclude:
        solve(candidates, start+1, target, result, temp)
    else:
        # Exclude:
        solve(candidates, start+1, target, result, temp)


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = set()
        solve(candidates, 0, target, result, [])
        answer = []
        for r in result:
            answer.append(list(r))
        return answer


print(Solution().combinationSum([2,3,6,7], 7)) #[[2,2,3],[7]]    