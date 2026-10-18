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

        # if the fast node not None, can traverse as fast will hit None before slow
        while fast and fast.next is not None:

            slow = slow.next
            fast = fast.next.next

            # if the slow and fast pointer meet, cycle exists
            if fast is slow:
                return True

        # if fast node is None, cycle doesn't exists
        return False