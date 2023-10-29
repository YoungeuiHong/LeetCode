import heapq

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        num_heap = []

        for i in nums:
            heapq.heappush(num_heap, (-i, i))

        while k > 0:
            popped = heapq.heappop(num_heap)
            k -= 1

        return popped[1]