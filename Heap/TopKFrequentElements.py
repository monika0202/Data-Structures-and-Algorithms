# 347. Top K Frequent Elements
# heap
# TC: O(n)
# SC: O(n)

from collections import Counter
import heapq


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        return heapq.nlargest( k,
        count.keys(),
        key=count.get
        )         



# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:

#         freq=Counter(nums)

#         freq=sorted(freq.items(),key=lambda x: x[1],reverse=True)
#         return [item[0] for item in freq[:k]]
