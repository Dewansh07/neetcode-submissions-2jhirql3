# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = fast = head

        def reverse(head):
            cur = head
            prev = None
            while cur:
                temp = cur.next
                cur.next = prev
                prev = cur
                cur = temp
            return prev

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        rev = reverse(slow)

        cur1 = head
        cur2 = rev
        while cur2.next:
            temp1 = cur1.next
            temp2 = cur2.next

            cur1.next = cur2
            cur2.next = temp1

            cur1 = temp1
            cur2 = temp2


