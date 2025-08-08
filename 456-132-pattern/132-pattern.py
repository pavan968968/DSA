class Solution(object):
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        stack = []
        third = float('-inf')  # This will represent nums[k]

        # Traverse from right to left
        for num in reversed(nums):
            if num < third:
                return True  # Found nums[i] < nums[k] < nums[j]
            while stack and num > stack[-1]:
                third = stack.pop()  # Update third to be a valid nums[k]
            stack.append(num)

        return False  # No pattern found
