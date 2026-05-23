def is_valid(stalls, k, mx):
    cows = 1
    prev = stalls[0]

    for i in range(1, len(stalls)):
        if stalls[i] - prev >= mx:
            cows += 1
            prev = stalls[i]

            if cows >= k:
                return True

    return False


def aggressiveCows(stalls, k):
    stalls.sort()

    start = 1
    end = stalls[-1] - stalls[0]

    ans = -1

    while start <= end:
        mid = start + (end - start) // 2

        if is_valid(stalls, k, mid):
            ans = mid
            start = mid + 1
        else:
            end = mid - 1

    return ans


print(aggressiveCows([1, 2, 3], 2))          # 2
print(aggressiveCows([0, 3, 4, 7, 10, 9], 4)) # 3