# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        
        # First find middle using fast and slow
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        
        second = slow.next
        prev = slow.next = None 
        # Reverse backend
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp


        # Merge both lists
        linkedList2 = prev
        linkedList1 = head

        while linkedList2:
            temp1, temp2 = linkedList1.next, linkedList2.next
            linkedList1.next = linkedList2
            linkedList2.next = temp1
            linkedList1 = temp1
            linkedList2 = temp2





        