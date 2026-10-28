# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        '''
        find mid 
        reverse second half
        merge alternatively
        '''

        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        def reverse(head):
            curr = head
            prev = None
            while curr:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            return prev
        
        rev = reverse(slow)

        curr1 = head
        curr2 = rev

        while curr2.next:
            temp1 = curr1.next
            temp2 = curr2.next

            curr1.next = curr2
            curr2.next = temp1

            curr1 = temp1
            curr2 = temp2