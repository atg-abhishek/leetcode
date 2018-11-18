# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        count = 0
        temp = head
        while(head):
            if head.next:
                head = head.next
                count += 1
            else:
                break
        import math 
        for i in range(math.ceil(count/2)):
            temp = temp.next
        return temp