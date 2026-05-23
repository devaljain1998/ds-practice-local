from typing import List

class Solution:
    def is_valid(self, weights: List[int], days: int, capacity: int) -> bool:
        days_required = 0

        current_weight = 0
        for w in weights:
            current_weight += w
            if current_weight > capacity:
                days_required += 1
                current_weight = w
            
            if days_required > days:
                return False
        
        return (days_required + 1)<= days

    def shipWithinDays(self, weights: List[int], days: int) -> int:
        start = max(weights)
        end = sum(weights)

        min_capacity = -1
        while start <= end:
            # Our calculated capacity:
            mid = start + (end-start) // 2

            # Check if weights can be shipped in these days:
            if self.is_valid(weights, days, mid):
                min_capacity = mid
                end = mid - 1
            else:
                start = mid + 1

        return min_capacity


# Test cases:
solution = Solution()
print(solution.shipWithinDays(weights = [1,2,3,4,5,6,7,8,9,10], days = 5)) # Expected output: 15