# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue, res = [(root, 0)], []
        while queue:
            node, level = queue.pop(0) # pop front
            if node:
                if len(res) < level + 1:
                    res.append([])
                res[level].append(node.val)
                queue.append((node.left, level + 1))  # push back
                queue.append((node.right, level + 1)) # push back
        return res