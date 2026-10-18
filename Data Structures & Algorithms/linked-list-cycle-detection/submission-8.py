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

        # if the current node not in seen set, can traverse
        while current not in seen:
            # check if current node is the end
            if current is None:
                return False

            # if there is a next node, add current to seen set and go to next node
            seen.add(current)
            current = current.next

        # if current node is seen cause not caught in while loop, cycle exists
        return True