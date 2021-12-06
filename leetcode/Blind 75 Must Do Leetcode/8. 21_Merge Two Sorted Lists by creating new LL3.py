# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 and l2: return l2
        if not l2 and l1: return l1
        if not l2 and not l1: return None

        l3 = tmp = ListNode()

        while 1:
            if l1.val < l2.val:
                tmp.val = l1.val
                if l1.next: l1 = l1.next
                else: break
            else:
                tmp.val = l2.val
                if l2.next: l2 = l2.next
                else: break

            tmp.next = ListNode()
            tmp = tmp.next

        if not l1.next and l1.val > l2.val:
            tmp.next = l1
        elif not l1.next: tmp.next = l2
        else: tmp.next = l1
        
        return l3
