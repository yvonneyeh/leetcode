#234. Palindrome Linked List

"""
Easy

Given the head of a singly linked list, return true if it is a palindrome or false otherwise.

Example 1:
Input: head = [1,2,2,1]
Output: true

Example 2:
Input: head = [1,2]
Output: false


Constraints:

The number of nodes in the list is in the range [1, 105].
0 <= Node.val <= 9


Follow up: Could you do it in O(n) time and O(1) space?"""


class Node:
  def __init__(self, val, next = None):
    self.val = val
    self.next = next

def createPalindromeLL(arr: list[int]) -> Node:
    if not arr:
        return None

    sentinel = Node(None)
    curr = sentinel

    for i in range(len(arr)):
        curr.next = Node(arr[i])
        curr = curr.next

    for i in range(len(arr) - 2, -1, -1):
        curr.next = Node(arr[i])
        curr = curr.next

    return sentinel.next


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        slow = head
        fast = head

        # find middle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse 2nd half
        prev = None
        current = slow
        while current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp

        # check from front to back
        left = head
        right = prev
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next

        return True


            
