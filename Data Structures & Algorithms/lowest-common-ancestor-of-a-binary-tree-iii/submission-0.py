"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        book = []
        while p is not None:
            book.append(p)
            p = p.parent
        while q is not None:
            if q in book:
                return q
            q = q.parent
        return None
        