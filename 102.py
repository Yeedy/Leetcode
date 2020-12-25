from collections import deque  # 双端队列


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 102. 二叉树的层序遍历
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        # 双端队列
        # 44ms(52.13%), 14.9MB(10.14%)
        if not root:
            return []

        ans = []
        d = deque()
        d.append(root)

        while d:
            length = len(d)
            level_ans = []
            for i in range(length):
                node = d.popleft()
                level_ans.append(node.val)
                if node.left:
                    d.append(node.left)
                if node.right:
                    d.append(node.right)
            ans.append(level_ans)

        return ans

        # 队列
        # 40ms(75.13%), 15.1MB(5.98%)
        # if not root:
        #     return []
        #
        # queue = [root]
        # ans = []
        #
        # while queue:
        #     length = len(queue)
        #     level_ans = []
        #     for i in range(length):
        #         cur = queue.pop(0)
        #         level_ans.append(cur.val)
        #         if cur.left:
        #             queue.append(cur.left)
        #         if cur.right:
        #             queue.append(cur.right)
        #
        #     ans.append(level_ans)
        #
        # return ans

    # 普通的BFS（非题解）
    # def bfs(self, root: TreeNode) -> List[List[int]]:
    #     if not root:
    #         return []
    #
    #     queue = [root]
    #     ans = []
    #
    #     while queue:
    #         cur = queue.pop(0)
    #         ans.append(cur.val)
    #         if cur.left:
    #             queue.append(cur.left)
    #         if cur.right:
    #             queue.append(cur.right)
    #
    #     return ans
