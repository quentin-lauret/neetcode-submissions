# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def is_in(root, p):
            if root is None:
                return False
            return root == p or is_in(root.left, p) or is_in(root.right, p)
        if root is None:
            return None
        l = self.lowestCommonAncestor(root.left, p, q)
        r = self.lowestCommonAncestor(root.right, p, q)
        if l != None:
            return l
        if r != None:
            return r
        if is_in(root, p) and is_in(root, q):
            return root
       
            
            
        