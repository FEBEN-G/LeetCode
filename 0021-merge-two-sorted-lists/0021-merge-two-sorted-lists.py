class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1, list2):
        
        dummy = ListNode()
        current = dummy

        
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        
        if list1:
            current.next = list1
        elif list2:
            current.next = list2

       
        return dummy.next


def list_to_listnode(lst):
    if not lst:
        return None
    dummy = ListNode()
    current = dummy
    for val in lst:
        current.next = ListNode(val)
        current = current.next
    return dummy.next


def listnode_to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result