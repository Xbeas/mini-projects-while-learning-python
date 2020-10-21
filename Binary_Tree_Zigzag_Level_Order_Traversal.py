rom collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        # empty binary tree (edge case)
        if not root:
            return []
        # we want to do bfs here, but the direction of traversal will change
        # after every level (use delimiter for that), using a variable to
        # track direction
        zigzagLevelOrderTraversal = []
        # a deque supports faster append operation from both sides
        zigzagLevel = deque()
        bfsQueue = deque()
        leftToRight = True  # change at every level
        # using an integer delimiter since all other elements in deque will be
        # TreeNode objects
        delimiter = -1
        bfsQueue.append(root)
        bfsQueue.append(delimiter)
        while bfsQueue:
            node = bfsQueue.popleft()
            if node == delimiter:
                zigzagLevelOrderTraversal.append(zigzagLevel)
                # we only proceed further if bfsQueue is not empty
                if bfsQueue:
                    # change leftToRight since level is changing
                    leftToRight = False if leftToRight else True
                    zigzagLevel = deque()   # empty current level elements
                    bfsQueue.append(delimiter)
            else:
                if leftToRight:
                    zigzagLevel.append(node.val)
                else:
                    zigzagLevel.appendleft(node.val)
                if node.left:
                    bfsQueue.append(node.left)
                if node.right:
                    bfsQueue.append(node.right)
        return zigzagLevelOrderTraversal
