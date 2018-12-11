class DListNode:
    def __init__(self,val):
        self.val=val
        self.prev=self.next=null

        def reverse(self,head):
            curt=None
            while head:
                curt=head
                head=curt.next
                curt.next=curt.prev
                curt.prev=head
            return curt
