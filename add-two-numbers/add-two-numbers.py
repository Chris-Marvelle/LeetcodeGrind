# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import deque
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        result = ListNode(0)
        dummy = result
        carry = 0
        
        
        while (l1 or l2):
            l1_num = l1.val if l1 else 0
            l2_num = l2.val if l2 else 0 
            
            step_sum = l1_num + l2_num + carry
            carry = step_sum // 10
            last_digit = step_sum % 10
            result.next = ListNode(last_digit)
            if l1:l1 = l1.next 
            if l2: l2 = l2.next
            result = result.next
        if carry > 0: result.next = ListNode(carry)
        return dummy.next