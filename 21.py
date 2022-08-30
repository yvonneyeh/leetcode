#21. Merge Two Sorted Lists
"""
Easy

You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.



Example 1:


Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: list1 = [], list2 = []
Output: []
Example 3:

Input: list1 = [], list2 = [0]
Output: [0]


Constraints:

The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:

        head = tail = ListNode(0)
        # create dummy node as to not insert into empty linked list

        while (l1 and l2):
            if (l1.val < l2.val):
                tail.next = l1
                l1 = l1.next
            elif (l1.val >= l2.val):
                tail.next = l2
                l2 = l2.next
            tail = tail.next

        tail.next = l1 or l2
        # for cases where one list is empty, or add whatever is left
        return head.next # returns everything newly added, excluding dummy node


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = temp = ListNode()
        while l1 != None and l2 != None:

            if l1.val < l2.val: #2
                temp.next = l1 #3
                l1 = l1.next #4
            else:
                temp.next = l2
                l2 = l2.next
            temp = temp.next
        temp.next = l1 or l2  #5
        return dummy.next #6

# Runtime: 40 ms, faster than 42.18% of Python3 online submissions for Merge Two Sorted Lists.
# Memory Usage: 14.4 MB, less than 32.31% of Python3 online submissions for Merge Two Sorted Lists.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        starter = ListNode()
        tail = starter

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else: #list2.next <= list1.next
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2

        return starter.next
