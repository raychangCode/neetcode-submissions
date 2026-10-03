"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        copy_memo = {None: None}

        curr = head
        while curr:
            copy = Node(curr.val)
            copy_memo[curr] = copy
            curr = curr.next

        dummy = head
        while dummy:
            copy = copy_memo[dummy]
            copy.next = copy_memo[dummy.next]
            copy.random = copy_memo[dummy.random]
            dummy = dummy.next

        return copy_memo[head]