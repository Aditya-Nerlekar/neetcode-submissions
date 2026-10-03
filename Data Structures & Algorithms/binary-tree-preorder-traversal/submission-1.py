# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # res = []
        
        # def preorder(node):
        #     if not node:
        #         return

        #     res.append(node.val)
        #     preorder(node.left)
        #     preorder(node.right)
        
        # preorder(root)
        # return res

        res = []
        s = []
        cur = root

        while s or cur:
            if cur:
                res.append(cur.val)
                s.append(cur.right)
                cur = cur.left
            else:
                cur = s.pop()

        return res
