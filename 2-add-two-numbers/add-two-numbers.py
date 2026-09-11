# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        head = dummy
        carry = 0
        while (l1 or l2):
            s = carry
            if l1:
                s += l1.val
            if l2:
                s += l2.val
            
            carry = s // 10
            if (s >= 10):
                s = s % 10
            dummy.next = ListNode(s)
            dummy = dummy.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        if carry:
            dummy.next = ListNode(carry)
        return head.next
        