# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right




class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q1 = [root]
        q2 = []
        l = []
        while len(q1) > 0:
            sub_l = []
            for i in range(len(q1)):
                v = q1[i]
                if v != None:
                    q2.append(v)
                    sub_l.append(v.val)
            q1 = []
            if sub_l:
                l.append(sub_l)
            for i in range(len(q2)):
                q1.append(q2[i].left)
                q1.append(q2[i].right)
            q2 = []
        return l


        