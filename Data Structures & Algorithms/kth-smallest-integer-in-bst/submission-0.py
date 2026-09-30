# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def parcours(root, l):
            if root is None:
                return l
            parcours(root.left, l)
            l.append(root.val)
            parcours(root.right, l)
            return l
        l = []
        
        parcours(root, l)
        print(l)
        return l[k - 1]
        