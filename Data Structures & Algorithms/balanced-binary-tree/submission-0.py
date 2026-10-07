# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def bal(node):            
            if not node:
                return [True,0]

            lv, lh = bal(node.left)
            rv, rh = bal(node.right)

            if lv and rv and abs(lh-rh) <= 1:
                return [True, 1 + max(lh, rh)]
            
            return [False,1 + max(lh, rh)]
        
        return bal(root)[0]