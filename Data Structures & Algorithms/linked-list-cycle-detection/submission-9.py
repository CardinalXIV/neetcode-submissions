# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # set a fast and slow node to the head node of the linked list
        fast = head
        slow = head

        # if the slow node not None, can traverse as slow increments by 1
        while slow and fast is not None:
            
            # if there is a next node, fast jumps 2, slow jumps 1
            if fast.next is None:
                return False

            slow = slow.next
            fast = fast.next.next

            # if the slow and fast pointer meet, cycle exists
            if fast is slow:
                return True

        # if fast node is None, cycle doesn't exists
        return False