# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # res = []

        # def postorder(node):
        #     if not node:
        #         return 

        #     postorder(node.left)
        #     postorder(node.right)
        #     res.append(node.val)

        # postorder(root)
        # return res

        s = [root]
        vis = [False]
        res = []

        while s:
            curr, v = s.pop(), vis.pop()
            if curr:
                if v:
                    res.append(curr.val)
                else:
                    s.append(curr)
                    vis.append(True)
                    s.append(curr.right)
                    vis.append(False)
                    s.append(curr.left)
                    vis.append(False)

        return res
