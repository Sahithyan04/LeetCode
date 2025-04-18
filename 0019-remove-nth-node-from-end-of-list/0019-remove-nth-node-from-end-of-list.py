# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        new_node = ListNode(0)
        new_node.next = head
        dummy = new_node

        fast = dummy
        slow = dummy

        if not head.next:
            return None

        for i in range(n):
            fast = fast.next
        
        
        print(fast)
        while fast and fast.next:
            fast = fast.next
            slow = slow.next

        print(slow.val)  
        slow.next = slow.next.next
        return dummy.next
        