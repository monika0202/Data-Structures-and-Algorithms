# 35. Search Insert Position
# Binary Search
# TC: O(log n)
# SC: O(1)

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n=len(nums)
        high=n-1
        low=0
       
        while(low<=high):
            mid=low+(high-low)//2
            if(target<nums[mid]):
                high=mid-1

            elif(target>nums[mid]):
                low=mid+1

            else:
                return mid


        return low

        