# 347. Top K Frequent Elements
# Hashing
# TC: O(n log n)
# SC: O(n)

from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq=Counter(nums)

        freq=sorted(freq.items(),key=lambda x: x[1],reverse=True)
        return [item[0] for item in freq[:k]]