# 83. Remove Duplicates from Sorted List

# Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None: # handles edge case where the list is empty
            return head
        current = head  # initialize current with the address of head node
        while current.next != None:  # traverse list until 2nd to last node
            if current.val == current.next.val:  # if value of current is equal to the value of previous, means it exists in the linked list
                temp = current.next  # increment value of current
                current.next = current.next.next
                del temp
            else:
                current = current.next  # otherwise increment current pointer
        return head  # return the sorted linked list without any duplicate element
