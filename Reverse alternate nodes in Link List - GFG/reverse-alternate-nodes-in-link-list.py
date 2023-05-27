"""
  reverse alternate nodes and append at the end
  The input list will have at least one element
  Node is defined as
class Node:

	# Constructor to initialize the node object
	def __init__(self, data):
		self.data = data
		self.next = None

"""
class Solution:
    def reverseLL(self,head):
        new_head = None
        while head != None:
            store = head.next
            head.next = new_head
            new_head = head
            head = store
        return new_head
    
    def rearrange(self, head):
        if head == None:
            return None
        oh=head
        ot=head
        eh=head.next
        et=head.next
        while et!=None and et.next!=None:
            ot.next=ot.next.next
            ot=ot.next
            if et.next!=None:   #note
                et.next=et.next.next
                et=et.next
        eh = self.reverseLL(eh)
        ot.next=eh
        return head



#{ 
 # Driver Code Starts
# Node Class
class Node:
    # Constructor to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None


# Linked list class contains node object
class LinkedList:
    # Constructor to initialize head
    def __init__(self):
        self.head = None

    # Function to insert a new node at the beginning
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data, end=" ")
            temp = temp.next
        print()


# Code execution starts here
if __name__ == '__main__':
    t = int(input())
    while (t > 0):
        llist = LinkedList()
        n = int(input())
        values = list(map(int, input().strip().split()))
        for i in reversed(values):
            llist.push(i)
            
        Solution().rearrange(llist.head)
        llist.printList()
        t -= 1
# Contributed by: Harshit Sidhwa
# } Driver Code Ends