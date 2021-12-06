# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# method1 
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 and l2: return l2
        if not l2 and l1: return l1
        if not l2 and not l1: return None
        
        l3 = tmp = ListNode()
        
        while 1:
            if l1.val < l2.val:
                tmp.next = l1
                tmp = tmp.next
                
                if l1.next: l1 = l1.next
                else: break
            else:
                tmp.next = l2
                tmp = tmp.next
                
                if l2.next: l2 = l2.next
                else: break

        if not l2.next and l2.val > l1.val:
            tmp.next = l2
        elif not l2.next: tmp.next = l1
        else: tmp.next = l2
        
        return l3.next


# method2
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 and l2: return l2
        if not l2 and l1: return l1
        if not l2 and not l1: return None
        
        l3 = tmp = ListNode()
        
        while l1 and l2:
            if l1.val < l2.val:
                tmp.next = l1
                l1 = l1.next
            else:
                tmp.next = l2
                l2 = l2.next
            tmp = tmp.next
        
        if l1: tmp.next = l1
        elif l2: tmp.next = l2
        
        return l3.next

