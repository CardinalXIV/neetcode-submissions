# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # both lists are sorted
        # get a pointer to point at head of each list for comparison
        current1, current2 = list1, list2
        # create a dummy empty nodes
        tail = ListNode()
        head = tail

        # while both lists not empty
        while current1 and current2:
            # if first list node val less or equal to 2nd list node, append it first
            if current1.val <= current2.val:
                tail.next = current1
                tail = tail.next
                current1 = current1.next
            
            # 2nd list node val smaller than 1st list node val, append 2nd list node
            # elif current2.val < current1.val:
            else:
                tail.next = current2
                tail = tail.next
                current2 = current2.next

        if current1:
            tail.next = current1

        else:
            tail.next = current2
            
        return head.next
