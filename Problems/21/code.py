# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not list1 and not list2:
            return None
        if not list2 or (list1 and list1.val < list2.val):
                pivot = list1
                list1 = list1.next
        elif list2:
            pivot = list2
            list2 = list2.next
        merged_list = pivot
        while list1 or list2:
            if not list2 or (list1 and list1.val < list2.val):
                pivot.next = list1
                list1 = list1.next
            else:
                pivot.next = list2
                list2 = list2.next
            pivot = pivot.next
        return merged_list