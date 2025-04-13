
# Link: https://www.geeksforgeeks.org/problems/allocate-minimum-number-of-pages0937/1?itm_source=geeksforgeeks&itm_medium=article&itm_campaign=practice_card
class Solution:
    
    @staticmethod
    def is_valid(arr, k, max_pages) -> bool:
        students = 1
        pages = 0
        
        for n in arr:
            # Max pages are allowed:
            # Keeping handing over the books to current student
            if pages + n <= max_pages:
                pages += n
            # Max pages exceeded so current student cannot take the book any more
            # have to give to a new student:
            else:
                students += 1
                pages = n
                
                # If students exceed the number of students
                # then it means cannot be solved through this max_pages variable:
                if students > k:
                    return False
        
        # return students == k
        # NOTE: Changed the return condition in is_valid to just True since we only care if it's possible to allocate with the given maximum pages limit, not whether exactly k students are used
        return True
    
    #Function to find minimum number of pages.
    def findPages(self, arr: list[int], k: int) -> int:
        # Base case:
        if len(arr) == 1:
            return arr[0] if k == 1 else -1
        elif k > len(arr):
            return -1
        
        start: int = max(arr)
        end: int = sum(arr)
        
        answer = -1
        while start <= end:
            mid = start + (end - start) // 2
            
            if self.is_valid(arr, k, mid):
                answer = mid
                end = mid - 1
            else:
                start = mid + 1
                
        
        return answer
        
# Examples:
# Input: arr[] = [12, 34, 67, 90], k = 2
# Output: 113
# Explanation: Allocation can be done in following ways:
# [12] and [34, 67, 90] Maximum Pages = 191
# [12, 34] and [67, 90] Maximum Pages = 157
# [12, 34, 67] and [90] Maximum Pages = 113.
# Therefore, the minimum of these cases is 113, which is selected as the output.
print(Solution().findPages([12, 34, 67, 90], 2)) # 113

# Input: arr[] = [15, 17, 20], k = 5
# Output: -1
# Explanation: Allocation can not be done.
print(Solution().findPages([15, 17, 20], 5)) # -1

# Input: arr[] = [22, 23, 67], k = 1
# Output: 112
print(Solution().findPages([22, 23, 67], 1)) # 112

# Input:
# 15 10 19 10 5 18 7
# 5
# Output:
# 25
print(Solution().findPages([15,10,19,10,5,18,7], 5)) # 25