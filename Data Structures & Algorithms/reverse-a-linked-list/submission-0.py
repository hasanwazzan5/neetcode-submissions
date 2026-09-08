# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        lst = []
        while current:
            lst.append(current)
            current = current.next

        for i in range(len(lst)-1, -1, -1):
            if i == 0:
                lst[i].next = None
            else:
                lst[i].next = lst[i-1]

        if lst:
            return lst[-1]
        else:
            return None