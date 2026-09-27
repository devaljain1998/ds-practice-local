def is_valid(arr, k, mx) -> bool:
    students = 1
    pages = 0

    for p in arr:
        pages += p

        if pages > mx:
            pages = p
            students += 1

            if students > k:
                return False
    
    return students <= k

def findPages(arr: [int], n: int, k: int) -> int:
    if len(arr) < k:
        return -1

    start = max(arr)
    end = sum(arr)

    max_pages = -1
    while start <= end:
        mid = start + (end - start) // 2

        if is_valid(arr, k, mid):
            max_pages = mid
            end = mid - 1
        else:
            start = mid + 1

    return max_pages
