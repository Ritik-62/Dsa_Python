class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Creating a dummy node
        dummy = ListNode(0)
        dummy.next = head

        prev = dummy

        while prev.next and prev.next.next:
            first = prev.next
            second = first.next

            # swap now
            first.next = second.next
            second.next = first
            prev.next = second

            prev = first
        return dummy.next