# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None: return True
        if root is not None and root.left is None and root.right is None: return True
        if root.left is None or root.right is None: return False
        left_stack,right_stack = [root.left],[root.right]
        left,right = [],[]
        while left_stack:
            curr = left_stack.pop()
            if curr is not None:
                left.append(curr.val)
                left_stack.append(curr.left)
                left_stack.append(curr.right)
            if curr is None:
                left.append('null')
        while right_stack:
            curr = right_stack.pop()
            if curr is not None:
                right.append(curr.val)
                right_stack.append(curr.right)
                right_stack.append(curr.left)
            if curr is None:
                right.append('null')
        print(left)
        print(right)
        return left == right
        
        
                