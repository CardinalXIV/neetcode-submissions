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

        # if the next node not in seen set, can traverse
        while current not in seen:
            seen.add(current)

            # check if current node is the end
            if current is None:
                return False

            current = current.next

        # if next node is seen cause not caught in while loop, cycle exists
        return True