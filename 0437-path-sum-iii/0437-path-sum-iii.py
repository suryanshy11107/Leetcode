# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: int
        """

        self.numOfPaths = 0
        self.dfs(root, targetSum)
        return self.numOfPaths

    def dfs(self, node, target):
        if node is None:
            return

        self.test(node, target)
        self.dfs(node.left, target)
        self.dfs(node.right, target)

    def test(self, node, target):
        if node is None:
            return

        if node.val == target:
            self.numOfPaths += 1

        self.test(node.left, target - node.val)
        self.test(node.right, target - node.val)