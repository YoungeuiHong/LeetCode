# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def closestNodes(self, root, queries):
        """
        :type root: Optional[TreeNode]
        :type queries: List[int]
        :rtype: List[List[int]]
        """
        answer = []
        before = None
        curr = root

        for query in queries:
            while curr != None:
                if curr.val == query:
                   answer.append([query, query])
                   break
                elif before != None and before.val > query and curr.val < query:
                    right = curr
                    while right != None:
                        min_child = right.val
                        right = right.right
                    answer.append([min_child, before])
                    break
                elif before != None and before.val < query and curr.val > query:
                    left = curr
                    while left != None:
                        max_child = left.val
                        left = left.left
                    answer.append([before, max_child])
                    break
                else:
                    if curr.val > query:
                        curr = curr.left
                    else:
                        curr = curr.right
                    before = curr

            if curr == None and before != None:
                if before.val > query:
                    answer.append([-1, before.val])
                else:
                    answer.append([before.val, -1])

        return answer


        