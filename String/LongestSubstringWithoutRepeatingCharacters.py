# 3. Longest Substring Without Repeating Characters
# Two pointer approach
# TC: O(n)
# SC: O(min(n, k)) #k is the size of the character set.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        s2=set()
        left=0
        maxLen=0

        for right in range(len(s)):
            while(s[right] in s2):
                s2.remove(s[left])
                left+=1

            s2.add(s[right])
            maxLen=max(maxLen,right-left+1) 

        return maxLen   