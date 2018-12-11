class NodeCircle:
    def __init__(self, val):
        self.val=val
        self.next=None

    def has_circle(self,head):
        slow=head
        fast=head
        while(slow and fast):
            fast=fast.next
            slow=slow.next
            if fast:
                fast=fast.next
            if fast==slow:
                break
            if fast and slow and (fast==slow):
                return True
            else:
                return False