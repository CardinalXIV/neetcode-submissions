# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # set current node to the head of the list
        current = head
        # when the list is reversed, what does the original head point to? 
        prev = None
        nextnode = None
        
        # While loop till list ends, and for each iteration switch the head to the prev node
        while current is not None:
            # switch between the current node and the previous node (don't need change val just
            # change where the node is pointing!)
            # save the node ahead
            # flip the current node’s arrow back
            # move prev up
            # move current up
            
            nextnode = current.next
            current.next = prev
            prev = current
            current = nextnode
            
        return prev