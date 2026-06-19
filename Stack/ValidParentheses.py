# 20. Valid Parentheses
# Linked List and Fast and Slow Pointers
# TC: O(n)
# SC: O(n)

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {
        ')': '(',
        ']': '[',
        '}': '{'
        }

        for ch in s:
            if ch in mapping.values():
                stack.append(ch)
            else:
                if not stack:
                    return False
                top = stack.pop()

                if top != mapping[ch]:
                    return False

        return len(stack) == 0