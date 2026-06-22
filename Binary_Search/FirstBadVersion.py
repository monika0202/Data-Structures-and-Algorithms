# 278. First Bad Version
# Binary Search
# TC: O(log n)
# SC: O(1)

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        low = 1
        high = n

        while low < high:
            mid = low + (high - low) // 2

            if isBadVersion(mid):
                high = mid
            else:
                low = mid + 1

        return low
        
