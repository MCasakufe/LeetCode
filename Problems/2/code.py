# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        def get_number(ListNode):
            number = ''
            while ListNode:
                number += str(ListNode.val)
                ListNode = ListNode.next
            return int(number[::-1])
        result = str(get_number(l1) + get_number(l2))[::-1]
        listNode_result = ListNode(0)
        pivot = listNode_result
        for number in result:
            pivot.next = ListNode(int(number))
            pivot = pivot.next
        return listNode_result.next