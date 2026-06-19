# 142. Linked List Cycle II
# Linked List and Fast and Slow Pointers
# TC: O(n)
# SC: O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(0)

        slow=head
        fast=head

        

        while fast and fast.next:
            slow=slow.next
            dummy=fast
            fast=fast.next.next

            if(slow==fast):
                dummy=head
                while dummy != slow:
                    dummy = dummy.next
                    slow = slow.next

                return dummy    

        return None
        

