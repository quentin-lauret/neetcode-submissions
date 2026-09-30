# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def is_valid(root, max_, min_):
            if root is None:
                return True
            if root.val < max_ and root.val > min_:
                return is_valid(root.left, root.val, min_) and is_valid(root.right, max_, root.val)
            return False
        return is_valid(root, float('inf'), -float('inf'))