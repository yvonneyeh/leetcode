#21. Merge Two Sorted Lists
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:

        head = sort_list = ListNode(0)

        while(l1 and l2):
            if (l1.val < l2.val):
                sort_list.next = l1
                l1 = l1.next
                sort_list = sort_list.next

            elif (l1.val >= l2.val):
                sort_list.next = l2
                l2 = l2.next
                sort_list = sort_list.next

        sort_list.next = l1 or l2
        return head.next

# Runtime: 40 ms, faster than 42.18% of Python3 online submissions for Merge Two Sorted Lists.
# Memory Usage: 14.4 MB, less than 32.31% of Python3 online submissions for Merge Two Sorted Lists.
