# 3. Contain Duplicate
# Hashing
# TC: O(n)
# SC: O(n)

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        s=set()
        for i in nums:
            if(i in s):
                return True

            s.add(i)

        return False        
        