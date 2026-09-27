from typing import List
from collections import deque

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """
        Approach:
        1. Calculate the final time required to reach the target with the given position and the speed -> hence creating a time array.
        2. Find out the nearest greater to right time and also fleet_count(defaulting 1).
            logic: because prior car will catch up to the next car fleet if it is faster
            ngr -> higher time in seconds
            fleet_count -> ngr(time, fleet_count)[1] + 1
        3. Append this to stack:
            stack.append({time, fleet_count)
        4. If no ngr is found then increment the fleet_gp and append to the stack
        5. we need to return the fleet group
        """

        speed_and_pos = sorted(zip(position, speed), key=lambda x: x[0])

        # Fill the times array:
        times = [-1 for _ in range(len(speed_and_pos))]
        for i, (pos, kmph) in enumerate(speed_and_pos):
            times[i] = round((target-pos)/kmph, 2)
        
        # Fill out ngr
        fleet_gp = 0
        stack = deque()
        for i in range(len(position)-1, -1, -1):
            time = times[i]
            if not stack:
                fleet_gp += 1
            else:
                while stack and stack[-1] < time:
                    stack.pop()
                if not stack:
                    fleet_gp += 1
                else:
                    prev_time = stack.pop() # Since the new car will become the part of the fleet we can safely pop it
                    stack.append(max(time, prev_time))
                    continue
            
            stack.append(time)

        return fleet_gp

# Test cases:
# 10, [0,4,2], [2,1,3]
print(Solution().carFleet(10, [0,4,2], [2,1,3]))    # Output: 1