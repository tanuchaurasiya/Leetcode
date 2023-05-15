# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]: 
        c=0 
        t=head
        while(t!=None):
            c+=1
            t=t.next 
        p1=head
        p2=head
        for i in range(k-1):
            p1=p1.next 
        for i in range(c-k):
            p2=p2.next
        p1.val,p2.val=p2.val,p1.val 
        return head
        
        