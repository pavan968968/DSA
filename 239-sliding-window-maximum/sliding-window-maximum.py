from collections import deque

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        dq = deque()
        result = []

        for i in range(len(nums)):
            # Remove indices from front if they are out of the window
            if dq and dq[0] < i - k + 1:
                dq.popleft()

            # Remove indices from back if the current number is bigger
            while dq and nums[i] > nums[dq[-1]]:
                dq.pop()

            # Add current index to deque
            dq.append(i)

            # Append result once first window is complete
            if i >= k - 1:
                result.append(nums[dq[0]])

        return result
# 