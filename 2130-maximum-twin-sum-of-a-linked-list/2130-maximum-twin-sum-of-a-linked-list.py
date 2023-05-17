# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        l=[] 
        t=head 
        while(t!=None):
            l.append(t.val) 
            t=t.next 
        i=0
        j=len(l)-1 
        maxx=l[i]+l[j]
        while(i<j):
            if maxx<l[i]+l[j]: 
                maxx=l[i]+l[j]  
            i+=1 
            j-=1 
        return maxx