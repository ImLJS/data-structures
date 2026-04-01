# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        max_len = 1
        stack = [(root, 1)]
        while stack:
            node, max_value = stack.pop()
            if node.right:
                stack.append((node.right, max_value+1))
            if node.left:
                stack.append((node.left,max_value+1))
            max_len = max(max_len, max_value)
        
        return max_len