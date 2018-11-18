# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if root.val == val:
            return root
        elif val > root.val and root.right:
            self.searchBST(root.right, val)
        elif val < root.val and root.left:
            self.searchBST(root.left, val)
        else:
            return None
        
sol = Solution()
root = ""
val = ""
print(sol.searchBST(root, val))