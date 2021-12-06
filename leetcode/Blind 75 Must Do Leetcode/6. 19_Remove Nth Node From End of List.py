# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if not n: return head     # n=0
        if not head.next: return None      # head->next = NULL

        tmp=head
        p=None

        while tmp.next:     # tmp->next != NULL
            # print(tmp.val,tmp.next)
            # print(" -> ")
            tmp = tmp.next
            n-=1
            if not n: p=head
            if p and n: p=p.next
            
        if not p: return head.next
        p.next = p.next.next
        
        return head
