# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # 1 Find middle of list
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 2 Reverse list2
        list2 = self.reverse(slow.next)
        slow.next = None

        # 3 combine 2 lists
        list1 = head
        while list1 and list2:
            temp1, temp2 = list1.next, list2.next
            list1.next = list2
            list2.next = temp1
            list1, list2 = temp1, temp2

    # 2 Reverse list2 func
    def reverse(self, head):
        prev, curr = None, head

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev
            