from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 103. 二叉树的锯齿形层序遍历
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        # 双端队列
        # 32ms(95.83%), 15.1MB(12.63%)
        if not root:
            return []

        ans = []
        queue = deque()
        queue.append(root)
        reverse = False

        while queue:
            lenght = len(queue)
            level_queue = deque()
            for i in range(lenght):
                node = queue.popleft()
                if reverse:
                    level_queue.appendleft(node.val)
                else:
                    level_queue.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            ans.append(list(level_queue))
            reverse = not reverse

        return ans

        # 队列
        # 32ms(95.83%), 15.1MB(21.01%)
        # if not root:
        #     return []
        #
        # ans = []
        # queue = [root]
        # level = 1
        #
        # while queue:
        #     length = len(queue)
        #     level_ans = []
        #     for i in range(length):
        #         node = queue.pop(0)
        #         level_ans.append(node.val)
        #         if node.left:
        #             queue.append(node.left)
        #         if node.right:
        #             queue.append(node.right)
        #
        #     if level % 2 == 0:
        #         ans.append(level_ans[::-1])
        #     else:
        #         ans.append(level_ans)
        #     level += 1
        #
        # return ans
