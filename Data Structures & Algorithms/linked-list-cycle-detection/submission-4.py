# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # set a current node to the head of the linked list
        current = head
        # seen set of nodes
        seen = set()

        # edge case for empty input
        if current is None:
            return False

        # if the next node not in seen set, can traverse
        while current.next not in seen:
            seen.add(current)
            current = current.next

            if current is None:
                return False

        return True